// Exact membership of a word in H_M = <d^5 : d reduced over {a,b}, 1 <= |d| <= M> <= F2
// via Stallings folding. Rust port of ../fold.py, scaled with compact arrays + union-find.
//
// Labels: 0=a,1=b,2=A,3=B ; inverse label = l xor 2.
// Membership(target) == target spells a closed loop at the base of the folded core.
//
// The Stallings folded core is canonical (folding is confluent), so fold order does not
// affect membership results -- this must match fold.py at every M (cross-validation).
//
// Build:  rustc -O -C opt-level=3 -C lto=fat -C codegen-units=1 fold.rs -o fold
// Run:    ./fold <M> <targets_file>

use std::env;
use std::fs;
use std::io::{self, Write, BufWriter};

const NIL: u32 = u32::MAX;

#[inline(always)]
fn inv(l: u8) -> u8 { l ^ 2 }

fn char_to_label(c: u8) -> u8 {
    match c {
        b'a' => 0,
        b'b' => 1,
        b'A' => 2,
        b'B' => 3,
        _ => panic!("bad char {}", c as char),
    }
}

// ---- Root generation: reduced words length 1..M, one per {w,w^-1}, no proper powers ----
struct RootGen {
    m: usize,
    buf: Vec<u8>,        // current word under construction
    packed: Vec<u8>,     // all emitted roots concatenated
    offsets: Vec<u32>,   // start index in `packed` of each root; last entry = packed.len()
    total_len: u64,      // sum of |d| over emitted roots
}

impl RootGen {
    fn new(m: usize) -> Self {
        RootGen { m, buf: Vec::with_capacity(m), packed: Vec::new(), offsets: vec![0], total_len: 0 }
    }

    // w == inv(reverse(w))?  and  w <= inv(reverse(w)) lexicographically.
    // Returns true iff w <= its formal inverse.
    fn le_inverse(w: &[u8]) -> bool {
        // inv-word[i] = inv(w[n-1-i]); compare w[i] vs inv(w[n-1-i]).
        let n = w.len();
        for i in 0..n {
            let a = w[i];
            let b = inv(w[n - 1 - i]);
            if a < b { return true; }
            if a > b { return false; }
        }
        true // equal
    }

    fn is_proper_power(w: &[u8]) -> bool {
        let n = w.len();
        let mut p = 1;
        while p < n {
            if n % p == 0 {
                let mut ok = true;
                for i in 0..n {
                    if w[i] != w[i % p] { ok = false; break; }
                }
                if ok { return true; }
            }
            p += 1;
        }
        false
    }

    fn emit(&mut self) {
        let w = &self.buf;
        if Self::le_inverse(w) && !Self::is_proper_power(w) {
            self.packed.extend_from_slice(w);
            self.offsets.push(self.packed.len() as u32);
            self.total_len += w.len() as u64;
        }
    }

    fn recurse(&mut self) {
        self.emit();
        if self.buf.len() >= self.m { return; }
        let last = *self.buf.last().unwrap();
        let forbidden = inv(last);
        for l in 0u8..4 {
            if l != forbidden {
                self.buf.push(l);
                self.recurse();
                self.buf.pop();
            }
        }
    }

    fn generate(&mut self) {
        for l in 0u8..4 {
            self.buf.push(l);
            self.recurse();
            self.buf.pop();
        }
    }
}

// ---- Folding graph: compact union-find + per-vertex [u32;4] adjacency ----
struct Graph {
    parent: Vec<u32>,
    rank: Vec<u8>,          // union-by-rank (canonical result; fold is confluent)
    adj: Vec<[u32; 4]>,
    stack: Vec<(u32, u32)>, // pending merges
    n: u32,                 // number of allocated vertices
}

impl Graph {
    fn with_capacity(v0: usize) -> Self {
        let mut g = Graph {
            parent: Vec::with_capacity(v0),
            rank: Vec::with_capacity(v0),
            adj: Vec::with_capacity(v0),
            stack: Vec::new(),
            n: 0,
        };
        g.new_vertex(); // base = 0
        g
    }

    #[inline]
    fn new_vertex(&mut self) -> u32 {
        let id = self.n;
        self.parent.push(id);
        self.rank.push(0);
        self.adj.push([NIL; 4]);
        self.n += 1;
        id
    }

    #[inline]
    fn find(&mut self, mut v: u32) -> u32 {
        while self.parent[v as usize] != v {
            let gp = self.parent[self.parent[v as usize] as usize];
            self.parent[v as usize] = gp; // path halving
            v = gp;
        }
        v
    }

    // Set adj[u][l]=v; on conflict (slot occupied by w!=v) queue a merge, keep existing.
    #[inline]
    fn set_edge(&mut self, u: u32, l: u8, v: u32) {
        let cur = self.adj[u as usize][l as usize];
        if cur == NIL {
            self.adj[u as usize][l as usize] = v;
        } else {
            let w = self.find(cur);
            if w != v {
                self.stack.push((w, v));
            }
        }
    }

    // Add an undirected labeled edge (both directions), fold-aware.
    #[inline]
    fn add_edge(&mut self, u: u32, l: u8, v: u32) {
        self.set_edge(u, l, v);
        self.set_edge(v, inv(l), u);
    }

    // Drain the merge worklist to fixpoint.
    fn fold(&mut self) {
        while let Some((a, b)) = self.stack.pop() {
            let mut x = self.find(a);
            let mut y = self.find(b);
            if x == y { continue; }
            if self.rank[x as usize] < self.rank[y as usize] {
                std::mem::swap(&mut x, &mut y);
            }
            self.parent[y as usize] = x;
            if self.rank[x as usize] == self.rank[y as usize] {
                self.rank[x as usize] += 1;
            }
            for l in 0..4 {
                let ty_raw = self.adj[y as usize][l];
                if ty_raw == NIL { continue; }
                self.adj[y as usize][l] = NIL;
                let ty = self.find(ty_raw);
                let tx_raw = self.adj[x as usize][l];
                if tx_raw == NIL {
                    self.adj[x as usize][l] = ty;
                } else {
                    let tx = self.find(tx_raw);
                    self.adj[x as usize][l] = tx;
                    if tx != ty {
                        self.stack.push((tx, ty));
                    }
                }
            }
        }
    }

    fn accepts(&mut self, labels: &[u8]) -> bool {
        let base = self.find(0);
        let mut v = base;
        for &l in labels {
            let t = self.adj[v as usize][l as usize];
            if t == NIL { return false; }
            v = self.find(t);
        }
        v == self.find(0)
    }

    fn live_count(&self) -> usize {
        (0..self.n as usize).filter(|&i| self.parent[i] as usize == i).count()
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("usage: {} <M> <targets_file>", args[0]);
        std::process::exit(2);
    }
    let m: usize = args[1].parse().expect("M must be an integer");
    let targets_file = &args[2];

    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());

    // --- generate roots ---
    let mut rg = RootGen::new(m);
    rg.generate();
    let n_roots = rg.offsets.len() - 1;
    let total_path_edges: u64 = rg.total_len * 5;
    // V0 = 1 (base) + sum over roots (5*|d| - 1)
    let v0: usize = 1 + (total_path_edges as usize - n_roots);
    writeln!(out, "M={} roots={} total_path_edges={}", m, n_roots, total_path_edges).unwrap();
    out.flush().unwrap();

    // --- build wedge of d^5 loops ---
    let mut g = Graph::with_capacity(v0);
    for r in 0..n_roots {
        let s = rg.offsets[r] as usize;
        let e = rg.offsets[r + 1] as usize;
        let root = &rg.packed[s..e];
        let l5 = root.len() * 5;
        // path base -> v1 -> ... -> v_{l5-1} -> base, spelling root repeated 5x
        let mut cur = g.find(0);
        for i in 0..l5 {
            let lab = root[i % root.len()];
            let nxt = if i == l5 - 1 { g.find(0) } else { g.new_vertex() };
            g.add_edge(cur, lab, nxt);
            cur = nxt;
        }
    }

    // --- fold ---
    g.fold();
    writeln!(out, "folded: vertices={}", g.live_count()).unwrap();
    out.flush().unwrap();

    // --- targets ---
    let content = fs::read_to_string(targets_file).expect("cannot read targets file");
    for line in content.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        let (name, word) = match line.find(char::is_whitespace) {
            Some(idx) => {
                let name = &line[..idx];
                let word = line[idx..].trim();
                (name.to_string(), word.to_string())
            }
            None => {
                let name = if line.len() > 12 { format!("{}...", &line[..12]) } else { line.to_string() };
                (name, line.to_string())
            }
        };
        let labels: Vec<u8> = word.bytes().map(char_to_label).collect();
        let r = g.accepts(&labels);
        writeln!(out, "MEMBER={} M={} {}", if r { "True" } else { "False" }, m, name).unwrap();
    }
    out.flush().unwrap();
}

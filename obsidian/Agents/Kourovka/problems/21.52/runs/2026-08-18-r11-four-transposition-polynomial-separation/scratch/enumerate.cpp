#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using Edge = std::pair<int,int>;
using Matching = std::array<Edge,4>;

static Edge norm_edge(int a, int b) {
  if (a > b) std::swap(a,b);
  return {a,b};
}

static std::string edges_string(const Matching &M) {
  std::ostringstream out;
  for (int i=0;i<4;i++) {
    if (i) out << ',';
    out << M[i].first << '-' << M[i].second;
  }
  return out.str();
}

static long long choose_ll(int n, int k) {
  if (k<0 || k>n) return 0;
  if (k>n-k) k=n-k;
  long long ans=1;
  for (int i=1;i<=k;i++) ans=ans*(n-k+i)/i;
  return ans;
}

static void pairings_rec(std::vector<int> &v, int pos,
                         std::array<Edge,4> &cur, int depth,
                         const std::function<void(const Matching&)> &emit) {
  if (pos == (int)v.size()) {
    Matching M=cur;
    for (auto &e:M) e=norm_edge(e.first,e.second);
    std::sort(M.begin(),M.end());
    emit(M);
    return;
  }
  if (depth >= 4) { std::cerr << "pairing depth failure\n"; std::exit(5); }
  int a=v[pos];
  for (int j=pos+1;j<(int)v.size();j++) {
    std::swap(v[pos+1],v[j]);
    cur[depth]=norm_edge(a,v[pos+1]);
    pairings_rec(v,pos+2,cur,depth+1,emit);
    std::swap(v[pos+1],v[j]);
  }
}

static void all_pairings(std::vector<int> vertices,
                         const std::function<void(const Matching&)> &emit) {
  std::array<Edge,4> cur;
  pairings_rec(vertices,0,cur,0,emit);
}

static void combinations_rec(int n, int k, int start, std::vector<int> &cur,
                             const std::function<void(const std::vector<int>&)> &emit) {
  if ((int)cur.size()==k) { emit(cur); return; }
  int need=k-(int)cur.size();
  for (int x=start;x<=n-need;x++) {
    cur.push_back(x);
    combinations_rec(n,k,x+1,cur,emit);
    cur.pop_back();
  }
}

static void combinations(int n, int k,
                         const std::function<void(const std::vector<int>&)> &emit) {
  std::vector<int> cur;
  combinations_rec(n,k,0,cur,emit);
}

static std::vector<int> partner(const Matching &M, int n) {
  std::vector<int> p(n);
  std::iota(p.begin(),p.end(),0);
  for (auto e:M) { p[e.first]=e.second; p[e.second]=e.first; }
  return p;
}

static int gcd_int(int a,int b) { while (b) {int t=a%b;a=b;b=t;} return a; }
static int lcm_int(int a,int b) { return a/gcd_int(a,b)*b; }

static int product_order(const Matching &A, const Matching &B, int n) {
  auto a=partner(A,n), b=partner(B,n);
  std::vector<char> seen(n,0);
  int ans=1;
  for (int s=0;s<n;s++) if (!seen[s]) {
    int len=0, v=s;
    do { seen[v]=1; len++; v=a[b[v]]; } while (!seen[v]);
    ans=lcm_int(ans,len);
  }
  return ans;
}

struct SigInfo {
  std::string label;
  Matching x,y;
  int m;
  int common;
};

static std::pair<std::string,int> signature(const Matching &X, const Matching &Y) {
  std::set<Edge> xs(X.begin(),X.end()), ys(Y.begin(),Y.end());
  int common=0;
  for (auto e:xs) if (ys.count(e)) common++;
  std::array<std::vector<std::pair<int,char>>,16> adj;
  for (auto e:xs) if (!ys.count(e)) {
    adj[e.first].push_back({e.second,'X'});
    adj[e.second].push_back({e.first,'X'});
  }
  for (auto e:ys) if (!xs.count(e)) {
    adj[e.first].push_back({e.second,'Y'});
    adj[e.second].push_back({e.first,'Y'});
  }
  struct Desc { char kind; int len; int diff; };
  std::vector<Desc> desc;
  std::array<char,16> seen{};
  for (int s=0;s<16;s++) if (!seen[s] && !adj[s].empty()) {
    std::vector<int> stack={s}; seen[s]=1;
    int vertices=0, twice_edges=0, nx2=0, ny2=0;
    bool cycle=true;
    while (!stack.empty()) {
      int v=stack.back(); stack.pop_back(); vertices++;
      if ((int)adj[v].size()!=2) cycle=false;
      for (auto [w,c]:adj[v]) {
        twice_edges++;
        if (c=='X') nx2++; else ny2++;
        if (!seen[w]) { seen[w]=1; stack.push_back(w); }
      }
    }
    int len=twice_edges/2, nx=nx2/2, ny=ny2/2;
    desc.push_back({cycle?'C':'P',len,nx-ny});
  }
  auto build=[&](int flip) {
    std::vector<std::string> parts;
    for (int i=0;i<common;i++) parts.push_back("E");
    for (auto d:desc) {
      std::ostringstream q;
      q << d.kind << d.len;
      int z=flip*d.diff;
      if (z>0) q << "X";
      if (z<0) q << "Y";
      parts.push_back(q.str());
    }
    std::sort(parts.begin(),parts.end());
    std::ostringstream q;
    for (int i=0;i<(int)parts.size();i++) { if (i) q << '+'; q << parts[i]; }
    return q.str();
  };
  std::string a=build(1), b=build(-1);
  return {std::min(a,b),common};
}

static Matching compress_outside(const Matching &Y, int &m) {
  std::vector<int> ext;
  for (auto e:Y) for (int v:{e.first,e.second}) if (v>=8) ext.push_back(v);
  std::sort(ext.begin(),ext.end());
  ext.erase(std::unique(ext.begin(),ext.end()),ext.end());
  std::map<int,int> ren;
  for (int i=0;i<(int)ext.size();i++) ren[ext[i]]=8+i;
  Matching Z=Y;
  for (auto &e:Z) {
    if (e.first>=8) e.first=ren[e.first];
    if (e.second>=8) e.second=ren[e.second];
    e=norm_edge(e.first,e.second);
  }
  std::sort(Z.begin(),Z.end());
  m=8+(int)ext.size();
  return Z;
}

int main() {
  const Matching X={Edge{0,1},Edge{2,3},Edge{4,5},Edge{6,7}};
  std::map<std::string,SigInfo> sigs;
  combinations(16,8,[&](const std::vector<int>& verts) {
    all_pairings(verts,[&](const Matching &Y0) {
      if (Y0==X) return;
      auto [lab,common]=signature(X,Y0);
      if (!sigs.count(lab)) {
        int m;
        Matching Y=compress_outside(Y0,m);
        auto check=signature(X,Y);
        if (check.first!=lab || check.second!=common) {
          std::cerr << "compression signature failure\n"; std::exit(2);
        }
        sigs.emplace(lab,SigInfo{lab,X,Y,m,common});
      }
    });
  });

  std::cout << "META\tformat\tFOUR_MATCHING_LOCAL_V1\n";
  std::cout << "META\tsignature_count\t" << sigs.size() << "\n";
  int id=0;
  std::set<int> all_orders;
  for (auto &[lab,S]:sigs) {
    std::cout << "SIG\t" << id << '\t' << (S.common?1:0) << '\t' << S.m
              << '\t' << lab << '\t' << edges_string(S.x) << '\t'
              << edges_string(S.y) << '\t' << product_order(S.x,S.y,S.m) << "\n";
    std::map<std::tuple<int,int,int>,long long> coeff;
    for (int j=0;j<=8;j++) {
      int k=8-j;
      if (k>S.m) continue;
      long long total=0;
      combinations(S.m,k,[&](const std::vector<int>& internal) {
        std::vector<int> verts=internal;
        for (int t=0;t<j;t++) verts.push_back(S.m+t);
        all_pairings(verts,[&](const Matching &Z) {
          int p=product_order(S.x,Z,S.m+j);
          int q=product_order(S.y,Z,S.m+j);
          coeff[{j,p,q}]++;
          all_orders.insert(p); all_orders.insert(q);
          total++;
        });
      });
      long long expected=choose_ll(S.m,k)*105;
      std::cout << "TOTAL\t" << id << '\t' << j << '\t' << total << '\t' << expected << "\n";
      if (total!=expected) { std::cerr << "total mismatch\n"; return 3; }
    }
    for (auto &[key,c]:coeff) {
      auto [j,p,q]=key;
      std::cout << "C\t" << id << '\t' << j << '\t' << p << '\t' << q << '\t' << c << "\n";
    }
    // Coordinates are oriented.  Downstream we use N_{p,q}+N_{q,p} for p<q,
    // which is intrinsic to the unordered endpoint pair represented by `lab`.
    id++;
  }
  std::cout << "ORDERS";
  for (int q:all_orders) std::cout << '\t' << q;
  std::cout << "\n";
  return 0;
}

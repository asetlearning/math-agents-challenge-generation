# Apply the exact C2-cocycle nondegeneracy screen to the complete exact list
# of class-at-least-3 SMP groups of order 128 obtained by
# catalogue_small_smp_class.g.  A single GAP process avoids startup overhead.

ids128 := [1735,1736,1751,1752,1753,1754,1758,1759,1760,1880,1881,1883,
           1884,1893,1897,1924,1925,1927,1949,1950,1970,1971,1985,1986,
           1987,2020,2021,2310,2311,2317,2318];
noquit:=true;
requirederived:=true;
stopafterfirst:=true;
for id128 in ids128 do
  ordtarget:=128;
  idtarget:=id128;
  Read("Agents/Kourovka/problems/12.15/scratch/screen_nondegenerate_c2_cocycles.g");
od;
QUIT;

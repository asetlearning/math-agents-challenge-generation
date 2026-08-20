# Bounded exact-arithmetic rescreen of the non-Taylor source parameterization.
# Bounds are inherited from the earlier screen: 1<=t<=100, 1<=a3<=1000.
x := Indeterminate(Rationals,"x");
rawcount := 0;; spherecount := 0;; paritycount := 0;; spectralcount := 0;;
schemecount := 0;; kreincount := 0;; absolutecount := 0;; qcount := 0;;
smallest := fail;; smallestv := fail;;
survivors := [];;

AbsoluteProductBound := function(ii,jj,multiplicities)
  if ii=jj then
    return multiplicities[ii]*(multiplicities[ii]+1)/2;
  fi;
  return multiplicities[ii]*multiplicities[jj];
end;

for t in [1..100] do
  for a in [1..1000] do
    den := t^2-a-1;
    if den > 0 and (a*(a+1)) mod den = 0 then
      c := a*(a+1)/den-1;
      if IsInt(c) and c >= 1 then
        k := t*(c+1)+a;; b1 := t*c;; b2 := a+1;; c3 := t*(c+1);;
        a1 := k-b1-1;; a2 := k-b2-c;;
        if a1 >= 0 and a2 >= 0 then
          rawcount := rawcount+1;
          k2 := k*b1/c;; k3 := k2*b2/c3;
          if IsInt(k2) and IsInt(k3) then
            spherecount := spherecount+1;
            if (k*a1) mod 2=0 and (k2*a2) mod 2=0 and (k3*a) mod 2=0 then
              paritycount := paritycount+1;
              v := 1+k+k2+k3;
              B := [[0,k,0,0],[1,a1,b1,0],[0,c,a2,b2],[0,0,c3,a]];
              fac := Factors(CharacteristicPolynomial(B));
              if Length(fac)=4 and ForAll(fac,f->Degree(f)=1) then
                roots := List(fac,function(f)
                  local cc;
                  cc := CoefficientsOfUnivariatePolynomial(f);
                  return -cc[1]/cc[2];
                end);
                nonprincipal := Difference(roots,[k]);
                if Length(nonprincipal)=3 then
                  M := [List([1..3],i->1),nonprincipal,List(nonprincipal,z->z^2)];
                  rhs := [v-1,-k,v*k-k^2];
                  mult := SolutionMat(TransposedMat(M),rhs);
                  if mult<>fail and ForAll(mult,m->IsInt(m) and m>0) then
                    spectralcount := spectralcount+1;
                    eig := Concatenation([k],nonprincipal);
                    multiplicities := Concatenation([1],mult);
                    p2 := z -> (z^2-a1*z-k)/c;
                    p3 := z -> ((z-a2)*p2(z)-b1*z)/c3;
                    P := List(eig,z->[1,z,p2(z),p3(z)]);
                    valencies := [1,k,k2,k3];
                    Q := List([1..4],rr->List([1..4],jj->multiplicities[jj]*P[jj][rr]/valencies[rr]));
                    qpar := function(ii,jj,hh)
                      return Sum([1..4],rr->P[hh][rr]*Q[rr][ii]*Q[rr][jj])/v;
                    end;
                    ppar := function(ii,jj,hh)
                      return Sum([1..4],ee->multiplicities[ee]*P[ee][ii]*P[ee][jj]*P[ee][hh])/(v*valencies[hh]);
                    end;
                    qorders := [];
                    for perm in PermutationsList([2,3,4]) do
                      ord := Concatenation([1],perm);; good := true;
                      for jj in [1..4] do
                        for hh in [1..4] do
                          qq := qpar(ord[2],ord[jj],ord[hh]);
                          if qq < 0 or (AbsInt(hh-jj)>1 and qq<>0) then good:=false; fi;
                        od;
                      od;
                      if good and ForAll([1..3],jj->qpar(ord[2],ord[jj],ord[jj+1])>0) then
                        Add(qorders,ord);
                      fi;
                    od;
                    schemefeasible := ForAll([1..4],ii->ForAll([1..4],jj->ForAll([1..4],hh->
                      IsInt(ppar(ii,jj,hh)) and ppar(ii,jj,hh)>=0)));
                    if schemefeasible then schemecount:=schemecount+1; fi;
                    kreinfeasible := ForAll([1..4],ii->ForAll([1..4],jj->ForAll([1..4],hh->
                      qpar(ii,jj,hh)>=0)));
                    if schemefeasible and kreinfeasible then kreincount:=kreincount+1; fi;
                    absolutefeasible := schemefeasible and kreinfeasible and ForAll([1..4],ii->ForAll([ii..4],jj->
                      Sum(Filtered([1..4],hh->qpar(ii,jj,hh)<>0),hh->multiplicities[hh]) <=
                      AbsoluteProductBound(ii,jj,multiplicities)));
                    if absolutefeasible then absolutecount:=absolutecount+1; fi;
                    if absolutefeasible and not IsEmpty(qorders) then
                      qcount:=qcount+1;
                      Add(survivors,[v,t,a,c,k,b1,b2,c3,k2,k3,a1,a2,eig,multiplicities,qorders]);
                      if smallestv=fail or v<smallestv then
                        smallestv:=v;
                        smallest:=[t,a,c,k,b1,b2,c3,v,eig,multiplicities,qorders,k2,k3,a1,a2];
                      fi;
                    fi;
                  fi;
                fi;
              fi;
            fi;
          fi;
        fi;
      fi;
    fi;
  od;
od;

Print("bounds: 1<=t<=100, 1<=a3<=1000\n");
Print("raw_parameter_count=",rawcount,"\n");
Print("sphere_integral_count=",spherecount,"\n");
Print("all_layer_handshakes_count=",paritycount,"\n");
Print("integral_spectral_multiplicity_count=",spectralcount,"\n");
Print("scheme_feasible_count=",schemecount,"\n");
Print("scheme_and_all_Krein_nonnegative_count=",kreincount,"\n");
Print("absolute_bound_feasible_count=",absolutecount,"\n");
Print("qpolynomial_and_absolute_count=",qcount,"\n");
Print("smallest_record_[t,a3,c2,k,b1,b2,c3,v,eig,mult,Qorders,k2,k3,a1,a2]=",smallest,"\n");
Sort(survivors,function(r,s) return r[1]<s[1] or (r[1]=s[1] and r{[2..8]}<s{[2..8]}); end);
Print("first_20_sorted_records_[v,t,a3,c2,k,b1,b2,c3,k2,k3,a1,a2,eig,mult,Qorders]=\n");
for i in [1..Minimum(20,Length(survivors))] do Print(survivors[i],"\n"); od;
QUIT;

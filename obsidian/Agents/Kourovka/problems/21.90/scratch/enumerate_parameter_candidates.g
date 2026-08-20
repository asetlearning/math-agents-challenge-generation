# Bounded exact-arithmetic enumeration using the necessary conditions quoted in
# Belousov--Makhnev--Nirova (2019). This searches only the non-Taylor case.
x := Indeterminate(Rationals,"x");
count := 0;
qcount := 0;
schemefeasiblecount := 0;
absolutefeasiblecount := 0;
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
        k := t*(c+1)+a; b1 := t*c; b2 := a+1; c3 := t*(c+1);
        a1 := k-b1-1; a2 := k-b2-c;
        if a1 >= 0 and a2 >= 0 then
          k2 := k*b1/c; k3 := k2*b2/c3; v := 1+k+k2+k3;
          if IsInt(k2) and IsInt(k3) then
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
                  count := count+1;
                  # Build P (eigenspaces x relations), Q (relations x eigenspaces),
                  # then test all orderings for a tridiagonal irreducible B_1^*.
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
                    ord := Concatenation([1],perm);
                    good := true;
                    for jj in [1..4] do
                      for hh in [1..4] do
                        qq := qpar(ord[2],ord[jj],ord[hh]);
                        if qq < 0 or (AbsInt(hh-jj)>1 and qq<>0) then good:=false; fi;
                      od;
                    od;
                    if good and ForAll([1..3],jj->qpar(ord[2],ord[jj],ord[jj+1])>0) then Add(qorders,ord); fi;
                  od;
                  schemefeasible := ForAll([1..4],ii->ForAll([1..4],jj->ForAll([1..4],hh->IsInt(ppar(ii,jj,hh)) and ppar(ii,jj,hh)>=0)));
                  if schemefeasible then schemefeasiblecount:=schemefeasiblecount+1; fi;
                  absolutefeasible := schemefeasible and ForAll([1..4],ii->ForAll([ii..4],jj->
                    Sum(Filtered([1..4],hh->qpar(ii,jj,hh)<>0),hh->multiplicities[hh]) <=
                    AbsoluteProductBound(ii,jj,multiplicities)));
                  if absolutefeasible then absolutefeasiblecount:=absolutefeasiblecount+1; fi;
                  if schemefeasible and not absolutefeasible then
                    Print("ABSOLUTE_BOUND_FAIL t=",t," a3=",a," c2=",c," IA={",k,",",b1,",",b2,";1,",c,",",c3,"} v=",v,"\n");
                    for ii in [1..4] do for jj in [ii..4] do
                      lhsab := Sum(Filtered([1..4],hh->qpar(ii,jj,hh)<>0),hh->multiplicities[hh]);
                      rhsab := AbsoluteProductBound(ii,jj,multiplicities);
                      if lhsab>rhsab then Print("  pair=",[ii,jj]," lhs=",lhsab," rhs=",rhsab," support=",Filtered([1..4],hh->qpar(ii,jj,hh)<>0),"\n"); fi;
                    od; od;
                  fi;
                  if absolutefeasible and not IsEmpty(qorders) then
                    qcount := qcount+1;
                    Print("t=",t," a3=",a," c2=",c," IA={",k,",",b1,",",b2,";1,",c,",",c3,"} v=",v," eig=",eig," mult=",multiplicities," Qorders=",qorders,"\n");
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
Print("candidate_count=",count," bounds: 1<=t<=100, 1<=a3<=1000\n");
Print("qpolynomial_candidate_count=",qcount,"\n");
Print("scheme_feasible_candidate_count=",schemefeasiblecount,"\n");
Print("absolute_bound_feasible_candidate_count=",absolutefeasiblecount,"\n");
QUIT;

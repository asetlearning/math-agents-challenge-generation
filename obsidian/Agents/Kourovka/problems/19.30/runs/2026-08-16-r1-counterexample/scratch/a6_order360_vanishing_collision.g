# Frozen exact screen for strategy A6-ORDER360-VANISHING-COLLISION.
#
# Coverage: each index i in [1..NumberSmallGroups(360)] exactly once.
# Target: the independently constructed permutation group AlternatingGroup(6).
# Invariant: the set (not multiset) of orders of conjugacy classes on which at
# least one member of Irr(CharacterTable(H)) is exactly zero.
#
# This file is intentionally self-contained and must not be patched after its
# hash is sent with the compute-lease request.

SetInfoLevel(InfoWarning, 0);

BoolString := function(b)
    if b then
        return "true";
    fi;
    return "false";
end;

VanishingOrderSet := function(H)
    local tbl, irr, orders, result, j;

    tbl := CharacterTable(H);
    irr := Irr(tbl);
    orders := OrdersClassRepresentatives(tbl);

    if Length(irr) = 0 then
        Error("ordinary irreducible character list is empty");
    fi;
    if ForAny(irr, chi -> Length(chi) <> Length(orders)) then
        Error("character/class-position length mismatch");
    fi;

    result := [];
    for j in [1..Length(orders)] do
        if ForAny(irr, chi -> chi[j] = 0) then
            AddSet(result, orders[j]);
        fi;
    od;
    return result;
end;

order := 360;
if not SmallGroupsAvailable(order) then
    Error("SmallGroups representatives are not available at order 360");
fi;

numberGroups := NumberSmallGroups(order);
if numberGroups < 1 then
    Error("empty SmallGroups catalogue at order 360");
fi;

target := AlternatingGroup(6);
if Size(target) <> order then
    Error("AlternatingGroup(6) did not have order 360");
fi;
if not IsSimpleGroup(target) then
    Error("AlternatingGroup(6) did not pass IsSimpleGroup");
fi;

targetId := IdGroup(target);
if targetId[1] <> order then
    Error("target IdGroup order mismatch");
fi;
targetSet := VanishingOrderSet(target);

Print("META\tgap_version\t", GAPInfo.Version, "\n");
Print("META\torder\t", order, "\n");
Print("META\tcoverage\t1..NumberSmallGroups(360)\n");
Print("META\tnumber_small_groups\t", numberGroups, "\n");
Print("META\ttarget_constructor\tAlternatingGroup(6)\n");
Print("META\ttarget_size\t", Size(target), "\n");
Print("META\ttarget_is_simple\t", BoolString(IsSimpleGroup(target)), "\n");
Print("META\ttarget_id\t", String(targetId), "\n");
Print("META\ttarget_vanishing_order_set\t", String(targetSet), "\n");
Print("ROW_HEADER\tindex\tsize\tis_target_id\tvanishing_order_set\tequals_target_set\tcollision\n");

seen := [];
equalRows := [];
collisions := [];
targetRows := [];

for i in [1..numberGroups] do
    G := SmallGroup(order, i);
    if Size(G) <> order then
        Error("SmallGroup size mismatch at index ", i);
    fi;

    vset := VanishingOrderSet(G);
    isTargetId := [order, i] = targetId;
    equalsTarget := vset = targetSet;
    collision := equalsTarget and not isTargetId;

    Add(seen, i);
    if isTargetId then
        Add(targetRows, i);
    fi;
    if equalsTarget then
        Add(equalRows, i);
    fi;
    if collision then
        Add(collisions, i);
    fi;

    Print("ROW\t", i,
          "\t", Size(G),
          "\t", BoolString(isTargetId),
          "\t", String(vset),
          "\t", BoolString(equalsTarget),
          "\t", BoolString(collision), "\n");
od;

if seen <> [1..numberGroups] then
    Error("coverage check failed: indices were not visited exactly once in order");
fi;
if Length(targetRows) <> 1 then
    Error("target-id uniqueness check failed");
fi;
if not targetRows[1] in equalRows then
    Error("the SmallGroups representative of A6 did not reproduce the target set");
fi;

Print("SUMMARY\trow_count\t", Length(seen), "\n");
Print("SUMMARY\ttarget_rows\t", String(targetRows), "\n");
Print("SUMMARY\tequal_set_rows\t", String(equalRows), "\n");
Print("SUMMARY\tcollision_rows\t", String(collisions), "\n");
Print("SUMMARY\tcollision_count\t", Length(collisions), "\n");
Print("SUMMARY\tcomplete\ttrue\n");
Print("SUMMARY\truntime_ms\t", Runtime(), "\n");

QUIT_GAP(0);

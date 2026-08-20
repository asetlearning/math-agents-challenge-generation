from pathlib import Path
import json
import re


PATHS = [
    "Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.out",
    "Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.out",
]


def parse(path):
    text = " ".join(Path(path).read_text().splitlines())
    records = []
    for part in text.split("ROW=")[1:]:
        def number(key):
            return int(re.search(key + r"= *([0-9]+)", part).group(1))

        row = int(re.match(r" *([0-9]+)", part).group(1))
        height_key = "DERIVED_HEIGHT" if "DERIVED_HEIGHT=" in part else "HEIGHT"
        passed = re.search(r"PASS=(true|false)", part).group(1) == "true"
        records.append(
            (
                row,
                number("BLOCK"),
                number("DEGREE"),
                number(height_key),
                number("HEIGHT_POWER"),
                number("THRESHOLD"),
                passed,
            )
        )
    return sorted(records[:82])


claimant, validator = map(parse, PATHS)
print(
    json.dumps(
        {
            "claimant_records": len(claimant),
            "validator_records": len(validator),
            "records_identical": claimant == validator,
            "claimant_passes": sum(record[-1] for record in claimant),
            "validator_passes": sum(record[-1] for record in validator),
            "failure_rows": [record[0] for record in validator if not record[-1]],
        },
        separators=(",", ":"),
    )
)

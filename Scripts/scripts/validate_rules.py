import yaml
import sys
import os

RULES_DIR = "rules"
REQUIRED_FIELDS = ["displayName", "severity", "query", "queryFrequency"]

def validate_rule(filepath):
    with open(filepath, "r") as f:
        rule = yaml.safe_load(f)

    missing = [field for field in REQUIRED_FIELDS if field not in rule]
    if missing:
        print(f"FAIL: {filepath} is missing fields: {missing}")
        return False

    print(f"PASS: {filepath} looks valid")
    return True

def main():
    all_valid = True
    for filename in os.listdir(RULES_DIR):
        if filename.endswith(".yaml"):
            filepath = os.path.join(RULES_DIR, filename)
            if not validate_rule(filepath):
                all_valid = False

    if not all_valid:
        sys.exit(1)  # non-zero exit tells GitHub Actions "this failed"

if __name__ == "__main__":
    main()
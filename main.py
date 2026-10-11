from pathlib import Path
import yaml

CONFIG_DIR = Path(__file__).parent / "config"
FAMILY_ID = "software-engineering"
ROLE_ID = "staff-swe"


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    family_dir = CONFIG_DIR / "families" / FAMILY_ID

    rubric = load_yaml(CONFIG_DIR / "rubrics" / "base.yaml")
    family = load_yaml(family_dir / "family.yaml")
    role = load_yaml(family_dir / "roles" / f"{ROLE_ID}.yaml")

    print(f"Role: {role['name']} ({family['name']})")

    for criterion in rubric["criteria"]:
        bar = role["bar"][criterion["id"]]
        print(f"\n{criterion['name']} (bar: {bar})")
        print(f"  {criterion['question']}")

    competency_names = {c["id"]: c["name"] for c in family["competencies"]}

    print("\nCompetencies to cover:")
    for competency_id in role["competencies"]:
        print(f"  - {competency_names[competency_id]}")


if __name__ == "__main__":
    main()

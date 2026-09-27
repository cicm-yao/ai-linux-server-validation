import yaml
import glob


def load_knowledge():

    knowledge = []

    files = glob.glob(
        "knowledge/*.yaml"
    )

    for file in files:

        with open(file, "r") as f:

            data = yaml.safe_load(f)

            knowledge.extend(
                data["failures"]
            )

    return knowledge


if __name__ == "__main__":

    kb = load_knowledge()

    print("Loaded failures:")

    for item in kb:

        print(
            item["id"],
            "-",
            item["root_cause"]
        )

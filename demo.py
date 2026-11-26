"""Look up an invented result in an in-memory index."""

import argparse


RESULTS = {
    "DEMO-01": {"course": "Sample Algebra", "points": 72},
    "DEMO-02": {"course": "Sample Writing", "points": 84},
    "DEMO-03": {"course": "Sample Computing", "points": 91},
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", help="For example, DEMO-01.")
    reference = parser.parse_args().reference.strip().upper()
    result = RESULTS.get(reference)
    if result is None:
        parser.error("No matching demo reference.")
    print(f"{reference} — {result['course']}: {result['points']} points")


if __name__ == "__main__":
    main()

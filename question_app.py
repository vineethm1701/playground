import csv
from collections import defaultdict


def load_questions(csv_file):
    questions_by_team = defaultdict(list)
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            question = row.get('Question') or row.get('question')
            team = row.get('Team') or row.get('team')
            if question and team:
                questions_by_team[team].append(question)
    return questions_by_team


def print_questions(questions_by_team):
    for team, questions in questions_by_team.items():
        print(f"\nTeam: {team}")
        for idx, q in enumerate(questions, start=1):
            print(f"  {idx}. {q}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Display questions by team")
    parser.add_argument('csv_file', help='Path to CSV file containing questions and team labels')
    args = parser.parse_args()

    data = load_questions(args.csv_file)
    print_questions(data)

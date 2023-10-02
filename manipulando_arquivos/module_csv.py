import csv

courses = []

with open("courses.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        courses.append({"language": row["language"], "category": row["category"]})
print(reader)
import csv
def csv_reader(original_file):
    with open(original_file, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        return [(row[0], row[1], int(row[2])) for row in reader]

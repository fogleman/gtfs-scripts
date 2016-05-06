import csv

def read(path):
    with open(path, 'rb') as fp:
        reader = csv.DictReader(fp)
        result = list(reader)
        return result, reader.fieldnames

def write(path, rows, fieldnames=None):
    fieldnames = fieldnames or sorted(rows[0].keys())
    with open(path, 'wb') as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

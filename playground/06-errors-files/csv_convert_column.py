"""Analogous demo: DictReader gives you strings. Convert ONE column, keep the rest."""
import csv
import io

data = io.StringIO("city,temp\nBangkok,34\nOslo,4\n")  # pretend this is a file

reader = csv.DictReader(data)
first = next(reader)
print("raw row:", first)  # every value is a str
print("type of temp:", type(first["temp"]))

# Option A: mutate each row in a loop
data.seek(0)
rows_a = []
for row in csv.DictReader(data):
    row["temp"] = float(row["temp"])
    rows_a.append(row)
print("A:", rows_a)

# Option B: build a new dict per row with {**row, key: new_value}
data.seek(0)
rows_b = [{**row, "temp": float(row["temp"])} for row in csv.DictReader(data)]
print("B:", rows_b)

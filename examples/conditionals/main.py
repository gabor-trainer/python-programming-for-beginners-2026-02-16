import csv

data = []

with open("c:\\_Downloads\\customer_data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        # Optional: convert numeric fields to proper types
        row["customer_id"] = int(row["customer_id"])
        row["age"] = int(row["age"])
        row["total_purchases"] = float(row["total_purchases"])

        data.append(dict(row))  # ensure pure dict

for item in data:
    item["age"] = item["age"] + 1

with open("c:\\_Downloads\\processed.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=";")
    writer.writeheader()
    writer.writerows(data)

# print(data)

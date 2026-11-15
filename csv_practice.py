# Reflection Questions:
# 1. Python allows for the process to be automated and reused for any purpose. Excel would require you to manually do so. Python makes it much easier and quicker to produce ETL pipelines.
# 2. A POS system at, for example, a store or a gas station can use such a log file. They can process and compute the data recieved from each purchase made using that specific POS system.


from datetime import datetime
import csv
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)
csv_filepath = os.path.join("data", "sales.csv")

print("--- Exercise 2 ---")
with open(csv_filepath, mode="r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print()

print("--- Exercise 3 ---")
with open(csv_filepath, mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"Header: {header}")
    print("Data Rows:")
    for row in reader:
        print(row)
print()

print("--- Exercise 4 ---")
total_revenue = 0.0

with open(csv_filepath, mode="r", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        product_name = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product_name}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total Revenue across all rows: ${total_revenue:.2f}\n")

print("--- Exercise 5 ---")
cleaned_filepath = os.path.join("data", "cleaned.csv")
original_row_count = 0
written_row_count = 0

with open(csv_filepath, mode="r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header

    with open(cleaned_filepath, mode="w", newline="") as outfile:
        writer = csv.writer(outfile)
        # Write header
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_row_count += 1
            product_name = row[0]
            price = float(row[1])
            quantity = int(row[2])
            line_total = price * quantity

            if line_total > 100.0:
                writer.writerow([product_name, f"{price:.2f}", quantity, f"{line_total:.2f}"])
                written_row_count += 1

print(f"Original rows processed: {original_row_count}")
print(f"Cleaned high-value rows written: {written_row_count}\n")

print("--- Exercise 6 ---")
dict_total_revenue = 0.0

with open(csv_filepath, mode="r", newline="") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        dict_total_revenue += price * quantity

print(f"DictReader Total Revenue: ${dict_total_revenue:.2f}")

# csv.reader is preferable for smaller files and less data to process.
# csv.DictReader is ideal for larger stores of data so that data can be accessed safely and much easier.
print()

print("--- Exercise 7 ---")
product_summary = {}

with open(csv_filepath, mode="r", newline="") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        product_name = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity

        product_summary[product_name] = product_summary.get(product_name, 0.0) + line_total

for product in sorted(product_summary.keys()):
    print(f"{product}: ${product_summary[product]:.2f}")
print()

print("--- Exercise 8 ---")
log_filepath = os.path.join("data", "run_log.txt")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_filepath, mode="a") as log_file:
    log_file.write(f"Run Timestamp: {timestamp} | Total Revenue: ${total_revenue:.2f}\n")

print(f"Appended log record to '{log_filepath}'.")
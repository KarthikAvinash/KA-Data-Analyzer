import csv

input_file = 'rules_without_stopword_minConfidence_0.0001_minSupport_0.0002.csv'
output_file = 'ramayana_roman.csv'

with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.writer(csv_output)

    # Write header with the row number column
    header = next(reader)
    header.insert(0, '#')
    writer.writerow(header)

    # Write rows with row number
    for i, row in enumerate(reader, start=1):
        row.insert(0, i)
        writer.writerow(row)

print(f"Row number column added. Output saved to {output_file}.")

import csv


input_file = 'garud_purana_without_stop_word_cleaned_support0.010_confidence0.9.csv'

output_file = 'output.csv'

with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out, quoting=csv.QUOTE_ALL)
    
    for row in reader:
        modified_row = []
        for item in row:
            tuples = item.split('),(')
            enclosed_tuples = ['"' + tuple_item + '"' for tuple_item in tuples]
            modified_row.extend(enclosed_tuples)
        writer.writerow(modified_row)

print('Conversion complete. Output written to', output_file)

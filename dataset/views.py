from django.shortcuts import render
import csv
import pandas as pd

def dataset_list(request):
    # Implement logic to fetch and pass the dataset list to the template
    datasets = ['Ramayana (Roman)', 'Ramayana (Devanagri)', 'Bhagavadgita']
    return render(request, 'dataset/list.html', {'datasets': datasets})
   
def scatter_plot(request, dataset_id, min_conf, min_support):
    # Implement logic to generate the scatter plot
    # dataset_id is the selected dataset's ID or slug
    # min_conf and min_support are the specified minimum confidence and support values
    return render(request, 'dataset/scatter_plot.html', {'dataset_id': dataset_id, 'min_conf': min_conf, 'min_support': min_support})

csv_file_path = 'static/ramayana_roman.csv'
# csv_file_path = 'static/ramayana_devanagri.csv'

def dataset_details(request, dataset_id=0):
    # Read the CSV file and parse the data
    csv_data = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)

    # Extract the confidence and support values from the CSV data
    confidences = [float(row[3]) for row in csv_data[1:]]  # Skipping the header row
    supports = [float(row[5]) for row in csv_data[1:]]

    # Create a DataFrame for the scatter plot data
    data = {
        'Confidence': confidences,
        'Support': supports
    }
    df = pd.DataFrame(data)

    # Convert the DataFrame to JSON
    scatter_data = df.to_json(orient='records')

    # Pass the parsed CSV data and scatter plot data to the template
    return render(request, 'dataset/details.html', {'csv_data': csv_data, 'scatter_data': scatter_data})

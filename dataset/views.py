from django.shortcuts import render
import csv
import pandas as pd
import os

dataset_dir = 'dataset/csv_files'


def dataset_list(request):
    # Specify the directory path where the dataset files are located

    # Define the dataset files with their respective minConfidence and minSupport values
    dataset_files = [
        # {'file':'Vedas', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Vedas' },
        # {'file':'Upanishads-1', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Upanishads-1' },
        # {'file':'Upanishads-2', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Upanishads-2' },

        {'file': 'Ramayana [Roman]', 'min_confidence': 0.0001,
            'min_support': 0.0002, 'name': 'Ramayana [Roman]'},
        {'file': 'Ramayana [Devanagari]', 'min_confidence': 0.0001,
            'min_support': 0.0003, 'name': 'Ramayana [Devanagari]'},

        # {'file':'Bhagavatgita', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Bhagavatgita' },
        # {'file':'Vedanta Sutras Part I', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Vedanta Sutras Part I' },
        # {'file':'Vedanta Sutras Part II', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Vedanta Sutras Part II' },
        # {'file':'Vedanta Sutras', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Vedanta Sutras' },
        # {'file':'Brahma Knowledge(Vedantas)', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Brahma Knowledge(Vedantas)' },
        # {'file':'Crew jewel of wisdom (Vedantas)', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Crew jewel of wisdom (Vedantas)' },
        # {'file':'vishnu purana', 'min_confidence':0.001, 'min_support':0.002, 'name': 'vishnu purana' },

        {'file': 'Anugita', 'min_confidence': 0.02,
            'min_support': 0.02, 'name': 'Anugita'},
        {'file': 'Bhagavadgita', 'min_confidence': 0.03,
            'min_support': 0.03, 'name': 'Bhagavadgita'},
        {'file': 'Bhagavadgita poetic', 'min_confidence': 0.05,
            'min_support': 0.05, 'name': 'Bhagavadgita poetic'},
        {'file': 'Sanatsugatiya', 'min_confidence': 0.03,
            'min_support': 0.03, 'name': 'Sanatsugatiya'},
        {'file': 'Srimad Bhagavadgita', 'min_confidence': 0.003,
            'min_support': 0.003, 'name': 'Srimad Bhagavadgita'},
        {'file': 'Bhagavadgita translated by edwin arnold', 'min_confidence': 0.05,
            'min_support': 0.05, 'name': 'Bhagavadgita translated by edwin arnold'},
        {'file': 'Bhagavdgita asitis', 'min_confidence': 0.002,
            'min_support': 0.002, 'name': 'Bhagavdgita asitis'},
        {'file': 'Devi gita', 'min_confidence': 0.15,
            'min_support': 0.15, 'name': 'Devi gita'},
        {'file': 'Premsagar', 'min_confidence': 0.1,
            'min_support': 0.1, 'name': 'Premsagar'},
        {'file': 'Transmigration of seven bhramas', 'min_confidence': 0.19,
            'min_support': 0.19, 'name': 'Transmigration of seven bhramas'},
        {'file': 'VedicHymn', 'min_confidence': 0.05,
            'min_support': 0.05, 'name': 'VedicHymn'},

        # {'file':'Garud purana', 'min_confidence':0.001, 'min_support':0.002, 'name': 'Garud purana' },
        # Add more datasets and their values as needed
    ]

    # Pass the dataset file list to the template
    return render(request, 'dataset/list.html', {'dataset_files': dataset_files})


def dataset_details(request, dataset_id=0):
    # Specify the available dataset file paths and their respective names
    dataset_files = [
        {'file':  os.path.join(
            dataset_dir, 'ramayana_roman.csv'), 'name': 'Ramayana [Roman]'},
        {'file': os.path.join(dataset_dir, 'ramayana_devanagri.csv'),
         'name': 'Ramayana [Devanagari]'},
        {'file': os.path.join(
            dataset_dir, 'anugita-withoutstopwords-0.02.csv'), 'name': 'Ramayana [Roman]'},
        {'file': os.path.join(
            dataset_dir, 'bhagavadgita_without_stopwords-0.03.csv'), 'name': 'Ramayana [Devanagari]'},
        {'file': os.path.join(
            dataset_dir, 'Bagvadgitapoetic-withoutstopwords-0.05.csv'), 'name': 'Ramayana [Roman]'},
        {'file': os.path.join(
            dataset_dir, 'sanatsugatiya_without_stopwords-0.03.csv'), 'name': 'Ramayana [Devanagari]'},
        {'file': os.path.join(
            dataset_dir, 'srimad-bhagavadgita_without_stopwords-0.003.csv'), 'name': 'Ramayana [Roman]'},
        {'file': os.path.join(
            dataset_dir, 'srimad-bhagavadgita_without_stopwords-0.003.csv'), 'name': 'Ramayana [Devanagari]'},
        {'file': os.path.join(
            dataset_dir, 'Bhagavadgita_asitis_without_stopwords-0.002.csv'), 'name': 'Ramayana [Roman]'},
        {'file': os.path.join(
            dataset_dir, 'devigita_without_stopwords_0.15.csv'), 'name': 'Ramayana [Devanagari]'},
        {'file': os.path.join(
            dataset_dir, 'Premsagar-withoutStopwords-0.1.csv'), 'name': 'Ramayana [Roman]'},
        {'file': os.path.join(
            dataset_dir, 'Transmigration-withoutstopwords-0.19.csv'), 'name': 'Ramayana [Devanagari]'},
        {'file': os.path.join(
            dataset_dir, 'Vedichymn_without_stopwords-0.05.csv'), 'name': 'Ramayana [Roman]'},
    ]

    # Get the selected dataset file path and name based on the provided dataset ID
    dataset = dataset_files[int(dataset_id)]
    csv_file_path = dataset['file']
    dataset_name = dataset['name']

    # Read the CSV file and parse the data
    # Read the CSV file and parse the data
    csv_data = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)

    # Extract the confidence and support values from the CSV data
    confidences = [float(row[3])
                   for row in csv_data[1:]]  # Skipping the header row
    supports = [float(row[5]) for row in csv_data[1:]]

    # Create a DataFrame for the scatter plot data
    data = {
        'Confidence': confidences,
        'Support': supports
    }
    df = pd.DataFrame(data)

    # Convert the DataFrame to JSON
    scatter_data = df.to_json(orient='records')

    # Pass the dataset name to the template
    return render(request, 'dataset/details.html', {'csv_data': csv_data, 'scatter_data': scatter_data, 'dataset_name': dataset_name})

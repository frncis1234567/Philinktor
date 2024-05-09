import csv
import json
import pandas as pd
import time

def create_sorted_arr_and_dict():
    try:
        start = time.time()
        domain_data_array = []
        domain_data_dict = {}

        # Process the CSV file
        with open('static/data/top-1m.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                domain = row[1]  # Assuming the domain is in the second column
                rank = row[0]    # Assuming the rank is in the first column
                domain_data_array.append(domain)
                domain_data_dict[domain] = rank

        # Process the XLSX file
        df = pd.read_excel('static/data/data_imbal-55000.xlsx', engine='openpyxl')
        for index, row in df.iterrows():
            domain = row[0]  # Adjust if the domain is in a different column in your XLSX
            if domain not in domain_data_dict:
                rank = str(len(domain_data_dict) + 1)  # Generate a new rank
                domain_data_array.append(domain)
                domain_data_dict[domain] = rank

        # Sort the list by domain name
        sorted_domain_data = sorted(domain_data_array)

        # Save the sorted data to a new file
        with open('static/data/sorted-domains-combined.txt', 'w') as outfile:
            for domain in sorted_domain_data:
                outfile.write(domain + '\n')

        # Write the dictionary to a JSON file
        with open('static/data/domain-rank-combined.json', 'w') as outfile:
            json.dump(domain_data_dict, outfile)

        end = time.time()

        print('Script Executed Successfully.')
        print('Execution Time:', round(end - start, 2), 'seconds')

    except Exception as e:
        print(f"Error: {e}")

create_sorted_arr_and_dict()

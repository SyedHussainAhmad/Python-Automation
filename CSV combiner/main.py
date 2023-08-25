import os
import pandas as pd

# Directory containing your CSV files
directory_path = 'D:\F Drive\Work\Programming\Python\Coding\Web Scraping\CSV combiner\Files'

# List to store all dataframes
all_dataframes = []

# Loop through all CSV files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)
        all_dataframes.append(df)

# Combine all dataframes into one
merged_df = pd.concat(all_dataframes, ignore_index=True)

# Path to the output CSV file
output_csv_path = 'data.csv'

# Save the merged dataframe to a new CSV file
merged_df.to_csv(output_csv_path, index=False)

print(f"Merged {len(all_dataframes)} CSV files into {output_csv_path}")

import csv

# Define the path to your input CSV file and output CSV file
input_csv_file = "flatprice5.csv"
output_csv_file = "flatprice5_last3year.csv"

# Define the range of months you want to filter
start_month = "2021-06"
end_month = "2024-05"

# Open the input CSV file in read mode and the output CSV file in write mode
with open(input_csv_file, mode='r', newline='') as input_file, \
     open(output_csv_file, mode='w', newline='') as output_file:

    # Create a CSV reader object for the input file
    csv_reader = csv.reader(input_file)
    
    # Create a CSV writer object for the output file
    csv_writer = csv.writer(output_file)
    
    # Write the header row to the output file
    header = next(csv_reader)
    csv_writer.writerow(header)
    
    # Iterate over each row in the input CSV file
    for row in csv_reader:
        # Extract the month from the row
        row_month = row[0]
        # Check if the row's month is within the specified range
        if start_month <= row_month <= end_month:
            # Write the row to the output CSV file
            csv_writer.writerow(row)
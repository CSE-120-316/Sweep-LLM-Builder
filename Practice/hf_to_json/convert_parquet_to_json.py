import pandas as pd

# Step 1: Read Parquet File
parquet_file_path = 'example.parquet'  # Replace with the path to your Parquet file
df = pd.read_parquet(parquet_file_path)

# Step 2: Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Step 3: Save JSON to File
json_file_path = 'finish/output.json'  # Path to save the JSON file in the 'finish' folder
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON file saved: {json_file_path}")

# Step 4: Create HTML Index File
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parquet to JSON Converter</title>
</head>
<body>
    <h1>Parquet to JSON Converter</h1>
    <p>JSON file has been created successfully!</p>
    <a href="{json_file_path}">Download JSON File</a>
</body>
</html>
""".format(json_file_path=json_file_path)

html_file_path = 'finish/index.html'  # Path to save the HTML index file
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

print(f"HTML index file saved: {html_file_path}")

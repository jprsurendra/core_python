import json

# Sample input data
data = {
    'rates[0][field1]': ['value01'],
    'rates[0][field2]': ['value02'],
    'rates[1][field1]': ['value11'],
    'rates[1][field2]': ['value12'],
    'rates[n][field1]': ['valuen1'],
    'rates[n][field2]': ['valuen2']
}

# Initialize the list to hold the rates
rates = []

# Populate the rates list
for key, value in data.items():
    # Parse the key to get the index and field name
    parts = key.split('][')
    index = int(parts[0].split('[')[1])
    field = parts[1][:-1]

    # Ensure the rates list is large enough
    while len(rates) <= index:
        rates.append({})

    # Assign the value to the appropriate field
    rates[index][field] = value[0]  # Assuming value is a list with one item

# Convert to JSON
json_output = json.dumps({'rates': rates}, indent=4)

# Print the JSON output
print(json_output)

import pandas as pd

# Load the lookup table into a DataFrame
df = pd.read_excel("MDDC_FileLayout.xlsx")

# Get the field name from the user
field_name = input("Enter field name: ")

# Find the field in the lookup table
field = df.loc[df['FIELD NAME'] == field_name]
print(field)
# Check if the field was found
if len(field) == 0:
    print("Field not found.")
else:
    # Get the start and end positions of the field in the text file
    start_pos = field.iloc[0]['FROM'] - 1
    end_pos = field.iloc[0]['TO']

    # Read the text file
    with open("MDDC20230126.txt", "r") as f:
        text = f.read()

    # Print the content of the field
    field_content = text[start_pos:end_pos].strip()
    print(field_content)

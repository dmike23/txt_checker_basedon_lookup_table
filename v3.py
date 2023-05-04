import pandas as pd

# Load the lookup table into a DataFrame
df = pd.read_excel("MDDC_FileLayout.xlsx")

for index, row in df.iterrows():
    # Find the start and end positions for this field in the text file
    start_pos = row['FROM'] - 1
    end_pos = row['TO']

    # Read the text file
    with open("MDDC20230126.txt", "r") as f:
        text = f.read()

    # Extract the content of the field for this row
    field_content = text[start_pos:end_pos].strip()

    # Print the field content (or do whatever else you need to do with it)
    print(f"Field {row['FIELD NAME']}: {field_content}")
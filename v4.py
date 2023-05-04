import pandas as pd

# Load the lookup table into a DataFrame
df = pd.read_excel("MDDC_FileLayout.xlsx")

# Get the field name from the user
field_name = input("Enter field name: ")

# Find the field in the lookup table
field = df.loc[df['FIELD NAME'] == field_name]

# Check if the field was found
if len(field) == 0:
    print("Field not found.")
else:
    # Get the column number for the field in the text file
    col_num = field.iloc[0]['COLUMN']

    # Read the text file into a DataFrame
    df_text = pd.read_csv("MDDC20230126.txt", sep='|', header=None)

    # Extract the content of the column
    column_content = df_text.iloc[:, col_num].str.strip()

    # Print the content of the column
    print(column_content)

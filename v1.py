import pandas as pd

# Load lookup table from Excel file
df = pd.read_excel("MDDC_FileLayout.xlsx")

# Specify the field name to look up
field_name = "CASE-TYPE"

# Find the FROM and TO positions for the specified field
from_pos = df.loc[df["FIELD NAME"] == field_name, "FROM"].iloc[0] - 1
to_pos = df.loc[df["FIELD NAME"] == field_name, "TO"].iloc[0]

# Read the text file and print the content for the specified field
with open("MDDC20230126.txt") as f:
    content = f.read()
    field_content = content[from_pos:to_pos]
    print(field_content)

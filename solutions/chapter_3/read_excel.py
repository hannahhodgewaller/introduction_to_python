# Load in the police data

police = pd.read_excel("../data/police_data.xlsx", sheet_name=1)

police.head()

# The paramater sheet_name = 1 imports the second sheet
# sheet_name = "Table P1" will also work
# Note if you're using an older version of Pandas ( < 0.21.0 ) the parameter is sheetname = with no space. 

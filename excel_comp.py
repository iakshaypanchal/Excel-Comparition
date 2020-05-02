import os
import pandas as pd

# path of the files
file_A = "File_A.xlsx"
file_B = "File_B.xlsx"

#read the excel files
xl1 = pd.read_excel(file_A)
xl2 = pd.read_excel(file_B)

#the needed rows will be stored here
out_rows =[]

#sort the excel files for efficient parsing
xl1 = xl1.sort_values(['PubID'], ascending= 'True')
xl2 = xl2.sort_values(['PubID'], ascending='True')

#check if the row exists in the compare file
def row_exists(row, xl1):
    for index1, row1 in xl1.iterrows():
        if row[3] == row1[3]:
            return True
    return False



for index2, row2 in xl2.iterrows():
    if  row_exists(row2, xl1):
        out_rows.append(row2)

#copy the list into a pandas dataframe

data_frame = pd.DataFrame(out_rows, columns=['PubID', 'Name', 'SurName', 'Contact No'])

#output the rows into OUTPUT.xlsx
writer = pd.ExcelWriter('OUTPUT.xlsx', engine='xlsxwriter')
data_frame.to_excel(writer, 'Sheet1')
writer.save()
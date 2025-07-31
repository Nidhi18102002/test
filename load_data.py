import pandas as pd
import mysql.connector
import csv

# df=pd.read_csv(r'C:\Users\siddh\OneDrive\Desktop\test\__MACOSX\archive\._products.csv',encoding='utf-8',encoding_errors='ignore')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='ecommerce2'
)

cursor = conn.cursor()
with open(r'C:\Users\siddh\OneDrive\Desktop\test\__MACOSX\archive\._products.csv', 'r', newline ='', encoding='utf-8', errors='ignore') as csvfile:
    cleaned_file = (line.replace('\00', '') for line in csvfile)
    reader = csv.reader(cleaned_file)
    header = next(reader)
    insert_query = f"INSERT INTO products2({', '.join(header)}) VALUES ({', '.join(['%s'] * len(header))})"
    row_count = 0
    for row in reader:
        if len(row) == len(header):
            cursor.execute(insert_query, row)
            row_count += 1
conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully")
                   

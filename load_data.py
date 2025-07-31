import pandas as pd
import mysql.connector

df=pd.read_csv(r'C:\Users\siddh\OneDrive\Desktop\test\__MACOSX\archive\._products.csv',encoding='utf-8',encoding_errors='ignore')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database='ecommerce'
)

cursor = conn.cursor()
for _, row in df.iterrows():
    cursor.execute("INSERT INTO products (product_id, product_name, price, category)"  "VALUES (%s, %s, %s, %s)",
                   (row['product_id'], row['product_name'], row['price'], row['category']))
conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully")
                   

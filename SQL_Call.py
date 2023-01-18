import pandas as pd
import sqlite3
import json

# Ingest Receipts 
# Open JSON data
data = [json.loads(line)
        for line in open("receipts.json", 'r', encoding='utf-8')]

# Create A DataFrame From the JSON Data
df_receipts = pd.DataFrame(data)

df_receipts['_id'] = df_receipts['_id'].apply(lambda item: str(list(item.values())))
df_receipts['_id'] = df_receipts['_id'].apply(lambda item: item.replace('[','').replace(']',''))
df_receipts.userId = df_receipts.userId.apply(lambda item: str(item))

# Subset the datframe because the dates are not formatted for SQL 
df_sub = df_receipts.loc[:,('rewardsReceiptStatus', 'purchasedItemCount', 'totalSpent')]

# Use the connect() function to create a database in our environment
conn = sqlite3.connect("receipts.db")

# Use the cursor() function to assist with executing our SQL queries
c = conn.cursor()

# Write our subsetted DataFrame to a SQL database.
df_sub.to_sql("df_sub",conn)

# Our Query which gets the average totalSpent and max purchasedItemCount by rewardsReceiptStatus
# An important note is that rewardsReceiptStatus is missing any ACCEPTED rows
query = """SELECT rewardsReceiptStatus, MAX(purchasedItemCount) AS max_items, AVG(totalSpent) AS avg_spend
            FROM(
                SELECT *
                FROM df_sub
                WHERE rewardsReceiptStatus = "ACCEPTED"
                OR rewardsReceiptStatus = "REJECTED"
                )
            GROUP BY rewardsReceiptStatus
            ORDER BY rewardsReceiptStatus;
           """
        
# Use pandas to read the query from our SQL database
pd.read_sql_query(query,conn)

# Close our connection
conn.close()

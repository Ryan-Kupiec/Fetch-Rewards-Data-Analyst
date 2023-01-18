import pandas as pd
import json
import gzip
import shutil

# This is to open and save the gz files as json files 
# with gzip.open('brands.json.gz', 'rb') as f_in:
#     with open('brands.json', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# Ingest Receipts JSON data 
data = [json.loads(line)
        for line in open("receipts.json", 'r', encoding='utf-8')]

# Create A DataFrame From the JSON Data
df_receipts = pd.DataFrame(data)

# The _id columns came in as dictionaries so these turn them into strings so 
# they are more readable
df_receipts['_id'] = df_receipts['_id'].apply(lambda item: str(list(item.values())))
df_receipts['_id'] = df_receipts['_id'].apply(lambda item: item.replace('[','').replace(']',''))

# Ingest Users
data = [json.loads(line)
        for line in open("users.json", 'r', encoding='utf-8')]

# Create A DataFrame From the JSON Data
df_users = pd.DataFrame(data)

# The _id columns came in as dictionaries so these turn them into strings so 
# they are more readable
df_users['_id'] = df_users['_id'].apply(lambda item: str(list(item.values())))
df_users['_id'] = df_users['_id'].apply(lambda item: item.replace('[','').replace(']',''))

# Ingest Brands
data = [json.loads(line)
        for line in open("brands.json", 'r', encoding='utf-8')]

# Create a DataFrame from the JSON Data
df_brands = pd.DataFrame(data)

# The _id columns came in as dictionaries so these turn them into strings so 
# they are more readable
df_brands['_id'] = df_brands['_id'].apply(lambda item: str(list(item.values())))
df_brands['_id'] = df_brands['_id'].apply(lambda item: item.replace('[','').replace(']',''))

# The rows evaluate how many NAs are in each of the columns 
100*(df_receipts.isnull().sum()/len(df_receipts))
100*(df_brands.isnull().sum()/len(df_receipts))
100*(df_users.isnull().sum()/len(df_receipts))

# Describe the 3 dfs to evaluate the data  
df_receipts.describe(include = [object])
df_brands.describe(include = [object])
df_users.describe(include = [object])







    






# Fetch-Rewards-Data-Analyst

## First Task: Diagram a New Structured Relational Data Model
I have pushed my results as an image file to the repository. 

## Second Task: SQL query to answer a business stakeholder question
I decided to answer the average spend and the total number of items purchased questions with my query. I used the sqlite3 package in python to test my query. The script I have attached pulls in the receipts dataframe and creates an SQL database that we use with our query to answer the two questions. The query that I wrote is:

```
SELECT rewardsReceiptStatus, MAX(purchasedItemCount) AS max_items, AVG(totalSpent) AS avg_spend
FROM(
     SELECT *
     FROM df_sub
     WHERE rewardsReceiptStatus = "ACCEPTED"
     OR rewardsReceiptStatus = "REJECTED"
     )
GROUP BY rewardsReceiptStatus
ORDER BY rewardsReceiptStatus;
```

## Third Task: Data quality issues 
The first steps I take whenever I am evaluating a data set is to look at the dataset as a whole once we load the data in, look at the number of NA values for each of the columns, and use the describe function to evaluate the columns in the dataset. In the quick evaluation of this dataset there were a few issues that surfaced. First issue, was that some of the columns came in as dictionaries. The second issue was that the _id column in the users dataset only had 212 unique values even though there were 495 values. This means that some of the id values are being reused when they should be unique. 




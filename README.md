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





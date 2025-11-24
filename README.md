# Credit Card Spending Analyzer 

## Overview 



This project is a Python program that analyzes credit card spending data stored in a CSV file.

 It goes through each transaction, organizes expenses by category, calculates the total amount spent, and figures out the minimum payment due, which is 3% of the total.



## Features 



- Reads transaction data from a CSV file 

- Groups spending by category 

- Calculates total spending 

- Computes the minimum payment (3% of total) 

- Displays a formatted summary report in the terminal 

- Handles common issues like missing files, missing columns, or invalid data 



## CSV Format 



The program expects a CSV file with these lowercase column names: 



- date 

- category 

- amount 

- description 



Example: 



date,category,amount,description

11-11-2025,food,850,dominos

12-11-2025,shopping,3500,zara

13-11-2025,travel,250,uber

14-11-2025,bills,2000,electricity





## Requirements 



- Python 3.x 



### Uses only built-in modules: 



- csv 

- datetime 

- collections 



## How to Run 



Place the Python script and the CSV file in the same folder.





Open a terminal in that folder.





Run the command: 



bash

python card_spending.py

 



The spending summary will be shown in the terminal.





## How It Works 



- The program reads each transaction from the CSV file using csv.DictReader 

- It adds up the amounts for each category using defaultdict(float) 

- It totals the spending and determines the minimum payment 

- It sorts and displays the category spending from highest to lowest 

- It returns key results for possible further use 



## Error Handling 



The program manages the following: 



- Missing or incorrect file paths 

- Missing required columns 

- Invalid numeric values in the amount field 



## Future Improvements 



- Filtering by month 

- Calculating interest 

- Exporting reports to text, CSV, or PDF 

- Visualizing spending trends with graphs 



## Maintained by 

*Moksh Berawala*

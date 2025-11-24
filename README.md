# Credit Card Spending Analyzer
## Overview

This project is a Python program designed to analyze credit card spending data stored in a CSV file. It processes each transaction, groups expenses by category, calculates total spending, and determines the minimum payment due based on 3 percent of the total amount.

## Features

Reads transaction data from a CSV file

Groups spending by category

Calculates total spending

Computes minimum payment (3 percent of total)

Displays a formatted summary report in the terminal

Handles common errors such as missing files, missing columns, or invalid data

## CSV Format

The program expects a CSV file with the following lowercase column names:

date

category

amount

description

```bash
date,category,amount,description
11-11-2025,food,850,dominos
12-11-2025,shopping,3500,zara
13-11-2025,travel,250,uber
14-11-2025,bills,2000,electricity
```

## Requirements

Python 3.x

### Uses only built-in modules:

csv

datetime

collections

## How to Run

Place the Python script and the CSV file in the same directory.

Open a terminal in that directory.

Run the command:

```bash
python card_spending.py
```
The spending summary will be printed in the terminal.

## How It Works

Reads each transaction from the CSV file using csv.DictReader

Sums amounts per category using defaultdict(float)

Calculates total spending and minimum payment

Sorts and displays category spending from highest to lowest

Returns key results for potential further use

## Error Handling

### The program handles:

Missing or incorrect file paths

Missing required columns

Invalid numeric values in the amount field

## Future Improvements

Monthly filtering

Interest calculation

Exporting reports to text, CSV, or PDF

Graphical visualization of spending trends

## Maintaned by
**Moksh Berawala** 

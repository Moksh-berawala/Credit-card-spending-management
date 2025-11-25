
# Credit Card Spending Analyzer

This Python project allows users to analyze and manage their credit card spending using a CSV file as storage.
It provides features such as spending breakdown by category, minimum payment calculation, and full transaction CRUD operations.

---

## Features

- Analyze spending by category  
- Calculate total spending  
- Calculate minimum due amount (3%)  
- View all transactions  
- Add new transactions  
- Edit existing transactions  
- Delete transactions  
- CLI-based menu navigation  

---

## Project Structure

```
main.py                → Contains the entire program logic  
transactions.csv       → Auto-created file storing transactions  
 
```

---

## How It Works

### **1. Input CSV Format**

The application expects the CSV file to contain the following columns:

```
date, category, amount, description
```

---

## Modules Used

- csv → Read/write CSV files  
- datetime → Date validation and timestamps  
- collections.defaultdict → Efficient category grouping  
- os → File existence checks  

---

## Running the Program

Run the script using:

```
python main.py
```

On first run, it will automatically create `transactions.csv` if it does not exist.

---

## Application Menu

```
1. Analyze spending
2. Manage transactions
3. Exit
```

**Manage Transactions Submenu:**

```
1. View all transactions
2. Add new transaction
3. Edit transaction
4. Delete transaction
5. Return to main menu
```

---

## Error Handling

The program gracefully handles:

- Missing CSV file  
- Invalid or missing columns  
- Wrong number formats  
- Invalid date formats  
- Empty or corrupted CSV  
- Invalid user menu inputs  

---

## Future Enhancements

- Add GUI (Tkinter/PyQt)  
- Switch from CSV to SQLite/PostgreSQL  
- Add graphical charts for spending visualization  
- Export reports to PDF/Excel  
- User authentication system  

---

## Maintaned and managed by
* Moksh Berawala

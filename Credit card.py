import csv
from datetime import datetime
from collections import defaultdict
import os

def analyze_credit_card_spending(csv_file):
    """
    Analyze credit card spending from a CSV file.
    CSV format: date, category, amount, description
    """
    
    category_totals = defaultdict(float)
    total_spending = 0.0
    transactions = []
    
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                category = row['category'].strip()
                amount = float(row['amount'])
                
                category_totals[category] += amount
                total_spending += amount
                
                transactions.append({
                    'date': row['date'],
                    'category': category,
                    'amount': amount,
                    'description': row.get('description', 'N/A')
                })
        
        min_payment_percentage = 0.03
        minimum_payment = total_spending * min_payment_percentage
        
        print("=" * 60)
        print("CREDIT CARD SPENDING ANALYSIS")
        print("=" * 60)
        print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Total Transactions: {len(transactions)}")
        
        print("\n" + "-" * 60)
        print("SPENDING BY CATEGORY")
        print("-" * 60)
        
        sorted_categories = sorted(
            category_totals.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        for category, amount in sorted_categories:
            percentage = (amount / total_spending) * 100 if total_spending > 0 else 0
            print(f"{category:.<30} ₹{amount:>10.2f} ({percentage:>5.1f}%)")
        
        print("-" * 60)
        print(f"{'TOTAL SPENDING':.<30} ₹{total_spending:>10.2f}")
        print("=" * 60)
        
        print(f"\nMINIMUM PAYMENT DUE (3%): ₹{minimum_payment:.2f}")
        print(f"FULL BALANCE: ₹{total_spending:.2f}")
        print("\n" + "=" * 60)
        
        return {
            'total_spending': total_spending,
            'minimum_payment': minimum_payment,
            'category_totals': dict(category_totals),
            'transactions': transactions
        }
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    except KeyError as e:
        print(f"Error: Missing required column {e} in CSV file.")
        print("Expected columns: date, category, amount, description")
        return None
    except ValueError as e:
        print(f"Error: Invalid data format - {e}")
        return None


def view_transactions(csv_file):
    """Display all transactions from the CSV file."""
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            transactions = list(csv_reader)
            
        if not transactions:
            print("\nNo transactions found in the file.")
            return
        
        print("\n" + "=" * 80)
        print("ALL TRANSACTIONS")
        print("=" * 80)
        print(f"{'#':<4} {'Date':<12} {'Category':<20} {'Amount':<12} {'Description'}")
        print("-" * 80)
        
        for idx, txn in enumerate(transactions, 1):
            print(f"{idx:<4} {txn['date']:<12} {txn['category']:<20} "
                  f"₹{float(txn['amount']):<11.2f} {txn.get('description', 'N/A')}")
        
        print("=" * 80)
        
    except FileNotFoundError:
        print(f"\nError: File '{csv_file}' not found.")
    except Exception as e:
        print(f"\nError reading file: {e}")


def add_transaction(csv_file):
    """Add a new transaction to the CSV file."""
    print("\n" + "=" * 60)
    print("ADD NEW TRANSACTION")
    print("=" * 60)
    
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category: ").strip()
        amount = input("Enter amount: ").strip()
        description = input("Enter description: ").strip()
        
        # Validate amount
        try:
            float(amount)
        except ValueError:
            print("\nError: Amount must be a valid number.")
            return
        
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("\nError: Date must be in YYYY-MM-DD format.")
            return
        
        # Append to CSV
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        
        print("\n✓ Transaction added successfully!")
        
    except Exception as e:
        print(f"\nError adding transaction: {e}")


def delete_transaction(csv_file):
    """Delete a transaction from the CSV file."""
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            transactions = list(csv_reader)
            fieldnames = csv_reader.fieldnames
        
        if not transactions:
            print("\nNo transactions to delete.")
            return
        
        # Display transactions
        print("\n" + "=" * 80)
        print("SELECT TRANSACTION TO DELETE")
        print("=" * 80)
        print(f"{'#':<4} {'Date':<12} {'Category':<20} {'Amount':<12} {'Description'}")
        print("-" * 80)
        
        for idx, txn in enumerate(transactions, 1):
            print(f"{idx:<4} {txn['date']:<12} {txn['category']:<20} "
                  f"₹{float(txn['amount']):<11.2f} {txn.get('description', 'N/A')}")
        
        print("=" * 80)
        
        # Get transaction number to delete
        choice = input("\nEnter transaction number to delete (0 to cancel): ").strip()
        
        try:
            idx = int(choice)
            if idx == 0:
                print("Delete cancelled.")
                return
            if idx < 1 or idx > len(transactions):
                print("\nError: Invalid transaction number.")
                return
            
            # Remove transaction
            deleted_txn = transactions.pop(idx - 1)
            
            # Write back to file
            with open(csv_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(transactions)
            
            print(f"\n✓ Transaction deleted successfully!")
            print(f"  Deleted: {deleted_txn['date']} - {deleted_txn['category']} - ₹{deleted_txn['amount']}")
            
        except ValueError:
            print("\nError: Please enter a valid number.")
        
    except FileNotFoundError:
        print(f"\nError: File '{csv_file}' not found.")
    except Exception as e:
        print(f"\nError deleting transaction: {e}")


def edit_transaction(csv_file):
    """Edit an existing transaction in the CSV file."""
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            transactions = list(csv_reader)
            fieldnames = csv_reader.fieldnames
        
        if not transactions:
            print("\nNo transactions to edit.")
            return
        
        # Display transactions
        print("\n" + "=" * 80)
        print("SELECT TRANSACTION TO EDIT")
        print("=" * 80)
        print(f"{'#':<4} {'Date':<12} {'Category':<20} {'Amount':<12} {'Description'}")
        print("-" * 80)
        
        for idx, txn in enumerate(transactions, 1):
            print(f"{idx:<4} {txn['date']:<12} {txn['category']:<20} "
                  f"₹{float(txn['amount']):<11.2f} {txn.get('description', 'N/A')}")
        
        print("=" * 80)
        
        # Get transaction number to edit
        choice = input("\nEnter transaction number to edit (0 to cancel): ").strip()
        
        try:
            idx = int(choice)
            if idx == 0:
                print("Edit cancelled.")
                return
            if idx < 1 or idx > len(transactions):
                print("\nError: Invalid transaction number.")
                return
            
            txn = transactions[idx - 1]
            
            print("\n" + "=" * 60)
            print("EDIT TRANSACTION")
            print("=" * 60)
            print("Press Enter to keep current value")
            
            new_date = input(f"Date [{txn['date']}]: ").strip() or txn['date']
            new_category = input(f"Category [{txn['category']}]: ").strip() or txn['category']
            new_amount = input(f"Amount [{txn['amount']}]: ").strip() or txn['amount']
            new_description = input(f"Description [{txn.get('description', 'N/A')}]: ").strip() or txn.get('description', 'N/A')
            
            # Validate new values
            try:
                float(new_amount)
            except ValueError:
                print("\nError: Amount must be a valid number.")
                return
            
            try:
                datetime.strptime(new_date, '%Y-%m-%d')
            except ValueError:
                print("\nError: Date must be in YYYY-MM-DD format.")
                return
            
            # Update transaction
            transactions[idx - 1] = {
                'date': new_date,
                'category': new_category,
                'amount': new_amount,
                'description': new_description
            }
            
            # Write back to file
            with open(csv_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(transactions)
            
            print("\n✓ Transaction updated successfully!")
            
        except ValueError:
            print("\nError: Please enter a valid number.")
        
    except FileNotFoundError:
        print(f"\nError: File '{csv_file}' not found.")
    except Exception as e:
        print(f"\nError editing transaction: {e}")


def csv_editor_menu(csv_file):
    """Submenu for CSV editing operations."""
    while True:
        print("\n" + "=" * 60)
        print("CSV EDITOR MENU")
        print("=" * 60)
        print("1. View all transactions")
        print("2. Add new transaction")
        print("3. Edit transaction")
        print("4. Delete transaction")
        print("5. Return to main menu")
        print("=" * 60)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            view_transactions(csv_file)
        elif choice == '2':
            add_transaction(csv_file)
        elif choice == '3':
            edit_transaction(csv_file)
        elif choice == '4':
            delete_transaction(csv_file)
        elif choice == '5':
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")


def main_menu():
    """Main menu for the credit card analyzer application."""
    csv_filename = "transactions.csv"
    
    # Check if file exists, if not create it with headers
    if not os.path.exists(csv_filename):
        print(f"\nCreating new file: {csv_filename}")
        with open(csv_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'category', 'amount', 'description'])
        print("File created with headers: date, category, amount, description")
    
    while True:
        print("\n" + "=" * 60)
        print("CREDIT CARD SPENDING ANALYZER")
        print("=" * 60)
        print("1. Analyze spending")
        print("2. Manage transactions (Edit CSV)")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            print()
            analyze_credit_card_spending(csv_filename)
            input("\nPress Enter to continue...")
        elif choice == '2':
            csv_editor_menu(csv_filename)
        elif choice == '3':
            print("\nThank you for using Credit Card Spending Analyzer!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("WELCOME TO CREDIT CARD SPENDING ANALYZER")
    print("=" * 60)
    print("\nThis tool helps you:")
    print("• Analyze your credit card spending by category")
    print("• Calculate minimum payments and total balance")
    print("• Manage your transaction records")
    print("=" * 60)
    
    main_menu()
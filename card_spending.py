import csv
from datetime import datetime
from collections import defaultdict

def analyze_credit_card_spending(csv_file):
    """
    Analyze credit card spending from a CSV file.
    Your CSV format: date, category, amount, description
    """
    
    # Initialize variables
    category_totals = defaultdict(float)
    total_spending = 0.0
    transactions = []
    
    try:
        # Read the CSV file
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            
            # Print columns once (optional debug)
            # print("Columns detected:", csv_reader.fieldnames)
            
            for row in csv_reader:
                # Use lowercase keys to match your file
                category = row['category'].strip()
                amount = float(row['amount'])
                
                # Add to category total
                category_totals[category] += amount
                total_spending += amount
                
                # Store transaction
                transactions.append({
                    'date': row['date'],
                    'category': category,
                    'amount': amount,
                    'description': row.get('description', 'N/A')
                })
        
        # Calculate minimum payment (3% of total)
        min_payment_percentage = 0.03
        minimum_payment = total_spending * min_payment_percentage
        
        # Display results
        print("=" * 60)
        print("CREDIT CARD SPENDING ANALYSIS")
        print("=" * 60)
        print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Total Transactions: {len(transactions)}")
        
        print("\n" + "-" * 60)
        print("SPENDING BY CATEGORY")
        print("-" * 60)
        
        # Sort categories by spending amount (descending)
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

# Example usage
if __name__ == "__main__":
    csv_filename = "transactions.csv"
    
    print("\nCredit Card Spending Analyzer")
    print("Make sure your CSV has columns: date, category, amount, description\n")
    
    results = analyze_credit_card_spending(csv_filename)
    


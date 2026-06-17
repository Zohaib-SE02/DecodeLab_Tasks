"""
Expense Tracker
Demonstrates: Math operations & Accumulators
"""

total = 0
expenses = []

print("=" * 40)
print("         EXPENSE TRACKER")
print("=" * 40)
print("\nEnter your expenses one by one.")
print("Enter 'done' when finished.\n")

while True:
    user_input = input("Enter expense amount (or 'done' to finish): $")
    
    if user_input.lower() == 'done':
        break
    
    try:
        expense = float(user_input)
        
        # Validate positive amount
        if expense < 0:
            print("⚠️  Please enter a positive amount.\n")
            continue
        
        # Accumulator pattern: total = total + new_expense
        total = total + expense
        expenses.append(expense)
        print(f"✓ Added ${expense:.2f} | Running total: ${total:.2f}\n")
    
    except ValueError:
        print("⚠️  Invalid input. Please enter a number.\n")

# Display results
print("\n" + "=" * 40)
print("         EXPENSE SUMMARY")
print("=" * 40)

if expenses:
    print(f"\nExpenses entered: {len(expenses)}")
    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. ${expense:.2f}")
    print(f"\n{'Total Spent:':<20} ${total:.2f}")
else:
    print("\nNo expenses entered.")

print("=" * 40)

# Case Study 13: ATM Transaction Sequence Simulation

account_balance = float(input("Enter opening balance (Rs.): "))
number_of_transactions = int(input("Enter number of transactions: "))

if account_balance < 0 or number_of_transactions <= 0:
    print("Invalid opening balance or transaction count.")
else:
    minimum_balance = 1000.0
    daily_withdrawal_limit = 20000.0
    total_withdrawn_today = 0.0
    
    print("\nEnter transactions (e.g. Type: deposit/withdraw, Amount: 500)")
    for transaction_number in range(1, number_of_transactions + 1):
        print("\nTransaction", transaction_number)
        transaction_type = input("Transaction type (deposit/withdraw): ").strip().lower()
        amount = float(input("Amount (Rs.): "))
        
        if transaction_type == "deposit" or transaction_type == "1":
            if amount > 0:
                account_balance = account_balance + amount
                print("Deposit successful! Current balance: Rs.", round(account_balance, 2))
            else:
                print("Invalid deposit amount.")
        elif transaction_type == "withdraw" or transaction_type == "2":
            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif (total_withdrawn_today + amount) > daily_withdrawal_limit:
                print("Failed: Exceeds daily withdrawal limit of Rs.", daily_withdrawal_limit)
            elif (account_balance - amount) < minimum_balance:
                print("Failed: Insufficient funds! Must maintain min balance of Rs.", minimum_balance)
            else:
                account_balance = account_balance - amount
                total_withdrawn_today = total_withdrawn_today + amount
                print("Withdrawal successful! Remaining balance: Rs.", round(account_balance, 2))
        else:
            print("Invalid transaction type.")
            
    print("\n--- Daily ATM Summary ---")
    print("Total cash withdrawn today: Rs.", round(total_withdrawn_today, 2))
    print("Closing available balance : Rs.", round(account_balance, 2))

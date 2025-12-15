def check_balance():
    print()
    print(f"Your current balance is {balance}")
    print("---------------------------------------")

def deposit(amount):
    if amount <= 0:
        print("   Deposit amount must be positive!")
        print("---------------------------------------")
        return False
    global balance
    balance += amount
    return True

def withdraw(amount):
    if amount <= 0:
        print("  Withdrawal amount must be positive!")
        print("---------------------------------------")
        return
    global balance
    if amount > balance:
        print("Insufficient funds!")
        print("---------------------------------------")
        return
    balance -= amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print()
        print("KYC not done")
        print("---------------------------------------")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")
            print("---------------------------------------")
            

balance = 0.0
kyc_documents = {}

if __name__ == "__main__":
    print("---------------------------------------")
    print("     Welcome to Mr.Dubey Bank !!!")
    print("---------------------------------------")
    print()


    while True:
        print("1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC documents")
        print("5. Update KYC documents")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            print()
            amt = float(input("Enter the amount to deposit: "))
            if deposit(amt):
                print(f"Amount {amt} deposited successfully.")
            print("---------------------------------------")
        elif choice == '3':
            print()
            amt = float(input("Enter the amount to withdraw: "))
            print("---------------------------------------")
            withdraw(amt)
            print(f"Amount {amt} withdrawn successfully.")
            print("---------------------------------------")
            print()
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs= {}
            n_documents= int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value 
            update_kyc(kyc_docs)
            print(f"KYC Updated!!")
            check_kyc()
        elif choice == '6':
            print("Quiting, have a nice day.")
            break
        else:
            print("      Invalid choice!!! Re-try.")
            print("---------------------------------------")

    print()
    print("Thank you for banking with us!!")

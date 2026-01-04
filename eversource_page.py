"""
Eversource Page Module

Manage existing Eversource utilities such that you can:
- create an eversource account
    - name on the account
    - account number
    - service address
    - monthly bill amount

- view eversource account details
- update eversource account information
- delete an eversource account

"""
eversource_account_list = []
eversource_accounts = {}

while True:
    print("What would you like to do?")
    print("1. Create Eversource Account")
    print("2. View Eversource Account Details")
    print("3. Update Eversource Account Information")
    print("4. Delete Eversource Account")
    print("5. Exit")

    select = input("Select an option (1-5): ")

    if select == '1':
        name = input("Enter the name on the account: ")
        account_number = input("Enter the account number: ")
        service_address = input("Enter the service address: ")
        monthly_bill = input("Enter the monthly bill amount: ")

        eversource_accounts[name] = {
            "account number": account_number,
            "service_address": service_address,
            "monthly_bill": monthly_bill
        }
        print("Eversource account created successfully.")
        eversource_account_list.append(name)

        print(eversource_account_list)

    elif select == '2':
        account_name = input("Enter or select the name of the account you want to view: ")
        print(eversource_account_list)
        print(eversource_accounts.get(account_name, "Account not found.")) 

    elif select == '3': 
        print(eversource_account_list)
        if len(eversource_account_list) == 0:
            print("No accounts available to update.")
            continue
        account_name = input("Enter which existing account you want to update: ")      

    elif select == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please try again.")

        
from services.sales_service import register_sale, list_items, show_sales_report
from services.platform_service import list_platforms

def main():
    print("Main file started")
    while True:
        print("\n1 - Register Sale")
        print("2 - List Items")
        print("3 - List Platforms")
        print("4 - Show Sales Report")
        print("0 - Exit")
        option = input("Choose an option: ")

        if option == "1":
            register_sale()
        elif option == "2":
            list_items()
        elif option == "3":
            platforms = list_platforms()
            print("\nPlatforms:")
            for p in platforms:
                print(f"{p['platform_id']} - {p['name']} (Selling Fee: {p['selling_fee']*100}%, Withdrawal Fee: {p['withdrawal_fee']*100}%)")
        elif option == "4":
            show_sales_report()
        elif option == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()




# main.py
from tracker import clean_code, find_parcel, update_status

parcels = [
    {"code": "BP-20418", "status": "In transit", "location": "Depot A"},
    {"code": "BP-20419", "status": "Delivered", "location": "Customer"},
    {"code": "BP-20420", "status": "Out for delivery", "location": "Depot B"},
]


def show_menu():
    print()
    print("1) Look up a parcel")
    print("2) Update a status")
    print("3) List all parcels")
    print("4) Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            code = clean_code(input("Tracking code: "))
            if code == "":
                print("Please enter a tracking code.")
                continue
            parcel = find_parcel(parcels, code)
            if parcel is None:
                print("No parcel found with that code.")
            else:
                print(f"{code}: {parcel['status']} at {parcel['location']}")
        elif choice == "2":
            code = clean_code(input("Tracking code: "))
            new_status = input("New status: ").strip()
            if update_status(parcels, code, new_status):
                print("Status updated.")
            else:
                print("No parcel found with that code.")
        elif choice == "3":
            for parcel in parcels:
                print(f"{parcel['code']}: {parcel['status']}")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
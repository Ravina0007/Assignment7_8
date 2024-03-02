def enter_new_airport(airports):
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airports[icao_code] = airport_name
    print("New airport added successfully!")

def fetch_airport_info(airports):
    icao_code = input("Enter the ICAO code of the airport: ")
    if icao_code in airports:
        airport_name = airports[icao_code]
        print("Airport Name:", airport_name)
    else:
        print("Airport not found!")

def main():
    airports = {}

    while True:
        print("\nMenu:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            enter_new_airport(airports)
        elif choice == "2":
            fetch_airport_info(airports)
        elif choice == "3":
            print("Quitting the program...")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
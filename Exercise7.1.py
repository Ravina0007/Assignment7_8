def get_season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    month = (month - 1) % 12 

    if month < 3:
        return seasons[0]  # Winter
    elif month < 6:
        return seasons[1]  # Spring
    elif month < 9:
        return seasons[2]  # Summer
    else:
        return seasons[3]  # Autumn

def main():
    month = int(input("Enter the number of a month (1-12): "))
    season = get_season(month)
    print("The corresponding season is:", season)

if __name__ == "__main__":
    main()
def categorize_parcel(weight):
    if weight < 5:
        return "Light"
    elif 5 <= weight <= 15:
        return "Medium"
    else:
        return "Heavy"

weight = float(input("Enter the parcel weight (kg): "))
print(f"Parcel category: {categorize_parcel(weight)}")



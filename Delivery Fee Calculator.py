def calculate_delivery_fee():
    distance = float(input("Enter distance in kilometers: "))
    rate = float(input("Enter rate per kilometer (₱): "))
    total_fee = distance * rate
    print(f"Total Delivery Fee: ₱{total_fee:.2f}")

calculate_delivery_fee()
travel = []

print("Enter your 5 travel destinations:")

for i in range(5):
    place = input(f"Destination {i+1}: ")
    travel.append(place)

print("\nOriginal Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {travel[i]}")

print("\nUpdate your 2nd and 5th destinations:")
travel[1] = input("New destination for position 2: ")
travel[4] = input("New destination for position 5: ")

print("\nUpdated Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {travel[i]}")

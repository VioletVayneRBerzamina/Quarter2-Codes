
destinations = []

print("Please enter your 5 travel destinations:")
for i in range(5):
    place = input(f"Destination {i + 1}: ")
    destinations.append(place)

print("\nOriginal Travel Itinerary:")
for i in range(len(destinations)):
    print(f"{i + 1}. {destinations[i]}")

print("\nLet's update your 2nd and 5th destinations.")

destinations[1] = input("Enter a new destination for position 2: ")

destinations[4] = input("Enter a new destination for position 5: ")

print("\nUpdated Travel Itinerary:")
for i in range(len(destinations)):
    print(f"{i + 1}. {destinations[i]}")

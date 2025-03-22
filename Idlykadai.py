menu = ["இட்லி", "தோசை",  "வடை", "பொங்கல்", "பூரி", "டீ", "காபி"]
prices = [20, 50, 10, 40, 35, 15, 20]

print("முருகன் இட்லி கடை ")

total_amount = 0

while True:
    print("காலை உணவு:")
    for index, item in enumerate(menu, 1):
        print(f"{index}. {item} = ₹{prices[index-1]}")

    try:
        order_choice = input("நீங்கள் ஆர்டர் செய்ய விரும்பும் உணவின் எண்ணைத் தேர்ந்தெடுக்கவும்: ")
        order_choices = order_choice.split()

        for choice in order_choices:
            order_choice_int = int(choice)
            if 1 <= order_choice_int <= len(menu):
                selected_item = menu[order_choice_int - 1]
                price = prices[order_choice_int - 1]
                total_amount += price
                print(f" {selected_item} = ₹{price}")
            else:
                print(f"எண் {choice} தவறானது! சரியான எண்ணைத் தேர்ந்தெடுக்கவும்.")

    except ValueError:
        print("Invalid input. Please enter valid numbers separated by space or comma.")
        continue

    another_order = input("வேறு ஏதாவது ஆர்டர் செய்ய விரும்புகிறீர்களா? (yes/no): ").lower()

    if another_order != "yes":
        print(f"செலுத்த வேண்டிய மொத்தத் தொகை : ₹{total_amount}")
        print("உங்கள் ஆர்டருக்கு நன்றி! இன்றைய நாள் இனிய நாளாக வாழ்த்துக்கள்!!")
        break

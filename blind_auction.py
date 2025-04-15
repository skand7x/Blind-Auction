from art import logo

print(logo)

next_bid = True
name_price = {}

while next_bid is True:
    name = input("What is your name?:\n").lower()
    bid = input("What is your bid?:\n$")
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if other_bidders == "yes":
        print("\n" * 20)

    if other_bidders == "no":
        next_bid = False


    name_price[name] = bid

# print(name_price)
highest_bid = 0
winner = ''
for names in name_price:
    price = int(name_price[names])
    if price > highest_bid:
        highest_bid = price
        winner = names


print(f"The winner is {winner} with a bid of ${highest_bid}")





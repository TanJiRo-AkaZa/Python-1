def hotel(nights):
    return nights * 140
def plane(city):
    if city == "London":
        return 183
    elif city == "Paris":
        return 220
    elif city == "Berlin":
        return 222
    elif city == "Madrid":
        return 475
def car(days):
    if days>=7:
        return days*40-50
    elif days>=3:
        return days*40-20
    else:
        return days*40
def trip_cost(city, days, spending_money):
    return car(days)+hotel(days)+plane(city)+spending_money
print("cost of rental car", car(5))
print("the cost of plane ride", plane("Paris"))
print("cost of hotel", hotel(5))

print("total trip cost", trip_cost("London", 5, 200))
print(trip_cost("Paris", 5, 200))



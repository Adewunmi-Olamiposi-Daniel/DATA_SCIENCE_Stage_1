
def Total_cost():
    item1 = int(input("Enter figure for the first item: "))
    item2 = int(input("Enter figure for the second item: "))
    item3 = int(input("Enter figure for the third item: "))

    total = item1 + item2 + item3

    if total > 4000:
        discount = total * 0.9   # apply 10% discount (i.e., 90% of total)
        print (f"Total before discount {total}")
        print(f"Total after discount {discount}")
    else:
        print(f"Your total is {total}.No discount.Buy more")

    return
Total_cost()

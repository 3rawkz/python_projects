# info about an e-comm cart

from string import Template


class CartTemplate(Template):
    delimiter = '#'


def main():
    cart = []
    # could be added with a button
    cart.append(dict(item="Coke", price=4, qty=2))
    cart.append(dict(item="Fry", price=2, qty=2))
    cart.append(dict(item="Burger", price=6, qty=2))

    t = CartTemplate("#qty x #item = $#price")
    total = 0
    print("Cart:")

    for item in cart:
        print(t.substitute(item))
        total += item["price"]
    print("Total: $"+str(total))

# if the current file is being run then run main
if __name__ == '__main__':
    main()


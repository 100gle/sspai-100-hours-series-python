class Order:
    def __init__(self, item, telephone):
        self.item = item
        self.telephone = telephone


def query_item_number(name):
    print(f"Query database for {name}...")
    if name == "Macbook Pro M1":
        return 0


def notify(telephone, message):
    print(f"Send message to {telephone}: {message}")


def register(order, callback=None):

    number = query_item_number(order.item)

    if number == 0:
        message = "Sorry, we are out of stock."

        if callback:
            callback(order.telephone, message=message)
        return "register failed."

    return "register success."


def main():

    order = Order(item="Macbook Pro M1", telephone="000-0001")
    status = register(order, callback=notify)
    print(f"Register status: {status}")


if __name__ == "__main__":
    main()

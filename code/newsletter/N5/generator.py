def make_cards(values):
    container = values or []
    for value in container:
        yield value


def main():
    from collections.abc import Generator

    cards = make_cards(list("JQK"))
    print(cards)

    print(f"Is the cards variable a generator? {isinstance(cards, Generator)}")
    for card in cards:
        print(card)

    results = list(cards)
    print(results)


if __name__ == '__main__':
    main()

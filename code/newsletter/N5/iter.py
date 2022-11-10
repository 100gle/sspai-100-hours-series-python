class CardGroup:
    def __init__(self, container) -> None:
        self.container = container
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
        else:
            raise StopIteration
        return value


class Cards:
    def __init__(self, values=None) -> None:
        self._container = values or []

    def __iter__(self):
        return CardGroup(self._container)

    def __getitem__(self, index):
        return self._container[index]


def main():
    from collections.abc import Iterable

    cards = Cards(list("JQK"))
    print(f"Is the cards variable an iterale? {isinstance(cards, Iterable)}")

    for card in cards:
        print(card)

    print(cards[1:])


if __name__ == '__main__':
    main()

class Father:  # 1
    genre = "sports"  # 2

    def __init__(self, name):  # 4
        self.name = name

    def exercise(self):  # 4
        print('exercise better!')


class Child(Father):  # 5
    def __init__(self, name, gender):  # 6
        self.name = name  # 7
        self.gender = gender  # 8

    def exercise(self):  # 9
        if self.genre == "sports":
            print("exercise good!")
        else:
            print("exercise")

    def hobbies(self):  # 10
        return ["reading", "watching movies", "music"]


def main():
    elder_ming = Father("Ming")
    elder_ming.exercise()
    elder_ming_has_hobbies = hasattr(elder_ming, "hobbies") or False
    print(f"Elder Ming has other hobbies? {elder_ming_has_hobbies}")
    print("=" * 20)

    young_ming = Child("Ming", "boy")
    young_ming.exercise()
    young_ming_has_hobbies = hasattr(young_ming, "hobbies")
    print(f"Young Ming has other hobbies? {young_ming_has_hobbies}")
    if young_ming_has_hobbies:
        print(f"Young Ming's hobbies: {young_ming.hobbies()}")


if __name__ == '__main__':
    main()

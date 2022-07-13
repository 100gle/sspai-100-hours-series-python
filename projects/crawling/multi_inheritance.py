class GrandFather:
    genre = "sports"
    gender = "male"

    def __init__(self):
        pass


class GrandMother:
    gender = "female"

    def __init__(self):
        pass


class Father(GrandFather, GrandMother):
    gender = "male"

    def __init__(self):
        print("Father")


class Mother(GrandFather, GrandMother):
    genre = "music"
    gender = "female"

    def __init__(self):
        print("Mother")


class Child(Father, Mother):
    def __init__(self):
        pass


if __name__ == '__main__':
    child = Child()
    print(child.genre)
    print(child.gender)

import pytest
from faker import Faker
from faker.providers import BaseProvider


@pytest.fixture(scope="session", autouse=True)
def faker_session_locale():
    return "zh-CN"


class MyProvider(BaseProvider):
    def custom_locales(self):
        choices = ["zh-CN", "en-US", "ja-JP", "ko-KR"]
        return self.random_element(choices)

    def custom_programming_languages(self):
        langs = ["Python", "Java", "Golang", "JavaScript", "Swift"]
        return self.random_element(langs)

    def custom_numbers(self, n: int = 10):
        if n < 0:
            raise ValueError("n must be greater than or equal to 0.")

        return self.random_element(list(range(n)))


@pytest.fixture()
def faker(request):
    if "faker_locale" in request.fixturenames:
        locale = request.getfixturevalue("faker_locale")
        fake = Faker(locale=locale)
    else:
        fake = request.getfixturevalue("_session_faker")

    seed = 0
    if "faker_seed" in request.fixturenames:
        seed = request.getfixturevalue("faker_seed")
    fake.seed_instance(seed=seed)
    fake.unique.clear()

    fake.add_provider(MyProvider)
    return fake

import pytest


def test_faker_fixture(faker):
    assert faker.unique.boolean()


def test_faker_chinese_name(faker):
    import re

    name = faker.name()
    print(f"name is: {name}")
    assert re.match(r"[\u4e00-\u9eff]", name)


def test_faker_custom_locale(faker):
    el = faker.custom_locales()
    assert el in ["zh-CN", "en-US", "ja-JP", "ko-KR"]


def test_faker_custom_programming_language(faker):
    el = faker.custom_programming_languages()
    assert el in ["Python", "Java", "Golang", "JavaScript", "Swift"]


@pytest.mark.parametrize("n", argvalues=[1, 10, 100])
def test_faker_custom_numbers(faker, n):
    el = faker.custom_numbers(n=n)
    assert el in list(range(n))

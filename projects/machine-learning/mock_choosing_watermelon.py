import unittest


def get_answer_by_feature(feature, answer):
    if feature in answer:
        return True
    return False


def is_better_watermelon(appearance, pattern, spot_range, echo):
    features = [
        get_answer_by_feature(appearance, {"round", "oval"}),
        get_answer_by_feature(pattern, {"clear", "bright"}),
        get_answer_by_feature(spot_range, {"middle", "big"}),
        get_answer_by_feature(echo, {"clear", "pleasant"}),
    ]

    if features.count(True) >= 3:
        return True
    return False


class TestChooseBetterWatermelon(unittest.TestCase):

    samples = [
        dict(appearance="broken", pattern="clear", spot_range="big", echo="depressing"),
        dict(appearance="round", pattern="clear", spot_range="big", echo="pleasant"),
        dict(appearance="oval", pattern="bright", spot_range="middle", echo="clear"),
        dict(
            appearance="round", pattern="blured", spot_range="small", echo="depressing"
        ),
    ]

    def test_is_better_watermelon(self):
        for sample in self.samples:
            with self.subTest(**sample):
                self.assertTrue(is_better_watermelon(**sample))


if __name__ == "__main__":
    unittest.main(verbosity=2)

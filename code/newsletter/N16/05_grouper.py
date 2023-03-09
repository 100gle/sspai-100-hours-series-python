from rocketry import Grouper, Rocketry
from rocketry.args import Arg

app = Rocketry()

# -----------
# Daily Tasks
# -----------
daily_group = Grouper()


@daily_group.param("daily_signal")
def signal():
    return "Bang!"


@daily_group.task("daily")
def postit(signal=Arg("daily_signal")):
    ...


# ------------
# Weekly Tasks
# ------------

weekly_group = Grouper()


@weekly_group.param("weekly_signal")
def signal():
    return "weekly"


@weekly_group.task("weekly")
def backup(signal=Arg("weekly_signal")):
    ...


app.include_grouper(daily_group)
app.include_grouper(weekly_group)

if __name__ == '__main__':
    app.run()

from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import after_success

app = Rocketry(execution="async")


@app.task('every 3 second')
def success():
    return True


@app.task(after_success(success))
def handle(is_success=Return(success)):
    status = "Done" if is_success else "Running"
    print(f"Task status is: {status}")


if __name__ == '__main__':
    app.run()

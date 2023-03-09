from rocketry import Rocketry

app = Rocketry()


def get_params():
    yield {"name": "100gle"}
    yield {}


@app.task()
def greet(name=None):
    msg = name or "world"
    print(f"Hello, {msg}!")


@app.task('every 3 second', execution="thread")
def do_callback():
    for params in get_params():
        task = app.session["greet"]
        task.run(**params)


if __name__ == '__main__':
    app.run()

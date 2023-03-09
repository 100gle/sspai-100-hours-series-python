from rocketry import Rocketry

app = Rocketry(execution="main")
times = 0


@app.task('every 1 second')
def echo():
    global times
    times += 1
    print(f"Running {times} times...")


if __name__ == '__main__':
    app.run()

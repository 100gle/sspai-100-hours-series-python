class Device:
    def __init__(self, name: str):
        self.name = name

    def boot(self):
        print(f"Device<{self.name}> is booting...")


class Switcher:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        self._on()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._off()

    def _on(self):
        print(f"Loading switcher...")

    def _off(self):
        print(f"Closing switcher...")

    def plug(self, device: Device):
        device.boot()


def main():

    with Switcher() as switcher:
        device = Device("PC")
        switcher.plug(device)


if __name__ == '__main__':
    main()

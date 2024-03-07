import ursina


class App:
    def __init__(self):
        self.__app: ursina.Ursina = ursina.Ursina()

    def run(self):
        self.__app.run()


if __name__ == "__main__":
    app: App = App()

    app.run()

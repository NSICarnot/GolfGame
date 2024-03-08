import ursina
from ursina.prefabs.first_person_controller import FirstPersonController


class EventHandler(ursina.Entity):
    def __init__(self, app: "App", **kwargs):
        super().__init__(**kwargs)
        self.__app: ursina.Ursina = app.get_ursina_instance()

    def input(self, key):
        if key == "escape":
            self.__app.destroy()
            self.__app.finalizeExit()


class Controller(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self):
        super().update()
        if self.position[1] <= -10:
            self.position = (0, 3, 0)


class App:
    def __init__(self):
        self.__app: ursina.Ursina = ursina. Ursina()

        # Scene objects
        self.__ground: ursina.Entity = ursina.Entity(
            model="cube",
            color=ursina.color.rgb(255, 255, 255),
            scale=(10, 1, 10),
            collider="box"
        )

        self.__controller: Controller = Controller()

    def get_ursina_instance(self) -> ursina.Ursina:
        return self.__app

    def run(self):
        self.__app.run()


if __name__ == "__main__":
    try:
        app: App = App()
        event_handler: EventHandler = EventHandler(app)
        app.run()
    except Exception as e:
        print(f"Error occurred: {e}")

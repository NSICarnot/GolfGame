import ursina
import constants as c


class Ball(ursina.Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Ball variables
        self.__radius: float = 0.215  # In deci-meters
        self.__mass: float = 45.93  # In grams
        self.__static_force_coef: float = .30  # In Newtons
        self.__kinetic_force_coef: float = .26  # In Newtons

        self.__grounded: bool = False

        # Entity variables
        self.model = "sphere"
        self.color = ursina.color.rgb(255, 255, 255)
        self.position = ursina.Vec3(0, 2, 0)
        self.scale = self.__radius
        self.collider_setter('box')

    def grounded(self, val: bool | None = None) -> bool | None:
        if val:
            self.__grounded = val
        return self.__grounded

    def apply_gravity(self):
        origin: ursina.Vec3 = ursina.Vec3(self.position.x, self.position.y-self.__radius, self.position.z)
        direction: ursina.Vec3 = ursina.Vec3(0, -1, 0)
        hit_info: ursina.raycast = ursina.raycast(origin, direction, ignore=(self,), distance=.005, debug=False)
        if not hit_info and not self.grounded():
            # Apply the gravity force in Newton
            self.position += ursina.Vec3(0, c.EARTH_GRAVITY * self.__mass * .001 * ursina.time.dt, 0)
        else:
            self.grounded(True)

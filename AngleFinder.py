import random
import turtle


RADIUS = 270
ARROWHEAD_LENGTH = 50


class Angle:
    def __init__(self):
        turtle.mode("logo")
        turtle.speed(0)
        turtle.hideturtle()
        self.angle = None
        self.reset()

    def reset(self, *args) -> None:
        self.angle = random_angle()
        with Unbind(self.show_answer):
            with Origin():
                turtle.clear()
                self.draw_circle()
            self.draw_arrow()

    def goto_edge(self) -> None:
        turtle.setheading(self.angle)
        turtle.forward(RADIUS)

    def draw_arrow(self, *args) -> None:
        with Unbind(self.show_answer):
            with Origin():
                self.goto_edge()

                # draw arrowhead
                for heading in [self.angle + 45, self.angle - 45]:
                    turtle.setheading(heading)
                    turtle.backward(ARROWHEAD_LENGTH)
                    turtle.forward(ARROWHEAD_LENGTH)

    def show_answer(self, *args) -> None:
        with Unbind(self.reset):
            with Origin():
                with PenUp():
                    turtle.goto(0.8 * RADIUS, 0.8 * RADIUS)
                msg = f"{self.angle:03d}\N{DEGREE SIGN}"
                turtle.write(msg, align="left", font=("Arial", 14, "normal"))

    def draw_circle(self) -> None:
        with Origin():
            with PenUp():
                turtle.forward(RADIUS)
            turtle.left(90)
            turtle.circle(RADIUS)


def random_angle() -> int:
    return random.randrange(10, 360, step=5)


class Origin:
    def __init__(self):
        self.x, self.y = turtle.position()
        self.heading = turtle.heading()

    def __enter__(self):
        with PenUp():
            turtle.home()
            turtle.setheading(360)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with PenUp():
            turtle.goto(self.x, self.y)
            turtle.setheading(self.heading)


class PenUp:
    def __enter__(self):
        turtle.penup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        turtle.pendown()


class Unbind:
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        turtle.onscreenclick(None)

    def __exit__(self, exc_type, exc_val, exc_tb):
        turtle.onscreenclick(self.func)


def test_ui():
    a = Angle()
    turtle.mainloop()


if __name__ == "__main__":
    test_ui()
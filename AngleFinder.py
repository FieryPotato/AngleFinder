import random
import turtle


RADIUS = 270
ARROWHEAD_LENGTH = 50
HEADING_INCREMENTS = 5


class Angle:
    def __init__(self):
        turtle.mode("logo")
        turtle.speed(0)
        turtle.hideturtle()
        self.angle = None
        self.reset()

    def reset(self, *args) -> None:
        """
        Clear screen and reset turtle, draw arrow at the same time.
        """
        self.angle = random_angle()
        with Unbind(self.show_answer):
            with Origin():
                turtle.clear()
                self.draw_circle()
            self.draw_arrow()

    def goto_edge(self) -> None:
        """
        Move turtle to edge of circle.
        """
        turtle.setheading(self.angle)
        turtle.forward(RADIUS)

    def draw_arrow(self, *args) -> None:
        """
        Draw the arrow.
        """
        with Unbind(self.show_answer):
            with Origin():
                self.goto_edge()

                # draw arrowhead
                for heading in [self.angle + 45, self.angle - 45]:
                    turtle.setheading(heading)
                    turtle.backward(ARROWHEAD_LENGTH)
                    turtle.forward(ARROWHEAD_LENGTH)

    def show_answer(self, *args) -> None:
        """
        Display the current heading in degrees.
        """
        with Unbind(self.reset):
            with Origin():
                with PenUp():
                    turtle.goto(0.8 * RADIUS, 0.8 * RADIUS)
                msg = f"{self.angle:03d}\N{DEGREE SIGN}"
                turtle.write(msg, align="left", font=("Arial", 14, "normal"))

    def draw_circle(self) -> None:
        """
        Draw the enclosing circle.
        """
        with Origin():
            with PenUp():
                turtle.forward(RADIUS)
            turtle.left(90)
            turtle.circle(RADIUS)


def random_angle() -> int:
    """
    Generates a random angle between 10
    :return: number between HEADING_INCREMENTS and 360
    """
    return random.randrange(HEADING_INCREMENTS, 360, step=HEADING_INCREMENTS)


class Origin:
    """
    Context manager for enforcing centering of turtle.
    """
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
    """
    Context manager for automating turtle.penup() and turtle.pendown()
    during movement.
    """
    def __enter__(self):
        turtle.penup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        turtle.pendown()


class Unbind:
    """
    Context manager for unbinding and rebinding to prevent inputs
    during drawing.
    """
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        turtle.onscreenclick(None)

    def __exit__(self, exc_type, exc_val, exc_tb):
        turtle.onscreenclick(self.func)


def main():
    Angle()
    turtle.mainloop()


if __name__ == "__main__":
    main()
"""
    An example of using Navigator within a class and having bound methods as actors
"""
from navigator import ui, Navigator, Actor


class MyClass(object):
    nav = Navigator()

    def __init__(self):
        self.nav._add_actor(Actor("Class Method", self.print_y))
        self.nav._add_actor(Actor("Instance Method", self.print_x))

    def print_x(self):
        ui.text_success("I belong to instance of {}".format(self.__class__.__name__))

    @classmethod
    def print_y(cls):
        ui.text_success("I staticly belong to {}".format(cls.__name__))

    @staticmethod
    @nav.route("Static Method")
    def print_0():
        ui.text_success("I'm entirely static (and ecstatic :) )")


if __name__ == "__main__":
    MyClass().nav.run()
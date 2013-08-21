from functools import wraps

from . import ui, decorators
# TODO - Add doc strings


def do_nothing():
    pass


#-----------------------------------------------------------------------------#
class Navigator(object):
    def __init__(self, message, intro=None):
        self.actors = {}
        self.message = message
        self.intro = intro
        self.completed = Actor('quit', 'exit', do_nothing)

    def _add_actor(self, actor):
        if actor.name in self.actors:
            raise NameError("Name '{}' is already assigned".format(actor.name))
        self.actors[actor.name] = actor

    def route(self, name, blurb):
        """Decorator for registering functions"""
        def inner(f):
            actor = Actor(name, blurb, f)
            self._add_actor(actor)

            @wraps(f)
            def wrapped(*args, **kwargs):
                return f(*args, **kwargs)
            return wrapped
        return inner

    def register_assistant(self, assistant):
        self._add_actor(assistant)

    def __repr__(self):
        return "<Navigator - {}>".format(self.intro)

    def display_info(self):
        if self.intro is not None:
            ui.text_info(self.intro)

    @decorators.catch_exit_keys
    def run(self):
        self.display_info()
        choices = [(self.completed.label, self.completed)]
        for key in iter(self.actors):
            actor = self.actors[key]
            choices.append((actor.label, actor))
        picked = ui.choice(self.message, choices)
        ui.text_success("Selected {}".format(picked.name))
        picked.run()


class Assistant(Navigator):
    def __init__(self, name, blurb, message):
        super(Assistant, self).__init__(message=message)
        self.blurb = blurb
        self.name = name
        self.label = "{} - {}".format(name, blurb)

    def __repr__(self):
        return "<Assistant {}>".format(self.label)

    def display_info(self):
        ui.text_info(self.label)

class Actor(object):
    def __init__(self, name, blurb, func):
        self.name = name
        self.blurb = blurb
        self.func = func
        self.label = "{} - {}".format(name, blurb)

    def __repr__(self):
        return "<Actor {}>".format(self.label)

    def run(self):
        self.func()

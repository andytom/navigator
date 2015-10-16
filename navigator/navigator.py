from functools import wraps
import sys
from collections import OrderedDict


from . import ui, decorators
# TODO - Add doc strings
# TODO - Add better comments


#-----------------------------------------------------------------------------#
# Helper Functions
#-----------------------------------------------------------------------------#
def do_nothing():
    pass


#-----------------------------------------------------------------------------#
# Main Classes
#-----------------------------------------------------------------------------#
class Navigator(object):
    def __init__(self, message="What do you want to do?", intro=None,
                 done_name='quit', no_confirm=True, default_choice=None):
        self.actors = OrderedDict()
        self.message = message
        self.intro = intro
        self.completed = Actor(done_name, sys.exit)
        self.no_confirm = no_confirm
        self.default_choice = default_choice

    def _add_actor(self, actor):
        if actor.name in self.actors:
            raise NameError("Name '{}' is already assigned".format(actor.name))
        self.actors[actor.name] = actor

    def route(self, name, blurb=""):
        """Decorator for registering functions"""
        def inner(f):
            actor = Actor(name, f, blurb)
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
    def _do_run(self):
        choices = [(self.completed.label, self.completed)]
        for key in iter(self.actors):
            actor = self.actors[key]
            choices.append((actor.label, actor))
        picked = ui.choice(self.message, choices, self.default_choice)
        if self.no_confirm or ui.confirm("Run {}?".format(picked.name), True):
            picked.run()

    def run(self):
        self.display_info()
        while True:
            self._do_run()


class Assistant(Navigator):
    def __init__(self, name, blurb, message="What do you want to do?",
                 done_name='back', no_confirm=True, default_choice=None):
        super(Assistant, self).__init__(message=message, no_confirm=no_confirm, default_choice=default_choice)
        self.blurb = blurb
        self.name = name
        self.label = "{} - {}".format(name, blurb)
        self.completed = Actor(done_name, do_nothing)

    def __repr__(self):
        return "<Assistant {}>".format(self.label)

    def display_info(self):
        ui.text_info(self.label)

    def run(self):
        self.display_info()
        self._do_run()


class Actor(object):
    def __init__(self, name, func, blurb=""):
        self.name = name
        self.blurb = blurb
        self.func = func
        if blurb:
            self.label = "{} - {}".format(name, blurb)
        else:
            self.label = name

    def __repr__(self):
        return "<Actor {}>".format(self.label)

    def run(self):
        return self.func()

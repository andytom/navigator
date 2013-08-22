"""
    Navigator
    ---------

    Navigator is a simple framework for creating simple, interactive
    command line tools.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
"""
from functools import wraps
import sys

from . import ui, decorators
# TODO - Add doc strings
# TODO - Add better comments


#-----------------------------------------------------------------------------#
# Meta Stuff
#-----------------------------------------------------------------------------#
__version__ = '0.0.1'


#-----------------------------------------------------------------------------#
# Helper Functions
#-----------------------------------------------------------------------------#
def do_nothing():
    pass


#-----------------------------------------------------------------------------#
# Main Classes
#-----------------------------------------------------------------------------#
class Navigator(object):
    def __init__(self, message, intro=None, done_name='quit'):
        self.actors = {}
        self.message = message
        self.intro = intro
        self.completed = Actor(done_name, sys.exit)

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
        picked = ui.choice(self.message, choices)
        ui.text_success("Selected {}".format(picked.name))
        picked.run()

    def run(self):
        self.display_info()
        while True:
            self._do_run()


class Assistant(Navigator):
    def __init__(self, name, blurb, message, done_name='back'):
        super(Assistant, self).__init__(message=message)
        self.blurb = blurb
        self.name = name
        self.label = "{} - {}".format(name, blurb)
        self.completed = Actor(done_name, do_nothing)

    def __repr__(self):
        return "<Assistant {}>".format(self.label)

    def display_info(self):
        ui.text_info(self.label)

    def run(self):
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

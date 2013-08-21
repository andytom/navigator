import sys
import unittest

import navigator


#-----------------------------------------------------------------------------#
# Test Cases
#-----------------------------------------------------------------------------#
class navigatorBasicFunctionalityTestCase(unittest.TestCase):
    def setUp(self):
        self.test_nav = navigator.Navigator(__name__)

    def test_calling_an_actor(self):
        @self.test_nav.route('test')
        def test():
            return 'OK'
        self.assertTrue('test' in self.test_nav.actors)
        result = self.test_nav.actors['test'].run()
        self.assertEqual(result, "OK")


class navigatorAddingActorsTestCase(unittest.TestCase):
    def setUp(self):
        self.test_nav = navigator.Navigator(__name__)

    def test_adding_a_route_via_decorator(self):
        self.assertFalse('add' in self.test_nav.actors)

        @self.test_nav.route('add', 'add 1 + 2 and return the result')
        def add():
            return 1 + 2
        self.assertTrue('add' in self.test_nav.actors)

    def test_adding_an_actor_directly(self):
        self.assertFalse('add' in self.test_nav.actors)

        def add():
            return 1 + 2
        actor = navigator.Actor('add', '', add)
        self.test_nav._add_actor(actor)
        self.assertTrue('add' in self.test_nav.actors)

    def test_adding_a_route_via_decorator_cannot_replace(self):
        @self.test_nav.route('add', 'add 1 + 2 and return the result')
        def add():
            return 1 + 2

        with self.assertRaises(NameError, msg="Name 'add' is already assigned"):
            @self.test_nav.route('add', 'Also add 1 + 2 and return the resul')
            def add_2():
                return 1 + 2

    def test_adding_directly_cannot_replace(self):
        def add():
            return 1 + 2

        def add_2():
            return 1 + 2

        actor = navigator.Actor('add', '', add)
        actor_2 = navigator.Actor('add', '', add_2)

        self.test_nav._add_actor(actor)

        with self.assertRaises(NameError, msg="Name 'add' is already assigned"):
            self.test_nav._add_actor(actor_2)

    def test_adding_mixed_cannot_replace(self):
        @self.test_nav.route('add', 'add 1 and 2 return the result')
        def add():
            return 1 + 2

        def add_2():
            return 1 + 2

        actor_2 = navigator.Actor('add', '', add_2)

        with self.assertRaises(NameError, msg="Name 'add' is already assigned"):
            self.test_nav._add_actor(actor_2)


class navigatorAddingAssistantTestCase(unittest.TestCase):
    def setUp(self):
        self.test_nav = navigator.Navigator(__name__)

    def test_registering_an_assistant(self):
        self.assertFalse('Powers' in self.test_nav.actors)
        assistant = navigator.Assistant("Powers", "Tools for powers", "Prompt")
        self.test_nav.register_assistant(assistant)
        self.assertTrue('Powers' in self.test_nav.actors)

    def test_adding_a_route_to_an_assistant(self):
        assistant = navigator.Assistant("Powers", "Tools for powers", "Prompt")

        self.assertFalse('square' in assistant.actors)
        self.assertFalse('cube' in assistant.actors)

        @assistant.route('square', 'returns 3 * 3')
        def square():
            return 3 * 3

        @assistant.route('cube', 'returns 3^3')
        def cube():
            return 3 * 3 * 3

        self.assertTrue('square' in assistant.actors)
        self.assertTrue('cube' in assistant.actors)


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True)

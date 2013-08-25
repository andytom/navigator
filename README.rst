Navigator
=========
A framework to create simple, interactive command line tools.

Example
-------
A basic Hello World example ::

    >>> import navigator
    >>> nav = navigator.Navigator(intro="Welcome")
    >>> @nav.route('Hello World', "A simple Hello World")
    >>> def hello_world():
    >>>     navigator.ui.text_success("Hello World!")
    >>> nav.run()
    Welcome
    0 - quit
    1 - Hello World - A simple Hello World
    What do you want to do?

You can then select the option you would like to take. Entering one runs hello_world.

Navigator also includes prompts for user input ::

    >>> @nav.route('Hello Name', "A more advanced Hello World")
    >>> def hello_name():
    >>>     name = navigator.ui.prompt("What is your name?")
    >>>     navigator.ui.text_success("Hello {}!".format(name))


There are more complete examples in the examples directory.

To Do List
----------
- Complete README (examples, basic how to)
- Better Comments
- Add more Documentation (doc strings and documentation)
- Better test coverage
- Put on pypy

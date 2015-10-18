Navigator
=========

.. image:: https://travis-ci.org/andytom/navigator.svg?branch=master
    :target: https://travis-ci.org/andytom/navigator

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

You can then select the option you would like to take.
Entering '1' call the hello_world function.

Navigator also includes prompts for user input ::

    >>> @nav.route('Hello Name', "A more advanced Hello World")
    >>> def hello_name():
    >>>     name = navigator.ui.prompt("What is your name?")
    >>>     navigator.ui.text_success("Hello {}!".format(name))


There are more complete examples in the examples directory.

How to Install
--------------
Navigator can be install from pypi using pip ::

    pip install navigator

Python Support and Versioning
-----------------------------
Navigator is currently tested against python 2.7, 3.2, 3.3, 3.4 and 3.5.

Navigator follows `SemVar <http://semver.org/>`_ as such the Public API should
not be considered stable until version 1.0.0.

Testing
-------
You can run the test suite locally by running: ::

    python test.py

This requires that 'mock' is installed. In addition all tests are run automatically on
`TravisCI <https://travis-ci.org/andytom/navigator>`_.

To Do List
----------
- Complete README (examples, basic how to)
- Better Comments
- Add more Documentation (doc strings and documentation)
- More complete test coverage and better tests

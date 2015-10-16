"""
    An example of using default values in prompt
"""
from navigator import Navigator, ui


nav = Navigator(intro="Defaults example", done_name="Quit", default_choice=1)


@nav.route("Default action", "if you press enter without entering a choice this will be called")
def default_choice():
    ui.text_success("I'm the default")


@nav.route("Question with default", "Will prompt wil a default valid input")
def question_with_default():
    ui.prompt("Are you sure?", default="Yes")


@nav.route("Question without default", "Will prompt without a default value, and insist on a valid input")
def question_without_default():
    ui.prompt("Are you sure?")


if __name__ == "__main__":
    nav.run()
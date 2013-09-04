import navigator

intro = """
 _____       _             
|_   _|     | |            
  | |  _ __ | |_ _ __ ___  
  | | | '_ \| __| '__/ _ \ 
 _| |_| | | | |_| | | (_) |
|_____|_| |_|\__|_|  \___/ 
"""                                      

nav = navigator.Navigator(intro=intro)

@nav.route('Add', "Add 1 to 3 and print the result")
def add():
    navigator.ui.text_success(1 + 3)

@nav.route('Sub', "Subtract 3 from 1 and print the result")
def sub():
    navigator.ui.text_success(1 - 3)


assistant = navigator.Assistant("Powers", "Stuff for powers", "Select one:")
nav.register_assistant(assistant)


@assistant.route('Square', "Squares the number 3 and prints the result")
def square():
    navigator.ui.text_success(3 ** 2)


@assistant.route('Cube', "Cube the number 3 and prints the result")
def cube():
    navigator.ui.text_success(3 ** 3)


if __name__ == "__main__":
    nav.run()

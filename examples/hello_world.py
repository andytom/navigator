import navigator

intro = """
  _    _      _ _       
 | |  | |    | | |      
 | |__| | ___| | | ___  
 |  __  |/ _ \ | |/ _ \ 
 | |  | |  __/ | | (_) |
 |_|  |_|\___|_|_|\___/ 
"""                                      

nav = navigator.Navigator(intro=intro)

@nav.route('Hello World', "A simple Hello World")
def hello_world():
    navigator.ui.text_success("Hello World!")

@nav.route('Hello Name', "A more advanced Hello World")
def hello_name():
    name = navigator.ui.prompt("What is your name?")
    navigator.ui.text_success("Hello {}!".format(name))

if __name__ == "__main__":
    nav.run()

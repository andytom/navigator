import six
# TODO - Add doc strings


#-----------------------------------------------------------------------------#
# Helper Functions
#-----------------------------------------------------------------------------#
def _prompt_for_input(message):
    text_prompt(message, ' ')
    return six.moves.input()


#-----------------------------------------------------------------------------#
# Text Output
#-----------------------------------------------------------------------------#
def _text_out(colour_code, message, end):
    six.print_("\x1b[{}m{}\x1b[0m".format(colour_code, message), end=end)


def text_prompt(message, end="\n"):
    _text_out(33, message, end)


def text_info(message, end="\n"):
    _text_out(37, message, end)


def text_success(message, end="\n"):
    _text_out(32, message, end)


def text_error(message, end="\n"):
    _text_out(31, message, end)


#-----------------------------------------------------------------------------#
# User Input
#-----------------------------------------------------------------------------#
def prompt(message, expected_type='str', default=None):
    while True:
        raw = _prompt_for_input(message)
        if default is not None and not raw:
            raw = default
        if raw and expected_type == 'int':
            try:
                return int(raw)
            except ValueError:
                text_error('Invalid Input (Expected a Number)')
        elif raw:
            return raw
        else:
            text_error('Input required')


def confirm(message, default=False):
    if default:
        default_formatted = "[Yn]"
        default = "y"
    else:
        default_formatted = "[yN]"
        default = "n"
    message = "{} {}:".format(message, default_formatted)
    res = prompt(message, default=default)
    return res.lower().startswith('y')


def choice(message, choices):
    if len(choices) == 1:
        return choices[0][1]
    while True:
        for i, choice in enumerate(choices):
            text_prompt("{} - {}".format(i, choice[0]))
        picked = prompt(message, "int")
        try:
            return choices[picked][1]
        except IndexError:
            text_error("That is not a valid selection")

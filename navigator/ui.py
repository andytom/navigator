import six
# TODO - Add doc strings


#-----------------------------------------------------------------------------#
# Helper Functions
#-----------------------------------------------------------------------------#
def _prompt_for_input(message):
    text_prompt(message, ' ')
    return six.moves.input()


class ColorsFormats(object):
    """
        Enum like class that define possible colours and formats
        and those that are used for the different text ui types.
    """
    # Formats
    bold = 1
    # Foreground colours
    black, red, green, yellow, blue, magenta, cyan, light_grey = range(30, 38)
    dark_grey, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan, white = range(90, 98)
    # Background colours
    bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_magenta, bg_cyan, bg_grey = range(40, 48)
    bg_dark_grey, bg_light_red, bg_light_green, bg_light_yellow, bg_light_blue, bg_light_magenta, bg_light_cyan, bg_white = range(100, 108)
    # Attributes to be used by the ui.text methods
    prompt, info, success, error = yellow, light_grey, green, red


#-----------------------------------------------------------------------------#
# Text Output
#-----------------------------------------------------------------------------#
def _text_out(colour_code, message, end):
    six.print_("\x1b[{}m{}\x1b[0m".format(colour_code, message), end=end)


def text_prompt(message, end="\n"):
    _text_out(ColorsFormats.prompt, message, end)


def text_info(message, end="\n"):
    _text_out(ColorsFormats.info, message, end)


def text_success(message, end="\n"):
    _text_out(ColorsFormats.success, message, end)


def text_error(message, end="\n"):
    _text_out(ColorsFormats.error, message, end)


#-----------------------------------------------------------------------------#
# User Input
#-----------------------------------------------------------------------------#
def prompt(message, expected_type='str', default=None):
    if default is not None:
        message += " [Default: {}]".format(default)
    while True:
        raw = _prompt_for_input(message)
        if default is not None and not raw:
            raw = default
        if (raw or raw == 0)and expected_type == 'int':
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


def choice(message, choices, default=None):
    if len(choices) == 1:
        return choices[0][1]
    while True:
        for i, choice in enumerate(choices):
            text_prompt("  {} - {}".format(i, choice[0]))
        picked = prompt(message, "int", default)
        try:
            if picked < 0:
                raise IndexError()
            return choices[picked][1]
        except IndexError:
            text_error("That is not a valid selection")

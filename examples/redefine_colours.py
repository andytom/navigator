"""
    An example of redefining the ui text colours
"""
from navigator import ui, Navigator


nav = Navigator()


@nav.route("Print", "shows all the colours")
def colours():
    ui.text_prompt("prompt")
    ui.text_info("info")
    ui.text_success("success")
    ui.text_error("error")


@nav.route("Change", "try on some different colour scheme")
def change():
    ui.ColorsFormats.prompt = ui.ColorsFormats.magenta
    ui.ColorsFormats.info = ui.ColorsFormats.aqua
    ui.ColorsFormats.success = ui.ColorsFormats.bg_green
    ui.ColorsFormats.error = ui.ColorsFormats.bg_red


if __name__ == "__main__":
    nav.run()

import reflex as rx
from webPython.components.link_button import link_button

def links() ->rx.Component:
    return rx.vstack(
        link_button("Codifer","https://www.codifer.com"),
        link_button("Sanptec","https://www.sanptec.com")
    )
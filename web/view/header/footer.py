import reflex as rx
from rxconfig import config

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", margin_y="10px"),
        rx.link(
            "HOla LInk",
            href="https:www.google.com",
            is_external=True,
            ),
        rx.text("holaaaaaa"),
         align="center",
    )
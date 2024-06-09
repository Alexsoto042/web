import reflex as rx
from rxconfig import config
from web.view.links.link_button import link_button

def link()-> rx.Component:
    return rx.vstack(
       link_button("hello word", "https://www.amazon.com.mx"),
       link_button("hello word", "https://www.amazon.com.mx"),
       link_button("hello word pppp", "https://www.amazon.com.mx"),
       link_button("hello word", "https://reflex.dev"),
       width="100%"
    )

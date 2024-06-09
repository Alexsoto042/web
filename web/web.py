"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from web.components.nada_bar import nbar
from web.view.header.header import header
from web.view.links.link import link
from web.view.header.footer import footer
import web.style.style as styles



class State(rx.State):
    """The app state."""
    pass

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
   return rx.box(
       nbar(),
       rx.center(
           rx.vstack(
            header(),
            link(),
            
            
            # width="100%",
            margin_y=styles.spacer.DEFAUL
             ),
           
        ),
       
    footer(),
    
)
   





app = rx.App(
    style=styles.BASE_STYLE
    
)
app._compile()
app.add_page(index)

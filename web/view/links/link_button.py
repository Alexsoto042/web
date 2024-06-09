import reflex as rx
from rxconfig import config

def link_button (text: str, url:str)-> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="moon"
                ),
                rx.vstack(
                    rx.text(text,),
                    rx.text(text)
                ),
            ),
            
            color_scheme="red",
            
            ),
         href=url,
         is_external=True,
         width="100%"
        
       
    )
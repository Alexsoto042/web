import reflex as rx
from rxconfig import config

def header()-> rx.Component:
    return rx.avatar(        
        fallback="Rx",
        size="6",
        color_scheme="blue", 
        
    )
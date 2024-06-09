import reflex as rx
from rxconfig import config


def nbar() -> rx.Component:
 return rx.hstack( 
        rx.text(
            "Hola",
            align="center",
            size="6",
            height="40px",
            color="white",
            
            ),
         position="Sticky",
         bg="red"
        
        )
 
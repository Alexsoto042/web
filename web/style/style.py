import reflex as rx
from rxconfig import config
from enum import Enum

#constans
MAX_WIDTH="550 px"

class spacer(Enum):
    SMALL="em"
    DEFAUL="1em"
    BIG="2em"


BASE_STYLE= {
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": spacer.SMALL.value
    }
}
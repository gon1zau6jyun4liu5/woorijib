"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

from .styles import tab_style
from .styles import center_style
from .styles import vstack_style
from .styles import vstack_style2
from .styles import hstack_style
from .styles import link_style2

import pynecone as pc
from .base_state import State
from .page_parts.navibar import navibar

from guwanwoo.pages.son_guwanwoo import sonGuwanwoo


def index():
    """index"""

    return pc.tabs(
        navibar(),
        pc.tab_panels(

            # Components
            pc.tab_panel(
                pc.center(
                    pc.hstack(
                        pc.link(
                            pc.vstack(pc.image(src="papa.ico", height="12em", width="16em"), 
                            pc.heading("아빠 パパ", font_size="1.2em")),
                            href="/",
                            style = link_style2
                        ),
                        pc.link(
                            pc.vstack(pc.image(src="mama.ico", height="12em", width="18em"), 
                            pc.heading("엄마 ママ", font_size="1.2em")),
                            href="/",
                            style = link_style2
                        ),
                        style = hstack_style),
                ),
                pc.center(
                    pc.link(
                        pc.vstack(pc.image(src="guwanwoo.ico", height="12em", width="16em"), 
                        pc.heading("관우 寛祐", font_size="1.2em")),
                        href="/songuwanwoo",
                        style = vstack_style2
                    ),
                    style = center_style
                ),
                justify_content = "space-between",
            ),

            # State
            pc.tab_panel(
                pc.text("우리집", color="red")
            ),
            
            # Styling
            pc.tab_panel(
                pc.text("일정", color="red")
            ),            

            # Database
            pc.tab_panel(
                pc.text("가계부", color="red")            
            ),

            # Deploy
            pc.tab_panel(
                pc.text("위키", color="red")
            ),

            # Advanced Guide
            pc.tab_panel(
                pc.text("여행", color="red")
            ),

            # Events Reference
            pc.tab_panel(
                pc.text("Pynecone > Events Reference", color="red")
            ),

            # Gallery
            pc.tab_panel(
                pc.text("Pynecone > Gallery", color="red")
            )
            
            ,style = tab_style
        )
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(sonGuwanwoo, route="songuwanwoo")
app.compile()

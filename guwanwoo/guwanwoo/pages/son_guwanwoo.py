"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

from guwanwoo.styles import tab_style
from guwanwoo.styles import center_style
from guwanwoo.styles import vstack_style
from guwanwoo.styles import vstack_style2
from guwanwoo.styles import hstack_style

import pynecone as pc
from guwanwoo.base_state import State
from guwanwoo.page_parts.navibar import navibar


def sonGuwanwoo():
    """index"""

    return pc.tabs(
        navibar(),
        pc.tab_panels(

            # Components
            pc.tab_panel(
                # pc.html("""<img src="/awesome.gif" alt="gif">"""),
                # pc.image(src="guwanwoo.gif", width="500px", height="auto")

                pc.center(
                    pc.hstack(
                        pc.link(
                            pc.vstack(pc.image(src="guwanwoo.gif", height="12em", width="16em"), 
                            pc.heading("관우 사진", font_size="1.2em")),
                            href="/",
                            # style = link_style2
                        ),
                        pc.link(
                            pc.vstack(pc.image(src="mama.ico", height="12em", width="18em"), 
                            pc.heading("엄마 ママ", font_size="1.2em")),
                            href="/",
                            # style = link_style2
                        ),
                        style = hstack_style),
                ),


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

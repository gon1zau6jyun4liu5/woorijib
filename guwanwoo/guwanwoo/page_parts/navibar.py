import pynecone as pc
from guwanwoo.styles import navibar_style
from guwanwoo.styles import navibar_box_style


def navibar():
    """The navibar."""
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(
                        pc.image(src="favicon.ico", height="3em"), 
                        pc.heading("WooRiJib")
                    ),
                href="/",
            ),

            pc.tab_list(
                pc.tab("우리가족"),
                pc.tab("우리집"),
                pc.tab("일정"),
                pc.tab("가계부"),
                pc.tab("위키"),
                pc.tab("여행"),
                pc.tab("Events Reference"),
                pc.tab("Gallery"),
            ),
            style = navibar_box_style,
        ),
        style = navibar_style
    )


"""
def navibar2(title):
    return pc.box(
        pc.hstack(
            pc.link(
                "● "+ title,
                href="/",
            ),
            style = navibar2_box_style
        ),
        style = navibar2_style
    )
"""
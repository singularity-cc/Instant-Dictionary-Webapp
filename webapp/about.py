import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Our destiny offers not the cup of despair, 
        but the chalice of opportunity. So let us seize it, not in fear, 
        but in gladness.——R.M. Nixon
        """, classes="text-lg")
        return wp



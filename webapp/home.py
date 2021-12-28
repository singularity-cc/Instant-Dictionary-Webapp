import justpy as jp
import webapp.layout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = webapp.layout.DefaultLayout(a=wp, view="hHh lpR fFf")

        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        I once saw Jazell Barbie Royale
        Do Whitney Houston so well
        I got upset with myself for sneaking 
        Past the cashier 
        After having been patted down. Security frisks you 
        For nothing. They don’t believe in trouble. They don’t 
        Imagine a gun or a blade, though
        Sometimes they make you walk all the way back 
        To the car with the weed you didn’t tuck well.
        No one’s at fault. That’s how they say it
        Where I’m from. Everyone’s got a job. 
        I should have paid. Our women
        Need to perform for the tips they couldn’t earn
        After the state shut down for good reason 
        And too late. We lost so many friends. 
        My buddy Janir swears 
        He still can’t smell his lip balm. Our women need us 
        To call them beautiful 
        Because they are. They’ve done what they must
        To prove it, and how often does any woman get
        To hear the truth? Jazell is so pretty.
        Whitney Houston is dead. No one wore a mask.
        It wasn’t safe, so it wasn’t really free.
        If you don’t watch me, I’ll get by you. I’ll take
        What I’ve been missing. My mother says 
        That’s not how she raised me. I spent 
        A year and a half sure she’d die.
        The women who lip sync for us could die.
        People like to murder them, 
        And almost everyone else wonders
        If they should be dead. Who got dressed looking 
        For safety today? Who got patted down?  My mother 
        Says what we do is sin. But all we do 
        Is party. Even when I’m broke, I can 
        Entertain. You’re going to miss me some day. 
        You’re going to forget the words to your favorite song. 
        You’re going to miss me when I’m gone.   
        """, classes="text-lg")
        return wp



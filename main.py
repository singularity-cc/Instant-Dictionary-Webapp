import justpy as jp
from webapp.about import About
from webapp.home import Home


jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.justpy(port=8001)
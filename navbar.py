# Import Bootstrap from Dash
import dash_bootstrap_components as dbc


# Navigation Bar fucntion
def Navbar():
    navbar = dbc.NavbarSimple(children=[
            dbc.NavItem(dbc.NavLink("Equipos", href='/equipos')),
            dbc.NavItem(dbc.NavLink("Jugadores", href='/jugadores')),
        ],
        brand="Home",
        brand_href="/",
        sticky="top",
        color="light",
        dark=False,
        expand='lg',)
    return navbar

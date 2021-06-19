# Import Bootstrap from Dash
import dash_bootstrap_components as dbc

# Navigation Bar fucntion
def Navbar():
    navbar = dbc.NavbarSimple(children=[
            dbc.NavItem(dbc.NavLink("Equipos", href='/equipos')),
            dbc.NavItem(dbc.NavLink("Jugadores", href='/jugadores')),
            dbc.NavItem(dbc.NavLink("Estadios", href='/estadios')),
            dbc.NavItem(dbc.NavLink("Expectativa de Carrera", href='/expectativa')),
        ],
        brand="Béisbol Analítica",
        brand_href="/",
        sticky="top",
        color="primary",
        dark=False,
        expand='lg',)
    return navbar

import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Schooling", header=True),
            dbc.DropdownMenuItem("Pre-primary enrollment rate (5 Year old)", href="/"),
            dbc.DropdownMenuItem("Pre-primary enrollment rate (3-5 Year old)", href="/enrollment-rate-pre-primary-35"),
            dbc.DropdownMenuItem("Primary net enrollment rate", href="/net-enrollment-primary"),
            dbc.DropdownMenuItem("Secondary net enrollment rate", href="/net-enrollment-secondary"),
            dbc.DropdownMenuItem("Tertiary net enrollment rate", href="/net-enrollment-tertiary"),
            dbc.DropdownMenuItem("Primary completion rate", href="/primary-completion-rate"),
            dbc.DropdownMenuItem("Secondary completion rate", href="/secondary-completion-rate"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Activities and time use", header=True),
            dbc.DropdownMenuItem("Participation in care activities", href="/participation-care-activities"),
            dbc.DropdownMenuItem("Weekly hours allocated to care activities", href="/hours-care-activities"),
            dbc.DropdownMenuItem("Participation in childcare activities", href="/participation-childcare-activities"),
            dbc.DropdownMenuItem("Weekly hours allocated to childcare activities", href="/hours-childcare-activities"),
            dbc.DropdownMenuItem("Youth neither in school nor economically active", href="/youth-neither-school-active"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Test Scores", header=True),
            dbc.DropdownMenuItem("Average score in standardized tests for 3rd grade students", href="/score-3rd"),
            dbc.DropdownMenuItem("Average score in standardized tests for 6th grade students", href="/score-6th"),
            dbc.DropdownMenuItem("Average score in standardized tests for 15 year-old students", href="/score-15"),
            dbc.DropdownMenuItem("Ratio of standardized tests scores for 3rd grade students", href="/ratio-3rd"),
            dbc.DropdownMenuItem("Ratio of standardized tests scores for 6th grade students", href="/ratio-6th"),
            dbc.DropdownMenuItem("Ratio of standardized tests scores for 15 year-old students", href="/ratio-15"),
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores in 3rd grade", href="/women-10-low-3rd"),
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores in 6th grade", href="/women-10-low-6th"),
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores for 15 year-old students", href="/women-high-10-15"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores in 3rd grade", href="/women-10-high-3rd"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores in 6th grade", href="/women-10-high-6th"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores for 15 year-old students", href="/women-10-high-15"),
            dbc.DropdownMenuItem("Percentage of women among 15 year-old functionally-illiterate students", href="/women-illiterate-functionally"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicators",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()
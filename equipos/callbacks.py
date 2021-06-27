
# Dash components, html, and dash tables
from dash.dependencies import Input, Output

# Custom dependencies
from app import app
from commons.functions import create_callback_functions_from_specs
from equipos.specs import lov_specs


for f in create_callback_functions_from_specs(lov_specs):
    exec(f, locals())


'''
@app.callback(
    Output('lov_team', 'options'),
    [Input('lov_majorLeague', 'value'), Input('lov_season', 'value') ]
    )
def set_team_from_majorleague(lov_majorLeagueId=None, lov_seasonId=None):
    filter_cols = { 'majorLeagueId' : lov_majorLeagueId,
              'seasonId' : lov_seasonId
            }

    df = f.filter_df( df = es.lov_specs['lov_team']['dataset'], filter_cols=filter_cols)

    lov = f.create_list_of_values( df, label_col = es.lov_specs['lov_team']['label_col'],  value_col = es.lov_specs['lov_team']['value_col'] )

    return lov
'''

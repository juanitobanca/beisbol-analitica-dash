import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

def create_list_of_values(df, label_col, value_col):
    """
    Create a list of values.

    params:
    * df: Pandas dataframe.
    * label_col: String. Column name to be used as label.
    * value_col: String. Column name to be used as value.
    """
    lov = []
    unique_values = df.drop_duplicates([label_col, value_col])

    for idx, row in unique_values.iterrows():
        lov.append({"label": row[label_col], "value": row[value_col]})

    return lov


def filter_df(df, filter_cols):
    """
    Filter a dataset based on a list of filtering columns.

    * df: Pandas dataframe.
    * filter_cols: List of maps. Filters to be used to filter the dataframe.
    """
    filters = []

    for column, value in filter_cols.items():

        if type(value) is list:

            df = df[df[column].isin(value)]

        else:
            df = df[df[column] == value]

    return df


def create_callback_functions_from_specs(object_specs):

    """
    Document this
    """

    for obj, specs in object_specs.items():

        callback_output_list = []
        callback_input_list = []
        param_input_list = []
        filter_cols_list = []
        functions = []

        if not specs["callback_output"]:
            continue

        for co in specs["callback_output"]:
            callback_output_list.append(
                f"Output( component_id = '{co['component_id']}', component_property = '{co['component_property']}' )"
            )

        for ci in specs["callback_input"]:
            callback_input_list.append(
                f"Input( component_id = '{ci['component_id']}', component_property = '{ci['component_property']}' )"
            )
            param_input_list.append(f"{ci['component_id']}=None")
            filter_cols_list.append(f"'{ci['filter_col']}':{ci['component_id']}")

        callback_output_str = ",".join(callback_output_list)
        callback_input_str = "[" + ",".join(callback_input_list) + "]"
        param_input_str = ",".join(param_input_list)
        filter_cols_str = "{" + ",".join(filter_cols_list) + "}"

        obj_fstring = f"object_specs['{obj}']"
        function = f"@app.callback({callback_output_str}, {callback_input_str})"
        function += f"\ndef {specs['id']}({param_input_str}):"
        function += f"\n\tfilter_cols = {filter_cols_str}"
        function += f"\n\tdf = f.filter_df( df = {obj_fstring}['dataset'], filter_cols=filter_cols )"

        if specs["object_type"] == "lov":
            function += f"""\n\tobj = f.create_list_of_values( df = df
                                    , label_col = {obj_fstring}['label_col']
                                    , value_col = {obj_fstring}['value_col']
                                    )
                        """
        elif specs["object_type"] == "fig":
            function += f"""\n\tobj = f.create_px_figure( df = df
                                    , fig_type = {obj_fstring}['fig_type']
                                    , fig_specs = {obj_fstring}['fig_specs']
                                    )
                        """

        function += f"\n\treturn obj"

        functions.append(function)

    return functions


def create_px_figure(df, fig_type, fig_specs):

    if fig_type == "scatter":
        # px_fig = ff.create_table(df[["seasonId", "majorLeague", "gameDate", "teamName", "winPercentage"]].head(100))
        px_fig = px.line(
            df,
            x=fig_specs["x"],
            y=fig_specs["y"],
            color=fig_specs["color"],
            #title=fig_specs["title"],
            labels=fig_specs["labels"],
        )

        px_fig.update_layout(
            title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},
            autosize=False,
            width=400,
            height=300,
            margin=dict(l=0, r=0, b=2, t=2, pad=0),
            showlegend=False,
        )


    return px_fig

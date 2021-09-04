import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_table as dt

# Custom imports
import commons.data as d


def get_groupingDescription(filters):

    db_groupings = [
        "pitchHand",
        "batSide",
        "positionAbbrev",
        "halfInning",
        "menOnBase",
        "battingTeamId",
        "pitchingTeamId",
        "inning",
        "runnersBeforePlay",
        "outs",
        "majorLeagueId",
        "seasonId",
        "gameType2",
        "venueId",
        "teamId",
        "teamType",
        "playerId",
    ]

    groupingDescription_list = []
    groupingDescription_str = None

    for g in db_groupings:

        if g in filters and filters[g] != "":
            groupingDescription_list.append(g)

    print(groupingDescription_list)

    groupingDescription_str = "_".join(groupingDescription_list)

    return groupingDescription_str.upper()


def create_list_of_values(df, label_col, value_col):
    """
    Create a list of values.

    params:
    * dataset: name of a dataset in data_specs
    * label_col: String. Column name to be used as label.
    * value_col: String. Column name to be used as value.
    """
    lov = []

    unique_values = df.drop_duplicates([label_col, value_col])

    for idx, row in unique_values.iterrows():
        lov.append({"label": row[label_col], "value": row[value_col]})

    return lov


def filter_df(dataset_name, filter_cols, default_filters):
    """
    Filter a dataset based on a list of filtering columns.

    * dataset: name of a dataset in data_specs
    * filter_cols: List of maps. Filters to be used to filter the dataframe.
    """
    df = d.dataset_specs[dataset_name]["dataset"]

    filters = {}

    if default_filters:
        filters = {**filters, **default_filters}

    if filter_cols:
        filters = {**filters, **filter_cols}

    if "groupingDescription" not in filters and "groupingDescription" in df:
        filters["groupingDescription"] = get_groupingDescription(filters)

    print(f"Got Here for dataset {dataset_name}")
    print(filters)

    for column, value in filters.items():

        if type(value) is list:
            print(f"Filtering by {column} : {value}")
            df = df[df[column].isin(value)]

        elif value != "" and value != "dummy":
            print(f"Filtering by {column} : {value}")
            df = df[df[column] == value]

    print(
        f"Length of dataset: {len(df)} for {dataset_name} and default filters: {default_filters}\n"
    )
    print("Returning dataset")

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
        function += f"\n\tdf = f.filter_df( dataset_name = {obj_fstring}['dataset_name'], filter_cols=filter_cols, default_filters = {obj_fstring}['default_filters'])"

        if specs["object_type"] == "lov":
            function += f"""\n\tobj = f.create_list_of_values( df = df
                                    , label_col = {obj_fstring}['label_col']
                                    , value_col = {obj_fstring}['value_col']
                                    )
                        """
            function += f"\n\treturn obj"

        elif specs["object_type"] == "fig":
            function += f"""\n\tobj = f.create_px_figure( df = df
                                    , fig_type = {obj_fstring}['fig_type']
                                    , fig_specs = {obj_fstring}['fig_specs']
                                    )
                        """
            function += f"\n\treturn obj"

        elif specs["object_type"] == "table":
            function += f"\n\treturn df.to_dict('records')"

        print(function)

        functions.append(function)

    return functions


def create_px_figure(df, fig_type, fig_specs):

    if fig_type == "line":
        df2 = df[fig_specs["metrics"] + fig_specs["melt_by"]]
        df2 = df2.melt(
            id_vars=fig_specs["melt_by"], var_name="metrica", value_name="value"
        )
        fig = px.line(
            df2,
            x=fig_specs["x"],
            y="value",
            color="metrica",
            color_discrete_map=fig_specs["color_discrete_map"],
            title=fig_specs["title"],
            labels=fig_specs["labels"],
        )
        print(df2)
        print(fig)

    elif fig_type == "bar":
        fig = px.bar(
            df,
            x=fig_specs["x"],
            y=fig_specs["y"],
            color=fig_specs["color"],
            color_discrete_map=fig_specs["color_discrete_map"],
            labels=fig_specs["labels"],
            title=fig_specs["title"],
        )

    elif fig_type == "star":
        df2 = df[fig_specs["metrics"]].iloc[0, :].reset_index()
        df2.columns = ["theta", "r"]
        fig = px.line_polar(
            df2,
            r="r",
            theta="theta",
            text="r",
            line_close=True,
            range_r=fig_specs["range_r"],
            title=fig_specs["title"],
        )

    elif fig_type == "boxplot":
        fig = px.box(df, y=fig_specs["metrics"], title=fig_specs["title"])

    elif fig_type == "pie":
        df2 = df[fig_specs["metrics"] + fig_specs["melt_by"]]
        df2 = df2.melt(
            id_vars=fig_specs["melt_by"], var_name="metrica", value_name="value"
        )
        fig = px.pie(
            df2,
            values="value",
            names="metrica",
            labels=fig_specs["labels"],
            title=fig_specs["title"],
            hover_data=["metrica"],
            hole=0.5,
        )
        fig.update_traces(
            textposition="outside", textinfo="label,percent", name="Distro"
        )

    elif fig_type == "table":
        print("Returning a table")
        fig = dt.DataTable(
            columns=[
                {"name": name, "id": id} for name, id in fig_specs["columns"].items()
            ],
            data=df.to_dict("records"),
        )

        print([{"name": name, "id": id} for name, id in fig_specs["columns"].items()])
        return fig

    elif fig_type == "heatmap4":

        fig = go.Figure(
            [
                go.Scatter(
                    x=[
                        0,
                        0.1,
                        0.2,
                        0.3,
                        0.4,
                        0.5,
                        0.6,
                        0.7,
                        0.8,
                        0.9,
                        1,
                        1.1,
                        1.2,
                        1.3,
                        1.4,
                        1.5,
                        1.6,
                        1.7,
                        0,
                    ],
                    y=[
                        5,
                        5,
                        5,
                        4.99,
                        4.98,
                        4.97,
                        4.96,
                        4.95,
                        4.94,
                        4.92,
                        4.9,
                        4.88,
                        4.85,
                        4.83,
                        4.8,
                        4.77,
                        4.74,
                        4.7,
                        0,
                    ],
                    fill="toself",
                ),
                go.Scatter(
                    x=[
                        0,
                        1.8,
                        1.9,
                        2,
                        2.1,
                        2.2,
                        2.3,
                        2.4,
                        2.5,
                        2.6,
                        2.7,
                        2.8,
                        2.9,
                        3,
                        3.1,
                        3.2,
                        3.3,
                        3.4,
                        3.5,
                        3.6,
                        0,
                    ],
                    y=[
                        0,
                        4.66,
                        4.62,
                        4.58,
                        4.54,
                        4.49,
                        4.44,
                        4.39,
                        4.33,
                        4.27,
                        4.21,
                        4.14,
                        4.07,
                        4,
                        3.92,
                        3.84,
                        3.76,
                        3.67,
                        3.57,
                        3.47,
                        0,
                    ],
                    fill="toself",
                ),
                go.Scatter(
                    x=[ 0,
-0.1,
-0.2,
-0.3,
-0.4,
-0.5,
-0.6,
-0.7,
-0.8,
-0.9,
-1,
-1.1,
-1.2,
-1.3,
-1.4,
-1.5,
-1.6,
-1.7,
0
                    ],
                    y=[
                        5,
4.74,
4.77,
4.8,
4.83,
4.85,
4.88,
4.9,
4.92,
4.94,
4.95,
4.96,
4.97,
4.98,
4.99,
5,
5,
5,
0
                    ],
                    fill="toself",
                ),
            ]
        )

    fig.update_layout(
        # title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},
        autosize=True,
        # width=400,
        height=fig_specs["height"],
        margin=dict(l=0, r=0, b=0, t=50, pad=0),
        showlegend=fig_specs["showlegend"],
        font=dict(size=9),
        xaxis={"type": "category", "categoryorder": "category ascending"},
        legend_title_text="",
    )

    if fig_specs["orientation"] == "h":
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

    return fig

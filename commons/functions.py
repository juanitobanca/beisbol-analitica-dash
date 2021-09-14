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
                        5,
                        8.4,
                        8.3,
                        8.2,
                        8.1,
                        8.0,
                        7.9,
                        7.8,
                        7.7,
                        7.6,
                        7.5,
                        7.4,
                        7.3,
                        7.2,
                        7.1,
                        7.0,
                        6.9,
                        6.8,
                        6.7,
                        6.6,
                    ],
                    y=[
                        0,
                        3.67,
                        3.76,
                        3.84,
                        3.92,
                        4.0,
                        4.07,
                        4.14,
                        4.21,
                        4.27,
                        4.33,
                        4.39,
                        4.44,
                        4.49,
                        4.54,
                        4.58,
                        4.62,
                        4.66,
                        4.7,
                        4.74,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="blue",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[
                        5,
                        6.6,
                        6.5,
                        6.4,
                        6.3,
                        6.2,
                        6.1,
                        6.0,
                        5.9,
                        5.8,
                        5.7,
                        5.6,
                        5.5,
                        5.4,
                        5.3,
                        5.2,
                        5.1,
                        5.0,
                    ],
                    y=[
                        0,
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
                        5.0,
                        5.0,
                        5.0,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="yellow",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[
                        5,
                        5,
                        4.9,
                        4.8,
                        4.7,
                        4.6,
                        4.5,
                        4.4,
                        4.3,
                        4.2,
                        4.1,
                        4.0,
                        3.9,
                        3.8,
                        3.7,
                        3.6,
                        3.5,
                        3.4,
                        3.3,
                        3.2,
                    ],
                    y=[
                        0,
                        5,
                        5.0,
                        5.0,
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
                        4.66,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="orangered",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[
                        5,
                        3.2,
                        3.1,
                        3.0,
                        2.9,
                        2.8,
                        2.7,
                        2.6,
                        2.5,
                        2.4,
                        2.3,
                        2.2,
                        2.1,
                        2.0,
                        1.9,
                        1.8,
                        1.7,
                        1.6,
                        1.5,
                        5,
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
                        4.0,
                        3.92,
                        3.84,
                        3.76,
                        3.67,
                        3.57,
                        0,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="yellow",
                        size=0.5,
                    ),
                ),
            ]
        )

    elif fig_type == "heatmap8":

        fig = go.Figure(
            [
                go.Scatter(
                    x=[2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 5],
                    y=[4.21, 4.14, 4.07, 4.0, 3.92, 3.84, 3.76, 3.67, 3.57, 0],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="blue",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 5],
                    y=[4.66, 4.62, 4.58, 4.54, 4.49, 4.44, 4.39, 4.33, 4.27, 4.21, 0],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="red",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[
                        4.1,
                        4.0,
                        3.9,
                        3.8,
                        3.7,
                        3.6,
                        3.5,
                        3.4,
                        3.3,
                        3.2,
                        5,
                    ],
                    y=[
                        4.92,
                        4.9,
                        4.88,
                        4.85,
                        4.83,
                        4.8,
                        4.77,
                        4.74,
                        4.7,
                        4.66,
                        0,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="yellow",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[5, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 5],
                    y=[5, 5.0, 5.0, 4.99, 4.98, 4.97, 4.96, 4.95, 4.94, 4.92, 0],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="blue",
                        size=0.5,
                    ),
                ),
                # Half
                go.Scatter(
                    x=[5, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9],
                    y=[0, 5.0, 5.0, 5.0, 4.99, 4.98, 4.97, 4.96, 4.95, 4.94, 4.92],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="red",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[
                        5,
                        5.9,
                        6.0,
                        6.1,
                        6.2,
                        6.3,
                        6.4,
                        6.5,
                        6.6,
                        6.7,
                    ],
                    y=[
                        0,
                        4.92,
                        4.9,
                        4.88,
                        4.85,
                        4.83,
                        4.8,
                        4.77,
                        4.74,
                        4.7,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="blue",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[
                        5,
                        6.7,
                        6.8,
                        6.9,
                        7.0,
                        7.1,
                        7.2,
                        7.3,
                        7.4,
                        7.5,
                    ],
                    y=[
                        0,
                        4.7,
                        4.66,
                        4.62,
                        4.58,
                        4.54,
                        4.49,
                        4.44,
                        4.39,
                        4.33,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="yellow",
                        size=0.5,
                    ),
                ),
                go.Scatter(
                    x=[5, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 5],
                    y=[0, 4.33, 4.27, 4.21, 4.14, 4.07, 4.0, 3.92, 3.84, 3.76, 3.67, 0],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="red",
                        size=0.5,
                    ),
                ),
            ]
        )

    elif fig_type == "contour_heatmap":

        fig = go.Figure(
            [
                go.Scatter(
                    x=[
                        125,
                        18.93,
                        20.93,
                        22.93,
                        24.93,
                        26.93,
                        28.93,
                        30.93,
                        32.93,
                        34.93,
                        36.93,
                        38.93,
                        40.93,
                        42.93,
                        44.93,
                        46.93,
                        48.93,
                        50.93,
                        52.93,
                        54.93,
                        56.93,
                        58.93,
                        60.93,
                        62.93,
                        64.93,
                        66.93,
                        68.93,
                        70.93,
                        72.93,
                        74.93,
                        76.93,
                        78.93,
                        80.93,
                        82.93,
                        84.93,
                        86.93,
                        88.93,
                        90.93,
                        92.93,
                        94.93,
                        96.93,
                        98.93,
                        100.93,
                        102.93,
                        104.93,
                        106.93,
                        108.93,
                        110.93,
                        112.93,
                        114.93,
                        116.93,
                        118.93,
                        120.93,
                        122.93,
                        124.93,
                        126.93,
                        128.93,
                        130.93,
                        132.93,
                        134.93,
                        136.93,
                        138.93,
                        140.93,
                        142.93,
                        144.93,
                        146.93,
                        148.93,
                        150.93,
                        152.93,
                        154.93,
                        156.93,
                        158.93,
                        160.93,
                        162.93,
                        164.93,
                        166.93,
                        168.93,
                        170.93,
                        172.93,
                        174.93,
                        176.93,
                        178.93,
                        180.93,
                        182.93,
                        184.93,
                        186.93,
                        188.93,
                        190.93,
                        192.93,
                        194.93,
                        196.93,
                        198.93,
                        200.93,
                        202.93,
                        204.93,
                        206.93,
                        208.93,
                        210.93,
                        212.93,
                        214.93,
                        216.93,
                        218.93,
                        220.93,
                        222.93,
                        224.93,
                        226.93,
                        228.93,
                        230.93,
                        125,
                    ],
                    y=[
                        43,
                        149.07,
                        151.03,
                        152.92,
                        154.74,
                        156.5,
                        158.2,
                        159.84,
                        161.42,
                        162.95,
                        164.43,
                        165.85,
                        167.23,
                        168.56,
                        169.84,
                        171.08,
                        172.28,
                        173.44,
                        174.55,
                        175.63,
                        176.67,
                        177.67,
                        178.63,
                        179.56,
                        180.45,
                        181.31,
                        182.13,
                        182.92,
                        183.67,
                        184.4,
                        185.09,
                        185.75,
                        186.38,
                        186.98,
                        187.55,
                        188.09,
                        188.6,
                        189.08,
                        189.53,
                        189.96,
                        190.35,
                        190.72,
                        191.06,
                        191.37,
                        191.65,
                        191.91,
                        192.14,
                        192.34,
                        192.51,
                        192.66,
                        192.78,
                        192.88,
                        192.94,
                        192.99,
                        193.0,
                        192.99,
                        192.95,
                        192.88,
                        192.79,
                        192.67,
                        192.52,
                        192.35,
                        192.15,
                        191.92,
                        191.67,
                        191.39,
                        191.08,
                        190.74,
                        190.38,
                        189.98,
                        189.56,
                        189.11,
                        188.63,
                        188.12,
                        187.59,
                        187.02,
                        186.42,
                        185.79,
                        185.13,
                        184.44,
                        183.72,
                        182.97,
                        182.18,
                        181.36,
                        180.51,
                        179.62,
                        178.69,
                        177.73,
                        176.73,
                        175.7,
                        174.63,
                        173.51,
                        172.36,
                        171.17,
                        169.93,
                        168.65,
                        167.32,
                        165.94,
                        164.52,
                        163.05,
                        161.52,
                        159.95,
                        158.31,
                        156.62,
                        154.86,
                        153.04,
                        151.16,
                        149.2,
                        43,
                    ],
                    #fill="toself",
                    #mode="markers",
                    #marker=dict(
                    #    color="red",
                    #    size=0.5,
                    #),
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

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
    print(f"Dataset name: {dataset_name}: {d.dataset_specs[dataset_name]['path']}")

    if d.dataset_specs[dataset_name]["format"] == "csv":

        df = pd.read_csv(d.dataset_specs[dataset_name]["path"])

        print(f"Dataset name: {dataset_name}. Length: {len(df)}")

        if d.dataset_specs[dataset_name]["column_renamings"]:
            df = df.rename(columns=d.dataset_specs[dataset_name]["column_renamings"])
    else:

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

        elif value and value != "dummy":
            print(f"Filtering by {column} : {value}")
            df = df[df[column] == value]

        print(f"Dataset length: {len(df)}")

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

    elif fig_type == "contour":
        print(df.columns)
        fig = go.Figure(
            [ go.Histogram2dContour(
                x=df["coordX"],
                y=df["coordY"],
                colorscale="Hot",
                showscale=False,
                reversescale=True
            ),
            go.Scatter(
                    x=[
                        125,
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                        26,
                        27,
                        28,
                        29,
                        30,
                        31,
                        32,
                        33,
                        34,
                        35,
                        36,
                        37,
                        38,
                        39,
                        40,
                        41,
                        42,
                        43,
                        44,
                        45,
                        46,
                        47,
                        48,
                        49,
                        50,
                        51,
                        52,
                        53,
                        54,
                        55,
                        56,
                        57,
                        58,
                        59,
                        60,
                        61,
                        62,
                        63,
                        64,
                        65,
                        66,
                        67,
                        68,
                        69,
                        70,
                        71,
                        72,
                        73,
                        74,
                        75,
                        76,
                        77,
                        78,
                        79,
                        80,
                        81,
                        82,
                        83,
                        84,
                        85,
                        86,
                        87,
                        88,
                        89,
                        90,
                        91,
                        92,
                        93,
                        94,
                        95,
                        96,
                        97,
                        98,
                        99,
                        100,
                        101,
                        102,
                        103,
                        104,
                        105,
                        106,
                        107,
                        108,
                        109,
                        110,
                        111,
                        112,
                        113,
                        114,
                        115,
                        116,
                        117,
                        118,
                        119,
                        120,
                        121,
                        122,
                        123,
                        124,
                        125,
                        126,
                        127,
                        128,
                        129,
                        130,
                        131,
                        132,
                        133,
                        134,
                        135,
                        136,
                        137,
                        138,
                        139,
                        140,
                        141,
                        142,
                        143,
                        144,
                        145,
                        146,
                        147,
                        148,
                        149,
                        150,
                        151,
                        152,
                        153,
                        154,
                        155,
                        156,
                        157,
                        158,
                        159,
                        160,
                        161,
                        162,
                        163,
                        164,
                        165,
                        166,
                        167,
                        168,
                        169,
                        170,
                        171,
                        172,
                        173,
                        174,
                        175,
                        176,
                        177,
                        178,
                        179,
                        180,
                        181,
                        182,
                        183,
                        184,
                        185,
                        186,
                        187,
                        188,
                        189,
                        190,
                        191,
                        192,
                        193,
                        194,
                        195,
                        196,
                        197,
                        198,
                        199,
                        200,
                        201,
                        202,
                        203,
                        204,
                        205,
                        206,
                        207,
                        208,
                        209,
                        210,
                        211,
                        212,
                        213,
                        214,
                        215,
                        216,
                        217,
                        218,
                        219,
                        220,
                        221,
                        222,
                        223,
                        224,
                        225,
                        226,
                        227,
                        228,
                        229,
                        230,
                        125,
                    ],
                    y=[
                        43,
                        149,
                        150,
                        151,
                        152,
                        152,
                        153,
                        154,
                        155,
                        156,
                        157,
                        158,
                        159,
                        159,
                        160,
                        161,
                        162,
                        163,
                        163,
                        164,
                        165,
                        165,
                        166,
                        167,
                        167,
                        168,
                        169,
                        169,
                        170,
                        171,
                        171,
                        172,
                        172,
                        173,
                        174,
                        174,
                        175,
                        175,
                        176,
                        176,
                        177,
                        177,
                        178,
                        178,
                        179,
                        179,
                        180,
                        180,
                        180,
                        181,
                        181,
                        182,
                        182,
                        182,
                        183,
                        183,
                        184,
                        184,
                        184,
                        185,
                        185,
                        185,
                        186,
                        186,
                        186,
                        187,
                        187,
                        187,
                        187,
                        188,
                        188,
                        188,
                        188,
                        189,
                        189,
                        189,
                        189,
                        189,
                        190,
                        190,
                        190,
                        190,
                        190,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        193,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        190,
                        190,
                        190,
                        190,
                        190,
                        189,
                        189,
                        189,
                        189,
                        189,
                        188,
                        188,
                        188,
                        188,
                        187,
                        187,
                        187,
                        187,
                        186,
                        186,
                        186,
                        185,
                        185,
                        185,
                        184,
                        184,
                        184,
                        183,
                        183,
                        182,
                        182,
                        182,
                        181,
                        181,
                        180,
                        180,
                        180,
                        179,
                        179,
                        178,
                        178,
                        177,
                        177,
                        176,
                        176,
                        175,
                        175,
                        174,
                        174,
                        173,
                        172,
                        172,
                        171,
                        171,
                        170,
                        169,
                        169,
                        168,
                        167,
                        167,
                        166,
                        165,
                        165,
                        164,
                        163,
                        163,
                        162,
                        161,
                        160,
                        159,
                        159,
                        158,
                        157,
                        156,
                        155,
                        154,
                        153,
                        152,
                        152,
                        151,
                        150,
                        43,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="limegreen",
                        size=0.5,
                    ),
                ),
            ]
        )

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
                        19,
                        20,
                        21,
                        22,
                        23,
                        24,
                        25,
                        26,
                        27,
                        28,
                        29,
                        30,
                        31,
                        32,
                        33,
                        34,
                        35,
                        36,
                        37,
                        38,
                        39,
                        40,
                        41,
                        42,
                        43,
                        44,
                        45,
                        46,
                        47,
                        48,
                        49,
                        50,
                        51,
                        52,
                        53,
                        54,
                        55,
                        56,
                        57,
                        58,
                        59,
                        60,
                        61,
                        62,
                        63,
                        64,
                        65,
                        66,
                        67,
                        68,
                        69,
                        70,
                        71,
                        72,
                        73,
                        74,
                        75,
                        76,
                        77,
                        78,
                        79,
                        80,
                        81,
                        82,
                        83,
                        84,
                        85,
                        86,
                        87,
                        88,
                        89,
                        90,
                        91,
                        92,
                        93,
                        94,
                        95,
                        96,
                        97,
                        98,
                        99,
                        100,
                        101,
                        102,
                        103,
                        104,
                        105,
                        106,
                        107,
                        108,
                        109,
                        110,
                        111,
                        112,
                        113,
                        114,
                        115,
                        116,
                        117,
                        118,
                        119,
                        120,
                        121,
                        122,
                        123,
                        124,
                        125,
                        126,
                        127,
                        128,
                        129,
                        130,
                        131,
                        132,
                        133,
                        134,
                        135,
                        136,
                        137,
                        138,
                        139,
                        140,
                        141,
                        142,
                        143,
                        144,
                        145,
                        146,
                        147,
                        148,
                        149,
                        150,
                        151,
                        152,
                        153,
                        154,
                        155,
                        156,
                        157,
                        158,
                        159,
                        160,
                        161,
                        162,
                        163,
                        164,
                        165,
                        166,
                        167,
                        168,
                        169,
                        170,
                        171,
                        172,
                        173,
                        174,
                        175,
                        176,
                        177,
                        178,
                        179,
                        180,
                        181,
                        182,
                        183,
                        184,
                        185,
                        186,
                        187,
                        188,
                        189,
                        190,
                        191,
                        192,
                        193,
                        194,
                        195,
                        196,
                        197,
                        198,
                        199,
                        200,
                        201,
                        202,
                        203,
                        204,
                        205,
                        206,
                        207,
                        208,
                        209,
                        210,
                        211,
                        212,
                        213,
                        214,
                        215,
                        216,
                        217,
                        218,
                        219,
                        220,
                        221,
                        222,
                        223,
                        224,
                        225,
                        226,
                        227,
                        228,
                        229,
                        230,
                        125,
                    ],
                    y=[
                        43,
                        149,
                        150,
                        151,
                        152,
                        152,
                        153,
                        154,
                        155,
                        156,
                        157,
                        158,
                        159,
                        159,
                        160,
                        161,
                        162,
                        163,
                        163,
                        164,
                        165,
                        165,
                        166,
                        167,
                        167,
                        168,
                        169,
                        169,
                        170,
                        171,
                        171,
                        172,
                        172,
                        173,
                        174,
                        174,
                        175,
                        175,
                        176,
                        176,
                        177,
                        177,
                        178,
                        178,
                        179,
                        179,
                        180,
                        180,
                        180,
                        181,
                        181,
                        182,
                        182,
                        182,
                        183,
                        183,
                        184,
                        184,
                        184,
                        185,
                        185,
                        185,
                        186,
                        186,
                        186,
                        187,
                        187,
                        187,
                        187,
                        188,
                        188,
                        188,
                        188,
                        189,
                        189,
                        189,
                        189,
                        189,
                        190,
                        190,
                        190,
                        190,
                        190,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        193,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        192,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        191,
                        190,
                        190,
                        190,
                        190,
                        190,
                        189,
                        189,
                        189,
                        189,
                        189,
                        188,
                        188,
                        188,
                        188,
                        187,
                        187,
                        187,
                        187,
                        186,
                        186,
                        186,
                        185,
                        185,
                        185,
                        184,
                        184,
                        184,
                        183,
                        183,
                        182,
                        182,
                        182,
                        181,
                        181,
                        180,
                        180,
                        180,
                        179,
                        179,
                        178,
                        178,
                        177,
                        177,
                        176,
                        176,
                        175,
                        175,
                        174,
                        174,
                        173,
                        172,
                        172,
                        171,
                        171,
                        170,
                        169,
                        169,
                        168,
                        167,
                        167,
                        166,
                        165,
                        165,
                        164,
                        163,
                        163,
                        162,
                        161,
                        160,
                        159,
                        159,
                        158,
                        157,
                        156,
                        155,
                        154,
                        153,
                        152,
                        152,
                        151,
                        150,
                        43,
                    ],
                    fill="toself",
                    mode="markers",
                    marker=dict(
                        color="limegreen",
                        size=0.5,
                    ),
                ),
            ]
        )

    if fig_type == "contour_heatmap" or fig_type == 'contour':

        print("Adding Layout for Contour")

        fig.update_layout(
            # title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},
            autosize=True,
            # width=400,
            height=fig_specs["height"],
            margin=dict(l=0, r=0, b=0, t=50, pad=0),
            showlegend=fig_specs["showlegend"],
            font=dict(size=9),
            legend_title_text="",
        )

    else:
        print("Adding Layout")

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
        print("Orientation H")
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
    elif fig_specs["orientation"] == "v":
        print("Orientation V")

    print("Returning FIG")

    return fig

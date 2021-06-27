import pandas as pd


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

        if value:
            df = df[df[column] == value]

    return df


def create_callback_functions_from_specs( lov_specs ):

    callback_output_list = []
    callback_input_list = []
    param_input_list = []
    filter_cols_list = []
    functions = []

    for (lov, specs) in lov_specs.items():

        if not specs['callback_output']:
            continue

        for co in specs["callback_output"]:
            callback_output_list.append(f"Ouput( component_id = {co['component_id']}, component_property = {co['component_property']} )")

        for ci in specs["callback_input"]:
            callback_input_list.append(f"Input( component_id = {ci['component_id']}, component_property = {ci['component_property']} )")
            param_input_list.append(f"{ci['component_id']}=None")
            filter_cols_list.append(f"'{ci['component_id']}':{ci['filter_col']}")


        callback_output_str = ','.join(callback_output_list)
        callback_input_str = '[' + ','.join(callback_input_list) + ']'
        param_input_str = ','.join(param_input_list)
        filter_cols_str = '{' + ','.join(filter_cols_list) + '}'

        functions.append( f"""
    @app.callback({callback_output_str}, {callback_input_str})
    def {specs['id']}({param_input_str}):
            filter_cols = { filter_cols_str }
            df = f.filter_df( df = es.lov_specs['lov_team']['dataset'], filter_cols=filter_cols )
            lov = f.create_list_of_values( df = df
                                        , label_col = es.lov_specs['lov_team']['label_col']
                                        , value_col = es.lov_specs['lov_team']['value_col']
                                        )
            return lov
        """)

    return functions

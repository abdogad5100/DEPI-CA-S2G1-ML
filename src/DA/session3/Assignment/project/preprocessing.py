from pathlib import Path
import pandas as pd


def Read_data_file(file_path: str) -> pd.DataFrame:
    """
    Read a CSV data file and return it as a Pandas DataFrame.

    Parameters
    ----------
    file_path : str
        The path to the CSV file.

    Returns
    -------
    pd.DataFrame
        The data loaded from the CSV file.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the path points to a directory instead of a file.
    RuntimeError
        If an error occurs while reading the file.
    """

    path = Path(file_path)

    # Check if the file exists
    if not path.exists():
        raise FileNotFoundError(
            f"File not found. Please check the path: {file_path}"
        )

    # Check if the path is actually a file
    if not path.is_file():
        raise ValueError(
            f"The provided path is not a file: {file_path}"
        )

    try:
        df = pd.read_csv(path)
        return df

    except Exception as e:
        raise RuntimeError(
            f"An error occurred while reading the file: {e}"
        ) from e


def Check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Display the structure and basic information of each column.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame to analyze.

    Returns
    -------
    pd.DataFrame
        A transposed DataFrame containing each column's:
        - Column name
        - Data type
        - Number of unique values

    Raises
    ------
    TypeError
        If df is not a Pandas DataFrame.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a Pandas DataFrame.")

    result = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Unique Values": df.nunique()
    })

    return result.T
def Drop_unnecessary_features(
    df: pd.DataFrame,
    cols_to_drop: list[str]
) -> pd.DataFrame:
    """
    Drop unnecessary columns from a Pandas DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame.

    cols_to_drop : list[str]
        A list containing the names of columns to remove.

    Returns
    -------
    pd.DataFrame
        A new DataFrame with the specified columns removed.

    Raises
    ------
    TypeError
        If df is not a Pandas DataFrame or cols_to_drop is not a list.

    ValueError
        If one or more columns do not exist in the DataFrame.
    """

    # Validate DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a Pandas DataFrame.")

    # Validate columns list
    if not isinstance(cols_to_drop, list):
        raise TypeError("cols_to_drop must be a list of column names.")

    # Check if all columns exist
    missing_cols = [col for col in cols_to_drop if col not in df.columns]

    if missing_cols:
        raise ValueError(
            f"The following columns do not exist in the DataFrame: {missing_cols}"
        )

    # Drop columns and return a new DataFrame
    return df.drop(columns=cols_to_drop)    

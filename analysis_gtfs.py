import pandas as pd


# Load dataset and converts it in a dataframe (.csv file)
def load_dataset(url):
    """
    Load dataset on web page and converts it in a dataframe.

    - param(s):
        url: dataset url.

    - return:
        df: dataframe from the dataset.
    """

    # Load dataset
    df = pd.read_csv(url)

    return df

# Dataset url - hard coded
url = "https://data.gov.ie/dataset/84226d19-33ce-4516-a810-b021b418f4c3/resource/956bf826-9487-48eb-ada2-9bee199f93af/download/operator-gtfs-files.csv"

# Convert dataset in a dataframe
df = load_dataset(url)
print(df)

# Convert "Last Updated" series from str type to datetime type
df["Last Updated"] = pd.to_datetime(df["Last Updated"])

# Order values from dates using serie "Last Updated"
# Ascending=True is equal to ascending order. That is default.
# na_position="last" makes that null values are put in the last place on dataframe. For this, we have to know that "first" is default.
df_sorted_dates = df.sort_values(by=["Last Updated", "Operator"], ascending=True, na_position="last")
print(df_sorted_dates)

# Convert "Last Updated" series from datetime type to str type, converting the numeric month to long date (month)
df_sorted_dates["Last Updated"] = df_sorted_dates["Last Updated"].dt.strftime("%d %B, %Y")
print(df_sorted_dates)

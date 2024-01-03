import os
import sys
import pandas as pd

def read_csv_from_parent_folder(csv_filename= 'universal_top_spotify_songs.csv', parent_folder='..', subfolder='raw_data'):
    """
    Read a CSV file located in another folder relative to the script's location.

    Parameters:
    - csv_filename (str): The name of the CSV file to read.
    - parent_folder (str): The relative path to the parent folder (default: '..').
    - subfolder (str): The name of a subfolder within the parent folder (default: '').

    Returns:
    - pd.DataFrame: A Pandas DataFrame containing the CSV data.
    """
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Construct the path to the CSV file
    file_path = os.path.join(current_dir, parent_folder, subfolder, csv_filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    return df

def top_what(row):
    if row.daily_rank <= 5:
        cat = 'top5'
    elif row.daily_rank <= 10:
        cat = 'top10'
    elif row.daily_rank <= 20:
        cat = 'top20'
    else:
        cat = 'average'
    return row.country + '_' + cat

def clean_data(df):
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    df['target']=df.apply(top_what, axis = 1)
    df = df[['popularity', 'is_explicit', 'duration_ms', 'danceability', 'energy', 'key', 'loudness',
       'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'time_signature', 'target']]
    return df

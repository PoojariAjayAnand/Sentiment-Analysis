import pandas as pd

def load_dataset(path):
    df = pd.read_csv("D:\Sentiment Analysis\hotel-reviews.csv")
    string_to_int_map = {'happy': 1, 'not happy': 0}
    df['Ratings'] = df['Is_Response'].map(string_to_int_map)
    data=df[['Description','Ratings']]
    return data

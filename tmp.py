import json
import pandas as pd
import requests
from io import StringIO


def get_from_url(url):
    # Open the link and get the content
    s = requests.get(url).content
    # Convert the bytes into a dataframe
    df = pd.read_csv(StringIO(s.decode('utf-8')))
    return df

url_cities = "https://raw.githubusercontent.com/andrea-cola/support_files/main/worldcities.csv"
a = json.loads(get_from_url(url_cities).to_json(orient="records"))
url_ateco = "https://raw.githubusercontent.com/AlessandroArtoni/codici_ateco/master/ateco.csv"
b = json.loads(get_from_url(url_ateco).to_json(orient="records"))





import pandas as pd

data = pd.read_csv('c:/path_to_data/file.csv')

from pycaret.datasets import get_data

data = get_data('juice')

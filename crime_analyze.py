'''This file is a sample python script to test the template and environement'''

import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px

df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

df['TimeOccHr'] = df['TIME OCC']//100 + df['TIME OCC']%100/60

display(df.describe())
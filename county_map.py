from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_excel('data_nov2020.xlsx', sheet_name='data_nov2020')


import plotly.express as px

df['FIPS_Code'] = df['FIPS_Code'].apply(lambda x: '{0:0>5}'.format(x))

# print(df.head())

fig = px.choropleth_mapbox(df, geojson=counties, locations='FIPS_Code', color='County_Penetration',
                           color_continuous_scale="Viridis",
                           range_color=(0, 0.65),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                        #    labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
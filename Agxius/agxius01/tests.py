from django.test import TestCase
# Create your tests here.
# https://docs.mapbox.com/mapbox-gl-js/example/geojson-polygon/









import pandas as pd



# add json for token    config,json
#
#     remove unness files
#
#     rename usefull files
#
# web page tab name

# var names recheck signifcnt meanfl


signup4.html
profile
dash
login3
login4.html
login3
profile.html
dash2.html









df = pd.read_excel('C:/Users/HP/Downloads/data.xlsx')
datalen = df.shape[0]


dateafter=pd.to_datetime('2020-11-01')
print(dateafter)

df.loc[(df['e_dept'] == 'Business') & (df['e_date'] > dateafter) | (df['e_dept'] == 'Cloud') & (df['e_date'] >= dateafter), 'e_dept'] = 'Cloud/Business'


print(df)


# [
# [[-91.85147563427773, 42.76623806202218], [-91.85730829616445, 42.761955981364025], [-91.86056772486606, 42.76560836284088], [-91.85902378495479, 42.76963832699269], [-91.85147563427773, 42.76623806202218]],[[-91.89762228273405, 42.77996391340079], [-91.88166823698518, 42.76472677323355], [-91.90105326031433, 42.76371922689168], [-91.90637127556396, 42.775305020493704], [-91.89762228273405, 42.77996391340079]]
#
#
# ]
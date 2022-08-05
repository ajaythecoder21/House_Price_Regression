import streamlit as sl

import pandas as pd
import xgboost as xgb

sl.title('Hello World!')
sl.write(""""
# Do you want to buy a House?
Enter your House Specs

""")

sl.write("""
## Select The Area
""")
area = sl.slider("Select the area", 0, 100000, 0)

sl.write("""
## Select the Number of Bedrooms

""")

bedrooms = sl.radio("Pick the number of bedrooms", [1, 2, 3, 4])

sl.write("""
## Select the Number of Bathrooms

""")

bathrooms = sl.radio("Pick the number of bathrooms", [1, 2, 3, 4])


sl.write("""
## Select the Number of Stories

""")

stories = sl.radio("Pick the number of stories", [1, 2, 3, 4])


sl.write("""
## Select whether or not there is Parking!
""")

parking = sl.selectbox("Pick whether you need parking", [True, False])

sl.write("""
## Select whether there should be air conditiong
""")

ac = sl.selectbox("Pick whether there should be air conditioning", [True, False])

sl.write("""
## Select whether there should be guest room
""")
gr = sl.selectbox("Pick whether there should be guest room", [True, False])

sl.write("""
Select whether there should be main road"
""")

mr = sl.selectbox("Pick whether there should be main road", [True, False])


sl.write("""
## Select whether there should be a basement
""")

basement = sl.selectbox("Pick whether there should be a basement", [True, False])



sl.write("""
## Select whether there should be hot water heating
""")

hwh = sl.selectbox("Pick whether there should be hot water heating", [True, False])


sl.write("""
## Select whether there should be furnishing status
""")

fs = sl.selectbox("Pick whether there should be furnishing status", [True, False])

features = [area, bedrooms, bathrooms, stories, parking, ac, gr, mr, basement, hwh, fs]
model = xgb.XGBRegressor()
model.load_model('Housing_Price.json')

def predict(area, bedrooms, bathrooms, stories, parking, ac, gr, mr, basement, hwh, fs):
    if parking == True:
        parking = 1
    elif parking == False:
        parking = 0
    if ac == True:
        ac = 1
    elif ac == False:
        ac = 0
    if gr == True:
        gr = 1
    elif gr == False:
        parking = 0
    if mr == True:
        mr = 1
    elif mr == False:
        mr = 0
    if basement == True:
        basement = 1
    elif basement == False:
        basement = 0
    if hwh == True:
        hwh = 1
    elif hwh  == False:
        hwh = 0
    if fs == True:
        fs = 1
    elif fs == False:
        fs = 0
    return model.predict(pd.DataFrame([[area, bedrooms, bathrooms, stories, parking, ac, gr, mr, basement, hwh, fs]], columns=['area', 'bedrooms', 'bathrooms', 'stories', 'parking', 'ac', 'gr', 'mr', 'basement', 'hwh', 'fs']))
if sl.button('Predict'):
    price = predict(area, bedrooms, bathrooms, stories, parking, ac, gr, mr, basement, hwh, fs)
    sl.success(price[0])
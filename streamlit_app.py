import streamlit

streamlit.title('My parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('ð¥£  omega 3 &Blueberry Oatmeal')
streamlit.text('ð¥ Kale, Spinach & Rocket Smoothie')
streamlit.text(	'ð HArd-Boiled Free-Range Egg')
streamlit.text('ð¥ðavocado & sandwich')

streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)






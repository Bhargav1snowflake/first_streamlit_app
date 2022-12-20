import streamlit

streamlit.title('My parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣  omega 3 &Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(	'🐔 HArd-Boiled Free-Range Egg')
streamlit.text('🥑🍞avocado & sandwich')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

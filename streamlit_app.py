import streamlit
import pandas
import requests
streamlit.title('My Mom s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text( '🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text( '🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text( '🐔 Hard-Boiled Free Range Egg')
streamlit.text( '🥑🍞 Avocado Toast ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)

#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_To_Show= my_fruit_list.loc[fruits_selected]
#Display the table on the page
streamlit.dataframe(fruits_To_Show)


streamlit.header('Fruityvice Fruit Advice !')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response= requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")
#streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


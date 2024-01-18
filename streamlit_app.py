import streamlit
import pandas
streamlit.title('My Mom s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text( '🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text( '🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text( '🐔 Hard-Boiled Free Range Egg')
streamlit.text( '🥑🍞 Avocado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_first_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_first_list)

#Choose the Fruit Name Column as the Index
my_first_list = my_first_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect ("Pick some fruits:", list(my_first_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the table
#streamlit.dataframe(my_first_list)

streamlit.dataframe(fruits_to_show)



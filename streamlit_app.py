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

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect ("Pick some fruits:", list(my_first_list.index))
#Display the table
streamlit.dataframe(my_first_list)



import streamlit as st

st.title('Largest of 3 numbers')

# Define a function to take 3 numbers as parameters
def max_of_three(a, b, c):
  # Compare the first two numbers and store the bigger one in a variable
  max = a if a > b else b
  # Compare the variable with the third number and return the bigger one
  return max if max > c else c

# Ask the user to enter 3 numbers separated by commas
#numbers = input("Enter 3 numbers separated by commas: ")

# Split the input string by commas and convert each element to a float
#a, b, c = map(float, numbers.split(","))

a = st.number_input("Enter 1st number")
b = st.number_input("Enter 2nd number")
c = st.number_input("Enter 3rd number")


# Call the function and print the result
result = max_of_three(a, b, c)

st.text("Largest of 3 numbers: {}".format(result))


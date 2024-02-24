 python
def check_even_odd(number):
  """
  This function checks if a given number is even or odd.

  Args:
    number: The number to be checked.

  Returns:
    True if the number is even, False otherwise.
  """

  # Check if the number is divisible by 2.
  if number % 2 == 0:
    return True
  else:
    return False


# Get the number from the user.
number = int(input("Enter a number: "))

# Check if the number is even or odd.
if check_even_odd(number):
  print(f"{number} is even.")
else:
  print(f"{number} is odd.")

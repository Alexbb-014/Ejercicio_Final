def sum_even_numbers(lst):
    """
    Function to calculate the sum of even numbers in a list.
    
    Parameters:
        lst (list): A list of integers.
        
    Returns:
        int: The sum of even numbers in the list.
    """
    total_sum = 0
    for number in lst:
        if number % 2 == 0:
            total_sum += number
    return total_sum

def main():
    """
    Main function to interact with the user and execute the program.
    """
    print('Welcome to Alexis Calculator!')
    print("Catholic University Luis Amigo")
    print("Please enter some numbers separated by spaces.")

    # Ask the user to input numbers to form the list
    numbers = input("Enter the numbers separated by spaces: ").split()

    # Convert the input numbers to integers
    numbers = [int(number) for number in numbers]

    # Display the list entered by the user
    print("The entered list is:", numbers)

    # Calculate the sum of even numbers in the list
    result = sum_even_numbers(numbers)
    print("The sum of even numbers in the list is:", result)

if __name__== "__main__":
    main()

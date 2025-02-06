# Problem 1: Write a program that reverses the input of the user. Use a string method in displaying the text like str[2:5].
# Example:
# Input: hello
# Output: olleh

def reverse_input(word_reverse_input):
    return word_reverse_input[::-1]

user_input = input("Input: ")
reversed_string = reverse_input(user_input)
print(f"Output: {reversed_string}")


# Problem 2: Write a program that converts a user input to a list, and prints the string as a list.
# Example:      
# Input a String: Python123
# Output in list: [‘P’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’, ‘1’, ‘2’, ‘3’] 

def string_to_list(word_list_input):
    return list(word_list_input)

user_input = input("Input a string: ")
string_list = string_to_list(user_input)
print(f"Output in list: {string_list}")


# Problem 3: Write a program to input any string value and print the reverse value using a String method. 
# Example:  
#Enter a String: Python Programming
#Output: Programming Python 

def reverse_words(wholeword_reverse_input):
    words = wholeword_reverse_input.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

user_input = input("Enter a string: ")
reversed_word_order = reverse_words(user_input)
print(f"Output: {reversed_word_order}")
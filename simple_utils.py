# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverses the characters in the input string.
    
    Parameters:
        text (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the words in a sentence.
    
    Parameters:
        sentence (str): Input text where words are separated by whitespace.
    
    Returns:
        int: Number of words in the input sentence.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
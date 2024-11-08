# Function to generate an acronym from an input string
def create_acronym(phrase):
    # Split the input string into words
    words = phrase.split()
    
    # Take the first letter of each word, capitalize it, and join them together
    acronym = ''.join([word[0].upper() for word in words])
    
    return acronym

# Main program to run the acronym creator
if __name__ == "_main_":
    print("Welcome to the Acronyms Creator!")
    
    # Get input from the user
    user_input = input("Enter a phrase to create an acronym: ")
    
    # Create and display the acronym
    acronym = create_acronym(user_input)
    print(f"The acronym for '{user_input}' is: {acronym}")
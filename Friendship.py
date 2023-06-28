#Begin Friendship Algorithm from big bang theory

def ask_to_make_friend():
    response = input("Do you want to make a friend? (yes/no): ")
    
    if response.lower() == "yes":
        print("Great! Let's make a new friend.")
        call_person()  # Call the `call_person()` function
    elif response.lower() == "no":
        print("No problem. Maybe next time!")
        # Add your code here for handling the case when the user doesn't want to make a friend
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        # Recursive call to ask the question again
        ask_to_make_friend()

def call_person():
    response = input("Please call the person. Did they pick up the phone? (yes/no): ")
    
    if response.lower() == "yes":
        print("They picked up the phone!")
    elif response.lower() == "no":
        leave_message = input("They didn't pick up the phone. leave a message, wait for them to call back) ")      
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        # Recursive call to ask the question again
        call_person()        
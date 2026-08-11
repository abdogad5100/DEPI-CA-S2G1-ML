from model import get_response

def main_bot():
    print("Chatbot , hi how can i help u?")
    while True:
        user_input=input("User      ").lower()
        response=get_response(user_input)
        print("Chatbot :" ,response)
        if user_input=="goodbye":
            break
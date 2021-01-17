#from create_model import is_concern
import random

class Alecc:
    def __init__(self, message):
        self.message = message

    def response(self):
        # clean up message to all alpha-numeric
        message = self.message
        message = message.strip().lower()
        message = ''.join(e for e in message if e.isalnum())
        # sentiment = is_concern(message)
        sentiment = random.randint(0,1)  # replace with is_concern when ready
        if "hello" or "hi" or "hey" in message:
            response = "Hello! My name is ALECC. It's short for Aggies Love Existential Crisis Chatbots. I might just be a program, but I am a very loved program (... created to remind other people that they are also loved!). Are you here for yourself, or for a friend? Respond with either  'myself' or 'friend'"

        elif "myself" in message:
            response = "In a few sentences, let me know how you are.\n\nYou can always ask me for 'resources' or 'self care ideas' and I'd be happy to send some."
        elif "friend" in message:
            response = "If your friend has a twitter handle "
        elif "selfcare" in message:
            response = "Here are some self care ideas!\n\nListen to an interesting podcast or read your favorite book\n\nJournal your feelings\n\nCreate some art\n\nPlay an online game or watch a show with a pal\n\nThis is my favorite online mini game platform https://backyard.co/ you can invite pals to play with you!\n\nEat something yummy\n\nGo for a walk\n\nStep outside and look at the sky\n\nDo deep breathing exercises"
        elif "resources" in message:
            response = "Here is a link to a bunch of UC Davis mental health support resources: https://eachaggiematters.ucdavis.edu/campus-resources.\n\nAlso these are the numbers to some hotlines:\n\nNational Suicide Prevention Lifeline: 800-273-8255\n\n Suicide Prevention of Yolo County, Davis: (530) 756-5000\n\nIt sounds like you could use some self-care. I can give you examples of self care activities if you’d like :) Just send me a message saying 'self care'!"
        elif "thanks" in message:
            response = "You're welcome! If you'd like to just chat, send me a message starting with 'Yo Alecc!'"
        elif "yoalecc" in message:
            # chat function here
            response = ""
        else:
            if len(message)<50:
                response = "I was unable to understand your message. If you are sharing your feelings, make sure your message is longer than 50 characters and try again. Let me know if you need 'resources', 'self help ideas', or if you want to chat, start your message with 'Yo Alecc'"
            elif sentiment == 0:
                response = "That is so wonderful to hear! My guess is that you're a student. I know school can be stressful. Would you like a list of self care activities? Just send me a message saying 'self care'!"
            else: #sentiment == 1
                response = "It sounds like you aren't doing well. Here is a link to a bunch of UC Davis mental health support resources: https://eachaggiematters.ucdavis.edu/campus-resources.\n\nAlso these are the numbers to some hotlines:\n\nNational Suicide Prevention Lifeline: 800-273-8255\n\n Suicide Prevention of Yolo County, Davis: (530) 756-5000\n\nIt sounds like you could use some self-care. I can give you examples of self care activities if you’d like :) Just send me a message saying 'self care'!"

        final_response = "Message received: "+message+"\nSentiment: "+str(sentiment)+"\nResponse: "+response
        return final_response
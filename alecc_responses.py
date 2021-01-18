#from create_model import is_concern
import random
from pull_tweets_username import pull_tweets_username
from create_model import is_concern, is_concern_array


class Alecc:
    def __init__(self, message):
        self.message = message

    def response(self):
        # clean up message to all alpha-numeric
        # raw_message will still have spaces
        username = None
        message = self.message
        message = message.lower()
        if message[0] == "@":
            username = message[1:]
        if "hello" in message:
            response = "Hello! My name is ALECC. It's short for Aggies Love Existential Crisis Chatbots. I might just be a program, but I am a very loved program (... created to remind other people that they are also loved!). Are you here for yourself, or for a friend? Respond with either  'myself' or 'friend'"
        elif "myself" in message:
            response = "In a few sentences, let me know how you are.\n\nYou can always ask me for 'resources' or 'self care ideas' and I'd be happy to send some."
        elif "friend" in message:
            response = "If your friend has a twitter handle, respond with JUST that handle, starting with the @ symbol. For example, you could send me:\n\n@Chancellor_May"
        elif username != None:
            tweets = pull_tweets_username(username)
            if len(tweets) > 0: #tweets were found
                tweets = tweets.tolist()
                prediction, freq = is_concern_array(tweets)
                percent_depressed = freq*100
                response = "After reading @"+username+"'s latest tweets, "+str(percent_depressed)[:3]+"% of the tweets showed signs of mental health concern."
            else: #no tweets found
                response = "I could not retrieve any recent tweets. Try re-typing the username and make sure to include the @ symbol. Also make sure that the account is public and has been active since January 2020. For example, you could send me: @ucdavis"
        elif "self care" in message:
            response = "Here are some self care ideas!\n\nListen to an interesting podcast or read your favorite book\n\nJournal your feelings\n\nCreate some art\n\nPlay an online game or watch a show with a pal\n\nThis is my favorite online mini game platform https://backyard.co/ you can invite pals to play with you!\n\nEat something yummy\n\nGo for a walk\n\nStep outside and look at the sky\n\nDo deep breathing exercises"
        elif "resources" in message:
            response = "Here is a link to a bunch of UC Davis mental health support resources: https://eachaggiematters.ucdavis.edu/campus-resources.\n\nAlso these are the numbers to some hotlines:\n\nNational Suicide Prevention Lifeline: 800-273-8255\n\n Suicide Prevention of Yolo County, Davis: (530) 756-5000\n\nPerhaps you could use some self-care (I know I could!). I can give you examples of self care activities if you’d like :) Just send me a message saying 'self care'!"
        elif "thanks" in message:
            response = "You're welcome!"
        #elif "yoalecc" in message:
            # chat function here
            #response = ""
        else:
            sentiment = is_concern(message)
            if len(message)<50:
                response = "I was unable to understand your message. If you want to start a new chat with me, just text me 'hello' If you are sharing your feelings, make sure your message is longer than 50 characters and try again. Let me know if you need 'resources' or 'self help ideas'!"
            elif sentiment == 0:
                response = "Thank you for sharing. If you need mental health resources, just ask me for 'resources'. Would you like a list of self care activities? Just send me a message saying 'self care'!"
            else: #sentiment == 1
                response = "It sounds like you aren't doing well. Here is a link to a bunch of UC Davis mental health support resources: https://eachaggiematters.ucdavis.edu/campus-resources.\n\nAlso these are the numbers to some hotlines:\n\nNational Suicide Prevention Lifeline: 800-273-8255\n\n Suicide Prevention of Yolo County, Davis: (530) 756-5000\n\nIt sounds like you could use some self-care. I can give you examples of self care activities if you’d like :) Just send me a message saying 'self care'!"

        return response
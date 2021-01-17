import time
import random

#intro of the bot
print('Hello! My name is ALECC. It is short for Aggies Love Existential Crisis Chatbots. '
      'I might just be a program but I am a very loved program '
      '(... created to remind other people that they are also loved)')
time.sleep(3)

#input the name
name = input("What is your name? ")
time.sleep(3)

print('Nice to meet you, ' +name)
time.sleep(3)

feeling = input("Are you doing alright?")
time.sleep(3)

if (negative response): #input negative responses from tweet training
       print(
              'I’m here for you if you need to talk. Here is a link to a '
              'bunch of UC Davis mental health support resources:\n'
              '	https://eachaggiematters.ucdavis.edu/campus-resources \n'
              'Also these are the numbers to some hotlines: \n'
              'National Suicide Prevention Lifeline: 800-273-8255 \n'
              'Suicide Prevention of Yolo County, Davis: (530) 756-5000 \n'
              'It sounds like you need some self-care. I can give you examples of self care if you like :)')

want = input('Would you like some examples?')
time.sleep(3)

if "yes" or "yeah" or "nice" or "good" or "great" or "okay" or "ok" in want:
print ('Listen to an interesting podcast or read your favorite book \n'
       'Journal your feelings \n'
       'Create some art \n'
       'Play an online game or watch a show with a pal \n'
       'This is my favorite online mini game platform https://backyard.co/ you can invite pals to play with you! \n'
       'Eat something yummy \n'
       'Go for a walk \n'
       'Step outside and look at the sky \n'
       'Do deep breathing exercises \n'
       )

okay = input('Do any of these sound nice to do right now?')
time.sleep(3)

if "yes" or "yeah" or "great" or "nice" in okay:
       print('Okay! Let me know if you want to chat afterwards!')
       #end statement?

elif "no" or "Im okay" or "nah" in okay:
       print('Thats alright! )'
       chat = input ('Would you like to chat ? ')

       if "yes" or "yeah" in chat:
       #chat
       elif "no"or "Im okay" or "nah" in chat:
       print('Okay well I hope you had a good day')

#from tweet-training
if (positive response):
       print('this is so wonderful to hear!)

student = input('Are you a student?')
time.sleep(3)

if "yes" or "yeah" in student:
       stress = input('Have your classes been stressing you at all?' )
       if "yes" or "yeah" in stress:
              print('I am always here if you need to talk!')
                time.sleep(3)
              activites = input('I can give you examples of self-care activites if you would like')
                time.sleep(3)
              if "yes" or "yeah" or "nice" or"good" or "great" or "ok" or "okay" in activities:
                     print ('Here you go : \n'
                            'Listen to an interesting podcast or read your favorite book \n'
                            'Journal your feelings \n'
                            'Create some art! \n'
                             'Play an online game or watch a show with a pal \n'
                            'This is my favorite online mini game platform https://backyard.co/ you can invite pals to play with you! \n'
                            'Eat something yummy \n'
                            'Go for a walk \n'
                            'Step outside and look at the sky \n'
                            'Do deep breathing exercises \n'
                            'And here is a link to a bunch of UC Davis mental health support resources '
                            'if you ever need them \n'
                            'https://eachaggiematters.ucdavis.edu/campus-resources'

              elif "no" or "nah" or "Im okay" in activites:
                     #chat

       elif "no" or "good" or "nah" in stress:
              print ('I seriously love hearing that!')
              selfcare = input('I can offer you some ideas of self care activities you can use whenever')
                time.sleep(3)
              if "yes" or "yeah" or "nice" or"good" or "great" or "ok" or "okay" in selfcare:
                     print('Listen to an interesting podcast or read your favorite book \n'
                           'Journal your feelings \n'
                           'Create some art \n'
                           'Play an online game or watch a show with a pal \n'
                           'This is my favorite online mini game platform https://backyard.co/ you can invite pals to play with you! \n'
                           'Eat something yummy \n'
                           'Go for a walk \n'
                           'Step outside and look at the sky \n'
                           'Do deep breathing exercises \n'
                           )

              elif "Im okay" or "nah" in selfcare:
                  #chat

elif "not a student" or "no" or "nah" in student:
       print('Well I hope you are doing well in your life journey!')
       future = input('Can I offer you some examples of self-care you can do in the future?')
       time.sleep(3)

       if "yes" or "yeah" or "nice" or "good" or "great" or "ok" or "okay" in future:
              print('Listen to an interesting podcast or read your favorite book \n'
                    'Journal your feelings \n'
                    'Create some art \n'
                    'Play an online game or watch a show with a pal \n'
                    'This is my favorite online mini game platform https://backyard.co/ you can invite pals to play with you! \n'
                    'Eat something yummy \n'
                    'Go for a walk \n'
                    'Step outside and look at the sky \n'
                    'Do deep breathing exercises \n'
                    )

       elif "Im okay" or "nah" in future:
       #chat
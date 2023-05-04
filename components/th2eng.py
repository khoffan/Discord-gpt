from googletrans import Translator

# create an instance of the Translator class
translator = Translator()
def th_2_eng(msg):    
    # take user input
    user_input = msg
    # detect the language of the user input
    translator.detect(user_input).lang
    # translate the user input to English
    translation = translator.translate(user_input, dest='en')

    # print the original and translated text
    text = translation.text
    return text


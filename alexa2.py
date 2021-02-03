import speech_recognition as sr
import pyttsx3



    # TODO: if command in list [one,two...] parse string to int for index and rate 
    # Initial setup -> set type of voice, speed, name
    # Turn volume up/ down, 
    # turn rate up/down, play
    # Play some music.

class Assistant:
    # Speech recognizer
    listener = sr.Recognizer()
    # Assistant voice
    engine = pyttsx3.init()
    
    firstCmdWords = []
    secondCmdWords = []
    numbers = {}
    affirmations = []
    voices = engine.getProperty('voices')


    def __init__(self):

        self.numbers = {"one": 0, "two": 1, "three": 2, "four":3, "five":5, "six":5, "seven": 6, "eight":7}
        self.affirmations = ["yes", "sure", "yeah", "ok"]

        

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def setRate(self, rate):
        # Setting voice rate
        rate = self.engine.getProperty('rate')   # getting details of current speaking rate
        #printing current voice rate
        self.engine.setProperty('rate', rate)     # setting up new voice rate

    def configureVoiceType(self):
        self.talk("Would you like to change the voice type")
        self.engine.runAndWait()
        command = self.listen()
        if(not command):
            for i in range(0,3):
                self.talk("Pardon?")
                command = self.listen()
                if(command):
                    break
            if(not command):
                return

        print(command)
        if(any(ele in command for ele in  self.affirmations)):
            self.talk("Select the number of the voice you will like to change to from the ones you will hear now")
            
            for voice in self.voices:
                self.engine.setProperty('voice', voice.id)
                self.talk('The quick brown fox jumped over the lazy dog.')
            self.engine.setProperty('voice', self.voices[0].id)
            self.talk('Now please choose the number of the voice you would prefer') 
            self.engine.runAndWait()

            command = self.listen()

            if(any(ele in command for ele in  self.numbers)):
                isSet = self.setVoice(self.numbers.get(command))
                if(not isSet):
                    command = self.listen()
                    isSet = self.setVoice(self.numbers.get(command))
                    if(not isSet):
                        self.talk('Voice set to default value') 
                        self.engine.setProperty('voice', self.voices[0].id)



    def setVoice(self, index):  
        done = False
        if(index > len(self.voices)):
            self.talk("Please choose a valid index")        
        else:
            self.engine.setProperty('voice', self.voices[index].id)
            done = True
        return done
    
    def setVolume(self, volume):
        volume = self.engine.getProperty('volume')
        if(volume <= 100 and volume > 0):
            self.engine.setProperty('volume', volume/100)
            self.talk("The volume level is: " + volume)
        elif(volume > 100):
            self.engine.setProperty('volume', 1.0)
            self.talk("The volume level is: one hundred")


    def initialConfig(self):
        try:
            self.talk("Would you like to run an initial configuaration?")
            self.engine.runAndWait()
            command = self.listen()

            if(any(ele in command for ele in  self.affirmations)):
                self.configureVoiceType(self)
                   
            
        except:
            pass


    def listen(self):
        try:

            with sr.Microphone() as source:
                print("Listening...")
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()

                commandList = list(command.split(" "))
                return command
            
        except:
            pass

def main():
    assistant = Assistant()
    assistant.configureVoiceType()
    assistant.talk("Hello world")

if __name__ == "__main__":
    main()


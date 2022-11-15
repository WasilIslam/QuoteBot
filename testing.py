
import json
import pyttsx3


f= open("./data/dictionary.json")
data=dict(json.load(f))

string=" "
for key in data:
    string+=key+" meaning: "+data[key]

string=string[0:829105]

print("Started doing stuff: ",len(string))
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'dictionary.mp3')

engine.runAndWait()


f.close()









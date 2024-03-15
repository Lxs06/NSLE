import os
import time

enc_dict = {
    "a":"7",#used
    "b":"5",#used
    "c":"j",#used
    "d":"i",#used
    "e":"w",
    "f":"e",#used
    "g":"0",#used
    "h":"c",#used
    "i":"x",
    "k":"z",
    "l":"u",#double
    "m":"1",
    "n":"d",#used
    "o":"k",#used
    "p":"2",#used
    "q":"h",#used
    "r":"m",#used
    "f":"4",#used
    "t":"s",#used
    "u":"3",#used
    "v":"b",#used
    "w":"n",#used
    "x":"l",#used
    "y":"a",#used
    "z":"g",#used
    "0":"t",#used
    "1":"f",#used
    "2":"8",#used
    "3":"r",#used
    "4":"9",#used
    "5":"6",#used
    "6":"q",#used
    "7":"y",
    "8":"o",#used
    "9":"p",#used
}
String file_name = input("Enter file name: ")

file = open(file_name+".txt","r")
new_file open(file_name+"_NSLE.txt","w")

words = file.split(' ')

for word in words:
    for letter in word:
        try:
            new_file.write(enc_dict.)
        except:
            print("Error while encryption...")
            os.remove(file_name+"_NSLE.txt")
            time.sleep(5)
            exit()
import os
enc_dict = {
    "a":"w",#used
    "b":"0",#used
    "c":"v",#used
    "d":"4",#used
    "e":"u",
    "f":"8",#used
    "g":"6",#used
    "h":"3",#used
    "i":"z",
    "j":"9",
    "k":"y",
    "l":"o",#double
    "m":"t",
    "n":"p",#used
    "o":";",#used
    "p":"f",#used
    "q":"2",#used
    "r":"n",#used
    "f":"m",#used
    "t":"x",#used
    "u":"f",#used
    "v":"5",#used
    "w":"l",#used
    "x":"{",#used
    "y":"1",#used
    "z":"b",#used
    "0":".",#used
    "1":"e",#used
    "2":"h",#used
    "3":"r",#used
    "4":"d",#used
    "5":"k",#used
    "6":"j",
    "7":"q",
    "8":"i",
    "9":" ",
    " ":"a",
    ".":"g",
    ",":"",
    ";":"c",
    ":":"",
    "{":"7",
    "}":"",
    "[":"",
    "]":"",
    "(":"",
    ")":"",
    "&":"",
    "@":"",
    "#":"",
    "!":"",
    "?":"",
    "-":"",
    "+":"",
    "=":"",
    "*":"",
    "/":"",
}
file_name = input("Enter file name: ")
file = open(file_name+".txt","r")
new_file = open(file_name+"_NSLE.txt","w")
lines = file.readlines()
for line in lines:
    words = line.split('')
    for word in words:
        if word != "\n":
            for char in word:
                try:
                    new_file.write(enc_dict[char])
                except:
                    print("Error while encryption...")
                    os.remove(file_name+"_NSLE.txt")
                    time.sleep(5)
                    exit()
        else:
            new_file.write("\n")
new_file.close()
file.close()
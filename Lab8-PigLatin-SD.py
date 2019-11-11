#Lab8-PigLatin1-SD.py
#Stephen Davies
#turns a phrase into pig latin

def main():
    list = input("input a phrase you want converted to pig latin: ")
    msg = ""
    for word in list.split():
        word2 = word[1:] + word[0] + "e"
        msg = msg + word2 + " "
    print(msg)

#end main

main()
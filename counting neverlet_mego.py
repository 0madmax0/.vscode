#counting "the","a","and","of","for" in a textfile called neverletmego

def invert(dictionary):
    newdict = {}
    olditems = dictionary.items()
    for key, value in olditems:
        newdict[value]= key
    return newdict

def main():
    f = open("neverletmego.txt",'r')
    novella=f.read()
    f.close()
    words = ["the","a","and","of","for"]
    wordlist=[]
    frequencies={}
    for word in words:
        frequencies[word]=novella.count(word)+novella.count(word.upper())
    frequencies = invert(frequencies)
    reversekeys = sorted(frequencies,reverse = True)
    print("words     frequency")
    for key in reversekeys:
        print(f"{frequencies[key]}         {key}")
main()

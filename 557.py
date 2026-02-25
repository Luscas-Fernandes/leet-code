s = "Let's take LeetCode contest"

def printAllVariables(*args):
    print("All variables: ")
    for arg in args:
        print(arg)

lista = s.split(" ")
invertedList = []

for word in lista:
    sPointer = 0
    ePointer = len(word) - 1 # -1, if not, off by one
    listedWord = list(word)

    while sPointer < ePointer:        
        temp = listedWord[sPointer]
        listedWord[sPointer] = listedWord[ePointer]
        listedWord[ePointer] = temp

        sPointer += 1
        ePointer -= 1

    invertedList.append(listedWord)

result = " ".join("".join(word) for word in invertedList)
print(result)

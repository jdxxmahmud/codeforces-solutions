def isSequence(string, subStr):
    counter = 0

    for i in range(len(string)):
        if string[i] == subStr[counter]:
            counter += 1
            if counter == len(subStr):

                return "YES"

    return "NO"


requiredSequence = "heidi"
givenString = input()
print(isSequence(givenString, requiredSequence))

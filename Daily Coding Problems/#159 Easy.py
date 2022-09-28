# Given a string, return the first recurring character in it, or null if there is no recurring character.

# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

s1 = "acbcab"
s2 = "abcdefgkpnodef"

findin = s2
lowest = len(findin)
found = False

for x in range(len(findin)-1):
    c = findin[x]
    if(c in findin[x+1:]):
        found = True
        fndindex = findin[x+1:].index(c)
        if(fndindex+x < lowest):
            lowest = fndindex+x

if(found == True):
    print(findin[lowest+1])
else:
    print("Not found")
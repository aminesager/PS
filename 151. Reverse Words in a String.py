def reverseWords(s):
    new = ""
    temp = ""
    s += ' '
    for i in range(len(s)):
        temp += s[i]
        if temp == " ":
          temp = ""
        elif s[i] == " " :
            new = temp + new
            temp = ""
            
    return new[0:len(new)-1]

# take a string of input from the user, any capitalization 
# prints out the string
# all consonants in lower case
# all vowels in upper case 

def Changecap(str):
    str1 =""
    N = len(str)

    for i in range(N):
        if (str[i] == 'a'  or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
            temp = (str[i]).upper()
            str1 += temp

        elif(string[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U' ):
            str1 +=str[i]
            
        else:
            temp = (str[i]).lower()
            str1 += temp
    return str1

string = input("Please enter a random string: ")
print("The new string is: ", Changecap(string))





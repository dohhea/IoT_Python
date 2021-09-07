count=0

def toggle(ch):
    global count
    if (ch.isalpha()):
        count +=1
        if (ch>='a' and ch<='z'):
            return ch.upper()
        else:
            return ch.lower()
    return ch

string = input("Enter a sentense")

new_string = ""
for ch in string:
    new_string += toggle(ch)

print("Original string : " + new_string)
print("Changed string : " + new_string)
print("number of changes : ", count)

        
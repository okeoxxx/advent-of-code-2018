import string

file = open('5.txt','r')
text = file.read()

def delete(text,index):
    return text[:index]+text[index+2:]

def doit(text):
    for i,letter in enumerate(text):
        try:
            if letter.swapcase() == text[i+1]:
                text = delete(text,i)
                return doit(text)
        except:
            break
    return text

def react(text):
    while text != doit(text):
        print(len(text))
        text = doit(text)

    return len(text)

#řešení první části
#print('Řešením první části je:', react(text))

#druhá část
a = string.ascii_lowercase
result = []

for letter in a:
    new_text = ''
    for ch in text:
        if ch.lower() != letter:
            new_text += ch
    result.append(letter,react(new_text))
    print(letter,react(new_text))

lowest = 50000
result_char = ''
for lett in result:
    if lett[1] < lowest:
        lowest = lett[1]
        result_char = lett[0]

print('Řešením druhé části je:', lowest)

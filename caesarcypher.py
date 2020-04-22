# This is a basic script to use a caesar cypher (encode a message by replacing each letter with one X spots further down the alphabet)


latin_alpha = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

test_string = "Moe is the owner and operator of Moe's Tavern, frequented by Homer Simpson and other characters including Lenny Leonard, Carl Carlson, Sam and Larry and his former most loyal customer, Barney Gumble. The bar is noted for its depressing atmosphere and uncleanliness. The regular patrons of the tavern have been abandoned by Moe in several episodes in which he changes its target audience."
encrypted_string = "prh lv wkh rzqhu dqg rshudwru ri prh'v wdyhuq, iuhtxhqwhg eb krphu vlpsvrq dqg rwkhu fkdudfwhuv lqfoxglqj ohqqb ohrqdug, fduo fduovrq, vdp dqg oduub dqg klv iruphu prvw orbdo fxvwrphu, eduqhb jxpeoh. wkh edu lv qrwhg iru lwv ghsuhvvlqj dwprvskhuh dqg xqfohdqolqhvv. wkh uhjxodu sdwurqv ri wkh wdyhuq kdyh ehhq dedqgrqhg eb prh lq vhyhudo hslvrghv lq zklfk kh fkdqjhv lwv wdujhw dxglhqfh."

### DICTIONARY UNPACKERS

def return_key(dict, character):
    for index, letter in dict.items():
        if letter == character.lower():
            return index

def return_value(dict, num):
    return dict[num]

#### ENCRYPT MESSAGE

def cypherisor(dict, string, offset, encrypt):
    temp = ''
    stringy = string.lower()
    for letter in stringy:
        if letter in [',', '.',"'", '!']:
            temp += letter
            continue
        else:
            init_num = return_key(latin_alpha, letter)
            if init_num == None:
                temp += " "
            else:
                if encrypt == True:
                    if init_num >= 24:
                        init_num -= 26

                    offsetted = init_num + offset
                    new_letter = return_value(latin_alpha, offsetted)    
                    temp += new_letter
                else: 
                    if init_num <= 3:
                        init_num += 26
                    offsetted = init_num - offset
                    new_letter = return_value(latin_alpha, offsetted)    
                    temp += new_letter    
    return temp

crypted = cypherisor(latin_alpha,test_string, 3, True)

print(crypted)

decrypted = cypherisor(latin_alpha,encrypted_string, 3, False)

print(decrypted)

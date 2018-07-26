def encrypt(splitted_list, keyword,alphabet):
    i = 0
    translate = ""
    maxi = len(splitted_list)-1
    while i < maxi:
        for i,j in enumerate(splitted_list[i]):
            #print(i,j)
            i1 = alphabet.index(j)
            i2 = alphabet.index(keyword[i])
            
            value = (i1+i2) %26
            translate += alphabet[value]
            
        i+=1
    return translate    

def splitted(message,keyword,key_length,splitted_list):
    j = key_length
    for i in range(0,len(message)-1 , key_length):
        
        splitted_list.append(message[i:j])
        j += key_length
        
    return splitted_list

message = input("Enter Message: ").strip()
keyword = input("Enter Keyword: ").strip()
key_length = len(keyword)
splitted_list = []
message = message.replace(" ","")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(alphabet.index("A"))
splitted_list = splitted(message,keyword,key_length,splitted_list)

encrypt(splitted_list,keyword,alphabet)

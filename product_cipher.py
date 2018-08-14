def encrypt(splitted_list, keyword,alphabet):
    i = 0
    translate = ""
    maxi = len(splitted_list)-1
    while i <= maxi:
        for temp,j in enumerate(splitted_list[i]):
            #print(i,j)
            i1 = alphabet.index(j)
            i2 = alphabet.index(keyword[temp])
            
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

translate = encrypt(splitted_list,keyword,alphabet)
print("ENCRRYPTED TEXT: ",translate)

messages = translate
translated = ""
key = 3
matrix = [0] * 3
for i in range(key):
    matrix[i] = [0]*len(message)

dir_flag = False #false means down
z = 0
y = 0    #tracks message
for i in range(len(message)):
    if i == 0:
        matrix[0][0] = message[0]
        z += 1
        y += 1 
        
    elif dir_flag == False:
        matrix[z][i] = message[y]
        z += 1
        y += 1
        
        if z == key -1:
            dir_flag = True
            
    elif dir_flag:
        matrix[z][i] = message[y]
        z -= 1
        y += 1
        
        if z == 0:
            dir_flag = False
            

for i in matrix:
    for _ in i:
        if _ == 0:
            pass
        else:
            translated += _

print(translated)

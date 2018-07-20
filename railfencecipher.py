message = "MUNAFHAJIR"
translate = ""
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
            translate += _

#INPUT: MUNAFHAJIR
#Output: MFIUAHJRNA

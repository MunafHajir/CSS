def keyword_di(keyword_original):
    keyword = []
    for i in keyword_original:
        if i not in keyword:
            
            keyword.append(i)
    
    return keyword

def matrix(di_list,alphabet):
    for i in alphabet:
        if i == "I" or i == "J":
            
            if i not in di_list and "I" not in di_list and "J" not in di_list:
                di_list.append("I/J")
                
        elif i not in di_list:
            di_list.append(i)
            
    matrix_group = [[0]*5]*5
    
    matrix_group[0]=di_list[0:5]
    matrix_group[1]=di_list[5:10]
    matrix_group[2]=di_list[10:15]
    matrix_group[3]=di_list[15:20]
    matrix_group[4]=di_list[20:25]
    
    return matrix_group
    
def encrypt(message, matrix_group):
    translate = ""
    mess = []
    if len(message) % 2 != 0:
        message += "X"
    
    for i in range(0,len(message)-1,2):
        mess.append(message[i]+message[i+1])
    
    for pair in mess:
        pair1 = pair[0]
        pair2 = pair[1]
        
        #location variable
        pair1_loc = []
        pair2_loc = []
        
        #Location
        for i in range(0,5):
            for j in range(0,5):
                if pair1 == matrix_group[i][j]:
                    pair1_loc.insert(0, i)
                    pair1_loc.insert(1, j)
                elif pair2 == matrix_group[i][j]:
                    pair2_loc.insert(0, i)
                    pair2_loc.insert(1, j)
                    
        if pair1_loc[0] == pair2_loc[0]:
            translate += matrix_group[pair1_loc[0]][(pair1_loc[1]+1) % 5] 
            
            translate += matrix_group[pair2_loc[0]][(pair2_loc[1]+1) % 5] 
            
        elif pair1_loc[1] == pair2_loc[1]:
            translate += matrix_group[(pair1_loc[0]+1)%5][pair1_loc[1]] 
            
            translate += matrix_group[(pair2_loc[0]+1)%5][pair2_loc[1]] 
            
        else:
            translate += matrix_group[pair1_loc[0]][pair2_loc[1]]
            translate += matrix_group[pair2_loc[0]][pair1_loc[1]]
                        
    return translate
keyword = "FAIRYTALE"

alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"

message = "IYMCMINX"
#print(len(message))
di_list = keyword_di(keyword)
matrix_group = matrix(di_list,alphabet)
translate = encrypt(message,matrix_group)
print(translate)
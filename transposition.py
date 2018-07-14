message = "HIIAMMUNAF"
key = "BEC"
keyl = len(key)
l_index = []
translated = ''
i = 0
while True:
    if i > len(message)-1:
        i = 1
        
    elif i not in l_index:
        l_index.append(i)
        translated += message[i]
        i += keyl
    
        
        
    else:
        if i in l_index:
            i+=1
            
            if i in l_index:
                break 
                
print(translated)
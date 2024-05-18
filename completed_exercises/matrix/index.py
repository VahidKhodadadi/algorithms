import math

def matrix(n):
    iteration = 0
    result = []
    num = 1
    
    # initialize list
    for i in range(0, n):
        result.append([])
        for j in range(0, n):
            result[i].append(0)  
        
    # display initial values           
    # for arr in result:
    #     print(arr) 
    
    row = 0
    col = 0
            
    while True:
        # step 1
        for y in range(iteration, n - iteration):
            result[iteration][y] = num
            num += 1
            if y == (n - 1 - iteration):
                col = y
                break
            
        # step 2        
        for x in range(iteration + 1, n - iteration):
            result[x][col] = num
            num += 1
            if x == (n - 1 - iteration):
                row = x
                break
            
        # step 3   
        for y in reversed(range(iteration, n - 1 - iteration)):
            result[row][y] = num
            num += 1
            if y == iteration:
                col = y
                break
         
        # step 4   
        for x in reversed(range(iteration + 1, n - 1 - iteration)):
            result[x][col] = num
            num += 1
                    
        if result[math.floor(n/2)][math.floor(n/2)] != 0:
            break
        
        iteration += 1
    
    for arr in result:
        print(arr)
        
    return result
            
            
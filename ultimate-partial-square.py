import json 
# Python3 program to partially square a number  
# represented as array. 
  
# iteratively computes one digit at time and saves result in json file. 
def ultimate_partial_square():
    
    digits = [5]
    limit = 20
    current_length = len(digits)
    carry_old = 0
    
    
    while current_length < limit:
        
        #prints progress
        if len(digits) % 1000 == 0:
            print("I have reached this", len(digits))
        
        result = [0] + digits #we just need to compute result[0] which is set to 0 at the moment

        
        carry_new = 0
        value_a = 0
        
        for i in range(0, current_length // 2):
            j = current_length-i-2
            temp_a = digits[i] * digits[j]
            if i!=j:
                temp_a += temp_a
            value_a += temp_a
                
        carry_new = value_a // 10 # green part of the formula
        value_a = value_a % 10 # blue part of the formula
        
        #orange part of the formula
        if current_length > 1:
            value_b = (digits[0] * digits[current_length-1]) // 5
        else: #exception for t00
            value_b = (digits[0] * digits[current_length-1]) // 10

        
        t_result = value_a + value_b + carry_old 
        result[0] = t_result % 10 #value x_n+1
        carry_result = t_result // 10 #red part of the formula
        
        carry_old = carry_new + carry_result # carry for the next iteration
        digits = result
        current_length = len(digits)
    
    with open("result.json","w") as file:
        json.dump(digits, file)

    
    
import time
start_time = time.time()
ultimate_partial_square()
print("--- %s seconds ---" % (time.time() - start_time))

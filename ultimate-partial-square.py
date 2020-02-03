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
        
        if len(digits) % 1000 == 0:
            print("I have reached this", len(digits))
        # will keep the result number in vector 
        # in reverse order 
        
        result = [0] + digits#* (current_length + 1) 
        #total_len = len(result)

        
        carry_new = 0
        value_a = 0
        for i in range(0, current_length // 2):
            j = current_length-i-2
            temp_a = digits[i] * digits[j]
            if i!=j:
                temp_a += temp_a
            value_a += temp_a
            #carry_new += temp_a // 10
            #value_a += temp_a % 10
                
        carry_new = value_a // 10
        value_a = value_a % 10
        #print(current_length,":",value_a)
        
        if current_length > 1:
            value_b = (digits[0] * digits[current_length-1]) // 5
        else:
            value_b = (digits[0] * digits[current_length-1]) // 10

        
        t_result = value_a + value_b + carry_old 
        result[0] = t_result % 10
        carry_result = t_result // 10
        
        carry_old = carry_new + carry_result
        digits = result
        current_length = len(digits)
    
    with open("result.json","w") as file:
        json.dump(digits, file)

    
    
import time
start_time = time.time()
ultimate_partial_square()
print("--- %s seconds ---" % (time.time() - start_time))

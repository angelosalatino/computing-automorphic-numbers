import time
# Python3 program to partially square a number  
# represented as array. 
  
# partially squares number and prints result. 
def square(number): 
    num_length = len(number) 
    
    # variable hosting the result
    result = [0] * (num_length+1) 
    total_len = len(result)
    # two indexes used to find positions in result
    index1 = 0
    index2 = 0
  
    # iterating in reverse order
    for i in range(num_length - 1, -1, -1): 
        carry = 0
        n1 = number[i]
  
        # for shift position each iteration
        index2 = 0
  
        # iterating in reverse order
        for j in range(num_length - 1, -1, -1): 
            
            # STOP CRITERIA
            if (index1 + index2) >= total_len:
                break
             
            n2 = number[j]
          
            # multiply the two digits and sum their result 
            # with the previous carry and the current value in result
            summ = n1 * n2 + result[index1 + index2] + carry 
  
            # computing the next carry
            carry = summ // 10
  
            # Store its modulo in result 
            result[index1 + index2] = summ % 10
  
            index2 += 1
  
            # hold carry for next iteration
        if (carry > 0) and (index1 + index2) < total_len: 
            result[index1 + index2] += carry 
  
        index1 += 1
  
    # returning the inverted array
    return result[::-1]
  
  

start_time = time.time()
digits = [5]
limit = 20
while len(digits) < limit:
    res = square(digits) 
    digits = res[(len(res)-len(digits)-1):]
    if len(digits) % 1000 == 0:
        print("I have reached this", len(digits))
print(digits)
print("--- %s seconds ---" % (time.time() - start_time))

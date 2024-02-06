# Convert military time to standard time.
# Military midnight being 0000 and standard midnight being 12:00AM

#input format creates a string naturally, because of this we need to define each instance of this variable as an integer
mil_time = input('Enter time in 24 Hour format to convert to Standard format: ')


# while loop to check if input is valid
while mil_time[0] != (int(0) or int(1)) and mil_time[1] != (int(0) <= num <=int(9)):

# if military time is after 11:59AM we are changing to pm

if int(mil_time) > 1159: 
    
    # if military time is actually 1200 then we need to state this is 12:00 pm
    # further iteration to attempt to cover between 1201 and 1259
    
	if 1200 <= int(mil_time) <= 1259:
        new_time = str(mil_time)
        print(new_time[0] +new_time[1] + ':' +new_time[2] + new_time[3] + 'PM')
        
    else:
        new_time = str(int(mil_time) - 1200)
        
        #if attempt to print time as index
        if int(new_time) < 1000:
            
            
            print(new_time[0] + ':' + new_time[1] +new_time[2] + 'PM')

        else:
            print(new_time[0] +new_time[1] + ':' +new_time[2] + new_time[3] + 'PM')


else:
    if int(mil_time) < (100):
        
        new_time = str(int(mil_time) + 1200)
        
        print(str(new_time[0]) + str(new_time[1]) + ':' + str(new_time[2]) + str(new_time[3]) + 'AM')
        
    else:
        
        new_time = str(mil_time)
    

        if int(new_time) < 1000:
            print(new_time[0] + ':' + new_time[1] + new_time[2] + 'AM')

        else:
            print(new_time[0] +new_time[1] + ':' +new_time[2] + new_time[3] + 'AM')

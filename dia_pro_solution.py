message = input("enter a message") 
mod_string = message + '!'
length = len(mod_string)
mod_string

count=0
for i in range(0,length):
    if i<length-1:
        if mod_string[i]!=mod_string[i+1]:
            print(mod_string[i])
            if count>1:
                print(count+1)
                count=0
        else:
            count+=1
students = [ "Ram" , "Shyam" , "Krishan" , "Dipankar" , "Radhika"]


for i in range(len(students)) :
    if students[i] == "Dipankar" :
        continue
    else:
        print(students[i])


arr = [ 2 , 3 ,4  , 5 , 6, 7, 8]
for i in range(len(arr)) :
    print(arr[i])
    i = i + 1 ;
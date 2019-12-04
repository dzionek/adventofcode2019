def findDuplicates(password):
    duplicates = set()
    for i in range (5):
        if password[i] == password[i+1]:
            k = 1
            z = 1
            for k in range (6):  
                if (password[i],k) in duplicates:
                    z = k + 1
            if z>1:
                duplicates.remove((password[i],z-1))
                duplicates.add((password[i],z))
            else:
                duplicates.add((password[i],2))
    return duplicates

def checkPassword(password,question):
    for i in range(5):
        if not (password[i] <= password[i+1]):
            return False
    duplicates = findDuplicates(password)
    if len(duplicates) == 0:
        return False
    
    if question == 2:
        for (n,occurrences) in duplicates:
            if occurrences >2:
                if len(duplicates)==1:
                    return False
                else:
                    duplicates.remove((n,occurrences))
                    for (n_step,occurrences_step) in duplicates:
                        if occurrences_step != 2:
                            return False
                    duplicates.add((n,occurrences))
    return True

password = [0,0,0,0,0,0]
n_one = 0
n_two = 0

for i in range (206938,679129):
    password[0] = i // 100000
    password[1] = (i-100000*password[0]) // 10000
    password[2] =  (i-100000*password[0]-10000*password[1]) // 1000
    password[3] = (i-100000*password[0]-10000*password[1] - 1000*password[2]) // 100
    password[4] = (i-100000*password[0]-10000*password[1] - 1000*password[2] - 100*password[3]) // 10
    password[5] = (i-100000*password[0]-10000*password[1] - 1000*password[2] - 100*password[3] - 10*password[4])
    
    if checkPassword(password,1):
        n_one += 1
    if checkPassword(password,2):
        n_two += 1
print(n_one)
print(n_two)
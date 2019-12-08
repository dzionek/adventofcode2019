def find_duplicates(password):
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


def check_password(password,question):
    for i in range(5):
        if not (password[i] <= password[i+1]):
            return False
    duplicates = find_duplicates(password)
    if len(duplicates) == 0:
        return False
    
    if question == 2:
        for (n,occurrences) in duplicates:
            if occurrences >2:
                if len(duplicates) == 1:
                    return False
                else:
                    duplicates.remove((n,occurrences))
                    for (n_step,occurrences_step) in duplicates:
                        if occurrences_step != 2:
                            return False
                    duplicates.add((n,occurrences))
    return True


n_one = 0
n_two = 0

for i in range (206938,679129):
    password = list(map(int,str(i)))
    if check_password(password,1):
        n_one += 1
    if check_password(password,2):
        n_two += 1

print(n_one)
print(n_two)
#change this list with keywords matchin that of the person

nam=['bill','gates','2001','1967','elon','1234','123','08','8','!','@','2020','2019','2018','#','09031999','08','qwerty','davi123@gmail.com','password','root','toor','01','1','654712342','867876545','hello','12345678','        ','fuck','ilove','%']


def qq():
    input("")
    
def w1(nam,h):
    import itertools,hashlib
    permutations=itertools.permutations(nam,1)
    final_list=[]
    m=0
    for permutation in permutations:
        final_list.append(permutation[0])
    for key in final_list:
        print("TRYING       " +key)
        m=m+1
        result=hashlib.md5(key.encode())
        if h==str(result.hexdigest()):
            print("THE PASS IS > " +key)
            print (m)
            qq() 
            break 
def w2(nam,h):
    import itertools,hashlib
    permutations=itertools.permutations(nam,2)
    final_list=[]
    m=0
    for permutation in permutations:
        final_list.append(permutation[0]+permutation[1])
    
    for key in final_list:
        print("TRYING       " +key)
        m=m+1
        result=hashlib.md5(key.encode())
        if h==str(result.hexdigest()):
            print("THE PASS IS > " +key)
            print (m)
            qq() 
            break       
def w3(nam,h):
    import itertools,hashlib
    permutations=itertools.permutations(nam,3)
    final_list=[]
    m=0
    for permutation in permutations:
        final_list.append(permutation[0]+permutation[1]+permutation[2])
    for key in final_list:
        print("TRYING       " +key)
        m=m+1
        result=hashlib.md5(key.encode())
        if h==str(result.hexdigest()):
            print("THE PASS IS > " +key)
            print (m)
            qq() 
            break    
def w4(nam,h):
    import itertools,hashlib
    permutations=itertools.permutations(nam,4)
    final_list=[]
    m=0
    for permutation in permutations:
        final_list.append(permutation[0]+permutation[1]+permutation[2]+permutation[3])
    for key in final_list:
        print("TRYING       " +key)
        m=m+1
        result=hashlib.md5(key.encode())
        if h==str(result.hexdigest()):
            print("THE PASS IS > " +key)
            print (m)
            qq() 
            break  
def w5(nam,h):
    import itertools,hashlib
    permutations=itertools.permutations(nam,5)
    final_list=[]
    m=0
    for permutation in permutations:
        final_list.append(permutation[0]+permutation[1]+permutation[2]+permutation[3]+permutation[4])
    for key in final_list:
        print("TRYING       " +key)
        m=m+1
        result=hashlib.md5(key.encode())
        if h==str(result.hexdigest()):
            print("THE PASS IS > " +key)
            print (m)
            qq() 
            break
m=0
h=str(input("ENTER HASH TO CRACK > ")).lower()
w1(nam ,h)
w2(nam ,h)
w3(nam ,h)
w4(nam ,h)
w5(nam ,h)
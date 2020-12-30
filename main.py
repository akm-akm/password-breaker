import itertools,hashlib,os
nam=list(map(str, input().rstrip().split()))


def w1(nam,h):
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
            os._exit(0) 
def w2(nam,h):
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
            os._exit(0)       
def w3(nam,h):
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
            os._exit(0)    
def w4(nam,h):
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
            os._exit(0)
def w5(nam,h):
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
            os._exit(0)

h=str(input("ENTER HASH TO CRACK > ")).lower()
w1(nam ,h)
w2(nam ,h)
w3(nam ,h)
w4(nam ,h)
w5(nam ,h)

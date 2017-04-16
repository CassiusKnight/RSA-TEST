import math
import random

def main(): # first definition
    q1 = input("Want to Encrypt/Decrypt(1)or crack N to find P and Q(2)?: ")
    if q1 == "1":
        q2 = input("Choose values(1) or generate them(2)?")
        if q2 == "1":
            P, Q = primePQ()
        elif q2 == "2":
            P = primeRange()
            Q = primeRange()
        N = P*Q
        d = 1000
        tot = (P-1)*(Q-1)
        print("P =", P, "\nQ =", Q, "\nN =", N, "\nTotient =", tot)
        exp = ex(tot)
        cipher(N,exp,d)
        deCipher(d,N)
        print("\n")
        main()
    elif q1 == "2":
        crackPQ()
    else:
        main()

#RANDOM PRIME GENERATOR---------------------------------------------
def primeRange():
    primeChoice = [i for i in range(100,100000) if findPrime(i)]
    x = random.choice(primeChoice)
    return x
#-------------------------------------------------------------------

#PRIME NUMBER CHECKER-------------------------------------------------------
def findPrime(x):
    if x <= 2:
        print(x, "is a not a valid input!")
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:  return False
    return True
#---------------------------------------------------------------------------

#PRIME NUMBER P AND QCHOOSING-----------------------------------------------
def primePQ():
    def primeP():
        try:
            P = int(input("Enter your prime number, P: "))
        except:
            print("Invalid Input! - Must be an Integer")
            primePQ()
            exit()
        if findPrime(P):    return P
        else: primeP()
    def primeQ():
        try:
            Q = int(input("Enter your prime number, q: "))
        except:
            print("Invalid Input! - Must be an Integer")
            primePQ()
            exit()
        if findPrime(Q):    return Q
        else: primeQ()
    p = primeP()
    q = primeQ()
    return p, q
#------------------------------------------------------------------

#CRACKS N TO FIND P AND Q ------------------------------------------
def crackPQ():
    try:
        N = int(input("Enter the N value you want to Crack: "))
    except:
        print("Invalid Input! - Must be an Integer")
        crackPQ()
        exit()
    realN = False
    for i in range(2,int(math.sqrt(N))+1):
        if i % 2 == 0 or i % 3== 0 or i%5== 0 or i%7== 0 or i%9 == 0:   N = N
        else:
            findP = N/i
            if findP.is_integer():
                realN = True
                rightQ = findP
                rightP = N/findP
                print("P is:",int(findP),"\nQ is:",int(N/rightQ),"\n")
    if realN == False:
        print("Not a valid N value...")
        crackPQ()
    WantTot = input("Want to find the Totient using these values?(Y/N): ")
    rightTot = (rightP-1) * (rightQ - 1)
    if WantTot == "y":
        print("Totient = (P-1) * (Q-1)\n(",int(rightP),"- 1 ) * (",int(rightQ),"- 1 ) =",int(rightTot),"\n")
        crackPQ()
    else: crackPQ()
#-----------------------------------------------------------------------

#ENCRYPTS/DECRYPTS THE FILE------------------------------------------------------
def cipher(N,exp,d):
    plain = input("Input Plaintext to be encrypted: ")
    plain2 = '\n'.join(str(ord(p)) for p in plain)
    file = open('EncryptRSAOutput.txt', 'w')
    for eachLine in plain2.split():
        cipherText = (int(eachLine)**exp % N )
        file.write('%d\n' % cipherText)
    file.close()
    file = open('EncryptRSAOutput.txt', 'r')
    view = input("Want to see the ciphertext?(y/n)")
    if view == "y":
        print(file.read())
        return True
    else:return True

def deCipher(d,N):
    q1 = input("Would you like to decrypt the message?(y/n)")
    if q1 == "y":
        file = open('EncryptRSAOutput.txt', 'r')
        for eachLine in file:
            pl =(int(eachLine)**d % N)
            print(chr(pl),end='')
    else:
        return False
#--------------------------------------------------------------------------

#FINDS THE EXPONENT--------------------------------------------------------
def ex(x):
    print("Here's a list of potential 'e' values: ")
    for i in range (1,14,2):
        if x % i != 0 and i != 9:           print(i, end =", ")

    exp = int(input("\nSelect your 'e' value: "))
    if x % exp != 0 and exp <= 13 and exp != 9:
        return exp
    else:
        print("Not a valid choice!")
        ex(x)
    exp = ex()
#---------------------------------------------------------------------------






main()

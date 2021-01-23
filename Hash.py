import hashlib
import csv

def hash_finder():
    hash_list = list()
    hash_av = list()
    g = open("test.txt","w")
    with open("pass.csv","r") as f :
        reader = csv.reader(f)
        for row in reader :
            password = row[1]
            hash_av.append(password)
            #print(password)
        for i in range(300,900):
            k = bytearray(i)
            m = hashlib.sha256(k).hexdigest()
            hash_list.append(m)
            moratab = m + "\n"
            g.write(moratab)
    for i in hash_list :
        for p in hash_av :
            if i == p :
                print("taths it : ",p)
    g.close()
hash_finder()
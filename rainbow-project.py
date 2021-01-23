import hashlib
import csv

def hash_finder():
    hash_av = list()
    g = open("hash_list.txt","w")
    with open("pass.csv","r") as f :
        combo = dict()
        hash_list = list()
        reader = csv.reader(f)
        for row in reader :
            code = row[0]
            password = row[1]
            combo[password] = code
            hash_av.append(password)
        for i in range(300,900):
            k = bytearray(i)
            m = hashlib.sha256(k).hexdigest()
            hash_list.append(m)
        for i in hash_list :
            if i in combo.keys() :
                r = combo[i]
                final =  r + " => " + i + "\n"
                g.write(final)
    g.close()
hash_finder()
from random import randint
import json

def lcs ():
    names = ["IZAANSOHAIL", "MARIAALIASGHAR"]

    for i in range (10):
        seqs = []
        for name in names:
            seq1 = ""
            lenstr = randint (30, 100)
            while len (seq1) <lenstr:
                seq1 += name [randint (0, len (name) -1)]
            seqs.append (seq1)
        
            with open("./Algorithms-InputFiles/0_input/0-" + str(i) + ".json", "w") as f:
                data = {"data": seqs}
                f.write (json.dumps (data))

def scs ():
    names = ["IZAANSOHAIL", "MARIAALIASGHAR"]


    for i in range (10):
        seqs = []
        for name in names:
            seq1 = ""
            lenstr = randint (30, 50)
            while len (seq1) <lenstr:
                seq1 += name [randint (0, len (name) -1)]
            seqs.append (seq1)
        
            with open ("./Algorithms-InputFiles/1_input/1-" + str (i) + ".json", "w") as f:
                data = {"data": seqs}
                f.write (json.dumps (data))

def lis ():
    for i in range (10):
        lenarr = randint (0, 100)
        arr = []
        while len (arr) <lenarr:
            arr.append (randint (30, 100))
        
        with open ("./Algorithms-InputFiles/2_input/2-" + str (i) + ".json", "w") as f:
            data = {"data": arr}
            f.write (json.dumps (data))

def lvd ():
    names = ["IZAANSOHAIL", "MARIAALIASGHAR"]

    for i in range (10):
        seqs = []
        for name in names:
            seq1 = ""
            lenstr = randint (30, 100)
            while len (seq1) <lenstr:
                seq1 += name [randint (0, len (name) -1)]
            seqs.append (seq1)
        
            with open ("./Algorithms-InputFiles/3_input/3-" + str (i) + ".json", "w") as f:
                data = {"data": seqs}
                f.write (json.dumps (data))

def mcm ():
    for i in range (10):
        lenarr = randint (0, 100)
        arr = []
        while len (arr) <lenarr:
            arr.append (randint (30, 100))
        
        with open ("./Algorithms-InputFiles/4_input/4-" + str (i) + ".json", "w") as f:
            data = {"data": arr}
            f.write (json.dumps (data))

def ks01 ():
    for i in range (10):
        numpts = randint (10, 100)
        data = {}
        w = []
        v = []
        while len (w) <numpts:
            w.append (randint (1, 100))
            v.append (randint (1, 100))
        data ["n"] = numpts
        data ["w"] = w
        data ["v"] = v
        data ["W"] = 168

        with open ("./Algorithms-InputFiles/5_input/5-" + str (i) + ".json", "w") as f:
            data = {"data": data}
            f.write (json.dumps (data))


def partition ():
    for i in range (10):
        lenarr = randint (0, 100)
        arr = []
        while len (arr) <lenarr:
            arr.append (randint (30, 100))
        
        with open ("./Algorithms-InputFiles/6_input/6-" + str (i) + ".json", "w") as f:
            data = {"data": arr}
            f.write (json.dumps (data))

def rc ():
    for i in range (10):
        numpts = 168
        data = {}
        w = []
        v = []
        while len (w) <numpts:
            w.append (randint (1, 100))
            v.append (randint (1, 100))
        data ["n"] = numpts
        data ["l"] = w
        data ["p"] = v
        data ["L"] = 168

        with open ("./Algorithms-InputFiles/7_input/7-" + str (i) + ".json", "w") as f:
            data = {"data": data}
            f.write (json.dumps (data))

def coin ():
    ids = [168, 62]
    for i in range (10):
        index = randint (0,1)
        lenarr = randint (0, 100)
        data = {}
        arr = []
        while len (arr) <lenarr:
            arr.append (randint (30, 100))
        
        data ["coins"] = arr
        data ["money"] = ids [index]
        with open ("Algorithms-InputFiles/8_input/8-" + str (i) + ".json", "w") as f:
            data = {"data": data}
            f.write (json.dumps (data))


def wb ():
    names = ["izaansohail", "mariaaliasghar"]
    string = 'abcdefghijklmnopqrstuvwxyz'

    for i in range (10):
        index = randint (0,1)
        data = {}
        dictionary = []
        seq = ""
        for j in range (len (names [index])):
            wordlen = randint (5, 15)
            while len (seq) <wordlen: 
                strindex = randint (0,25)
                seq += string [strindex]
            dictionary.append (seq)
            seq = ""
        
        data ["s"] = names [index]
        data ["wordDict"] = dictionary
        with open ("Algorithms-InputFiles/9_input/9-" + str (i) + ".json", "w") as f:
            data = {"data": data}
            f.write (json.dumps (data))



lcs ()
scs ()
lis ()
lvd ()
mcm ()
ks01 ()
partition ()
rc ()
coin ()
wb ()

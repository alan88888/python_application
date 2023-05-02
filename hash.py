import hashlib
import os
import math
file="avengers.mp4"
buffer=1024
size=math.ceil(os.path.getsize(file)/1024)
sha256=hashlib.sha256()
data={}
#print(size)
with open(file,"rb") as f:
    content=f.read()
    hashlist=[]
    #print(type(hashvalue))
    chunklist = [content[i:i+buffer] for i in range(0, len(content), buffer)]
    for i in range(len(chunklist)):
        if chunklist!=[]:
            hashlist.insert(0,chunklist[-1])
            chunklist.pop()
            tmp=b""
            if len(hashlist)>1:
                #print(type(hashlist[0]),type(hashlist[1]))
                tmp=hashlist[0]+hashlist[1].encode()
            elif len(hashlist)==1:
                tmp=hashlist[0]
            #print(type(tmp))
            previous_hash = tmp
            new_hash = hashlib.sha256(previous_hash).hexdigest()
            while hashlist!=[]:
                hashlist.pop()
            #print(type(new_hash))
            hashlist.append(new_hash)
    print(new_hash)

    #sha256.update(data)
    #hashvalue=sha256.hexdigest().encode()
    #print(hashvalue)


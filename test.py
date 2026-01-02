with open ("demo.txt","r") as f:
    data=f.read()
    print(data)
    f.close
with open ("demo.txt","w") as g:
    data2=g.write("hello world")
    print(chr(data2))
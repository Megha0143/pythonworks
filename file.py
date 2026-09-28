#append

# write a pgm to append the content from one file into another text file
f=open("f1.txt", "r")
s=f.read()
f.close()
ff=open("f2.txt", "a")
ff.write(s)
ff.close()



#for opening file we use open() function.
#usage => infile = open(file_name, mode) *A PATH WHICH WE WANT TO CREATE IN
#MODES
#"w" (write), "a" (append), "x", (create), "r" (read) 
#with the help of .close() method we close the file.
#.write() helps us to write things to the file.
# *** file = open("newfile.txt", "w", encoding = 'utf-8') w methodu ile açtıgımızda klasörde cursor en başta yanıp sönmeye başlar başlangıçtaki bilgiler de gider.
#a modunda açtıgımızda ise kaldıgı yerde devam eder.

#try:
#    infile = open("file.txt", "r", encoding = "utf-8")
#    print(infile)
    #*****for loop******
    #for line in infile:
    #    print(line, end="")
    #content_one = infile.read()(#howmanycharacters you want to read)
    #print("content-1:")
    #print(content_one)
    #print("content-2:")
    #content_two = infile.read()#cursor will continue if you read before closing the file again.
    #****readline*****
    #print(infile.readline(), end="")#dosya bittikten sonra boş satır ekler.
    #****readlines*****
    #listOfFile = infile.readlines()
    #print(listOfFile)


    
#except FileNotFoundError:
#    print("You've been made mistake about location of the file.")
#else:
#    print("\nWorking...")
#finally:
#    infile.close()
#****Functions for files*****
#open("filename.txt", "mode", encoding = "encoding type")

#with the help of "with", we can create blocks for file processing...

#with open("file.txt", "r", encoding = "utf-8") as infile:
#    content = infile.read()
#    print(content)
    #*** tell method shows us the index of the cursor.
    #*** seek will place the cursor which index you want to.

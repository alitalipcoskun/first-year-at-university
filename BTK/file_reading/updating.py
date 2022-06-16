with open("file.txt", "r+", encoding ="utf-8") as infile:
    #r+ means reading and writing.
    infile.seek(25)
    infile.write("\ndeneme")

with open("file.txt", "r+", encoding="utf-8") as infile:
    print(infile.read())
try :

    file1= open("sample.txt", 'r')
    read=file1.read()
    print(read)
    file1.close()
except FileNotFoundError:
    print("the file 'sample.txt' was not found ")

import os

def compareFiles(file1, file2):
    directory = os.path.dirname(os.path.abspath(__file__))
    #print(directory)
    ficheiro1 = open(os.path.join(directory, file1), 'rb')
    ficheiro2 = open(os.path.join(directory, file2), 'rb')

    while True:
        portion1 = ficheiro1.read(1024)
        portion2 = ficheiro2.read(1024)

        if portion1 != portion2:
            return False

        if len(portion1)==0 and len(portion2)==0:
            return True

print(compareFiles('texto1.txt', 'texto2.txt'))
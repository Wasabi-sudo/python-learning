look_up = input("what do you want?\n")

found = False

#The 'with' keyword makes sure the File is properly closed when the file operations are done even if a exception is raised
with open('/home/ID/desroches_f/Workspace/Python/PythonCourse/exo/19-Files_read_write/my_acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line, 'this match!')
            found = True
            break

if not found:
    print('The acronym does not exist')
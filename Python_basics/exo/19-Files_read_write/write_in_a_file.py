acronym = input('add a words')

"""
'r' => read (par default)
'w' => write (efface ce qu'il y avait)
'a' => ajoute a la suite
'r+' => read&write
"""
with open('/home/ID/desroches_f/Workspace/Python/PythonCourse/exo/19-Files_read_write/my_acronyms.txt', 'a') as file:
    file.write(acronym + '\n')

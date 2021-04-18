def urai (x):                                                   # membuat fungsi
    c = ''                                                      # menampung nilai sementara
    for i in x:                                                 # melakukan perulangan
        c += i
        print(c, end='')
    for r in c:
        print(r, end='')
    print()

urai('Code')                                                    # memanggil fungsi       
urai('Python')                                                  # memanggil fungsi

print()

def rajut ():                                                   # membut fungsi
    code = 'CCoCodCodeCodCoC'                                   # input manual
    c = code[6:10]                                              # slicing string
    print('Huruf tak beraturan', code)
    print('Katanya adalah',c)
    print()
 
    python = 'PPyPytPythPythoPythonPythoPythPytPyP'             # input manual
    p = python[15:21]                                           # slicing stirng
    print('Huruf tak beraturan', python)
    print('Katanya adalah',p)
    print()

print()
rajut ()                                                       # memanggil fungsi
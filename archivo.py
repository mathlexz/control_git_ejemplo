num_instructions = int(input())
dict_directories = dict()
dict_directories["Mark"] = dict()
 
current_location = "/Mark"
 
def printdict(father_dict, directories, level):
    print(father_dict + ":")
    for child_directory in directories:
        print("--"*(level + 1), end = "")
        printdict(child_directory, directories[child_directory],level+1)
 
def insert(location, new_directory):
    navigation = dict_directories
    directories = location.split("/")[1:]
    
    for directory in directories:
        navigation = navigation[directory]
    
    navigation[new_directory] =dict()
 
for item in range(num_instructions):
    instruction, argument = input().split(" ")
    
    if instruction == "cd":
        if argument == "..":
            current_location = "/".join(current_location.split("/")[:-1])
        else:
            current_location = current_location + "/" + argument
    else:
        insert(current_location, argument)
 
printdict("Mark", dict_directories["Mark"], 0)

Ejercicio RAM
cantidad_instrucciones = int(input())

ram = {}

for _ in range(cantidad_instrucciones):
    linea = input().split(" ")
    
    if linea[0] == "load":
        #procesamos un load
        _, direccion_memoria, id_proceso = linea
        if direccion_memoria in ram:
            #direccion de memoria ocupada
            print("La posicion de memoria %s ya estaba ocupada con el proceso %s" % (direccion_memoria,ram[direccion_memoria]))
        else:
            #direccion de memoria libre
            ram[direccion_memoria] = id_proceso
            print("La carga del proceso %s en la posicion de memoria %s fue exitosa" % (id_proceso, direccion_memoria))
    else:
        #procesar un unload
        _, direccion_memoria = linea
        if direccion_memoria in ram:
            ram.pop(direccion_memoria)
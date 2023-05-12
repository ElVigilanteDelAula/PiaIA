
actividades = {
    'Actividad 1': {'materia': 1, 'tema': 1, 'subtema': 1, 'valor': 10, 'tiempo': 2, 'depende': [], 'obligatorio': False },
    'Actividad 2': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 20, 'tiempo': 3, 'depende': ['Actividad 1'], 'obligatorio': False },
    'Actividad 3': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 10, 'tiempo': 4, 'depende': [], 'obligatorio': False },
    'Actividad 4': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 15, 'tiempo': 5, 'depende': ['Actividad 2', 'Actividad 3'], 'obligatorio': False },
    'Actividad 5': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 25, 'tiempo': 3, 'depende': ['Actividad 1'], 'obligatorio': False },
    'Actividad 6': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 10, 'tiempo': 2, 'depende': [], 'obligatorio': False },
    'Actividad 7': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 26, 'tiempo': 1, 'depende': [], 'obligatorio': False },
    'Actividad 8': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 14, 'tiempo': 3, 'depende': ['Actividad 7'], 'obligatorio': False },
    'Actividad 9': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 8, 'tiempo': 2, 'depende': ['Actividad 6', 'Actividad 8'], 'obligatorio': False },
    'Actividad 10': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 21, 'tiempo': 1, 'depende': [], 'obligatorio': False }
}

cantidadSubtemas = 0
cantidadmaterias = 0
cantidadtemas = 0
subtemas = {}
materias = {}
temas = {}

for actividad in actividades:
    subtema = actividades[actividad]['subtema']
    if subtema not in subtemas:
        cantidadSubtemas = cantidadSubtemas + 1
        subtemas[subtema] = {}
    subtemas[subtema][actividad] = actividades[actividad]
cantidadSubtemas = cantidadSubtemas + 1

for actividad in actividades:
    materia = actividades[actividad]['materia']
    if materia not in materias:
        cantidadmaterias = cantidadmaterias + 1
        materias[materia] = {}
    materias[materia][actividad] = actividades[actividad]
cantidadmaterias = cantidadmaterias + 1

for actividad in actividades:
    tema = actividades[actividad]['tema']
    if tema not in temas:
        cantidadtemas = cantidadtemas + 1
        temas[tema] = {}
    temas[tema][actividad] = actividades[actividad]
cantidadtemas = cantidadtemas + 1




# Función para generar las combinaciones de actividades posibles a partir de un nodo dado
def generar_sucesores(nodo_actual, actividades):
    sucesores = []
    for actividad, datos in actividades.items():
        # Si la actividad ya ha sido seleccionada en el nodo actual, omitirla
        if actividad in nodo_actual['actividades']:
            continue
        # Si la actividad depende de actividades que no han sido seleccionadas aún, omitirla
        if any(dependencia not in nodo_actual['actividades'] for dependencia in datos['depende']):
            continue
        # Generar un nuevo nodo que incluya la actividad
        nuevas_actividades = nodo_actual['actividades'] | {actividad}
        nuevo_nodo = {
            'actividades': nuevas_actividades,
            'puntaje': nodo_actual['puntaje'] + datos['valor'],
            'tiempo': nodo_actual['tiempo'] + datos['tiempo']
        }
        sucesores.append(nuevo_nodo)
    return sucesores

# Función que implementa el algoritmo de búsqueda en anchura
def buscar_solucion(actividades):
    # Definir el nodo inicial con las actividades obligatorias
    nodo_inicial = {
        'actividades': set(obligatorias), 
        'puntaje': sum(actividades[a]['valor'] for a in actividades if actividades[a]['obligatorio'] == True) , 
        'tiempo': sum(actividades[a]['tiempo'] for a in actividades if actividades[a]['obligatorio'] == True)}
    frontera = [nodo_inicial]
    visitados = set()
    while frontera:
        # Tomar el primer nodo de la frontera
        nodo_actual = frontera.pop(0)
        # Si el puntaje del nodo actual es mayor o igual a 70, se ha encontrado una solución
        if nodo_actual['puntaje'] >= 70:
            return nodo_actual
        # Generar los sucesores del nodo actual
        sucesores = generar_sucesores(nodo_actual, actividades)
        # Agregar los sucesores a la frontera si no han sido visitados aún
        for sucesor in sucesores:
            if tuple(sucesor['actividades']) not in visitados:
                frontera.append(sucesor)
                visitados.add(tuple(sucesor['actividades']))
        # Si se llega a este punto, no se encontró solución
    return None

# Ejecutar la búsqueda y mostrar la solución encontrada
obligatorias = []


prueba={}
tiempoTotal = 0

for j in range(cantidadmaterias):
    if j != 0:
        print("materia: ", j) 
        for g in range(cantidadtemas):
            if g != 0:
                print("tema: ", g) 
                for i  in range(cantidadSubtemas):
                    if i != 0:
                        print("subtema: ", i) 
                        prueba={}
                        obligatorias = []
                        for actividad in actividades:
                            if actividades[actividad]['subtema'] == i and actividades[actividad]['materia'] == j and actividades[actividad]['tema'] == g:
                                prueba[actividad] = actividades[actividad]
                        for actividad, detalles in prueba.items():
                            if detalles['obligatorio']:
                                obligatorias.append(actividad)   
                        if prueba:             
                            solucion = buscar_solucion(prueba) 
                            if solucion:
                                print("Solución encontrada:", solucion['actividades'])
                                print("score:", solucion['puntaje'])
                                print("\n")
                                tiempoTotal = tiempoTotal + solucion['tiempo']
                            else:
                                print("no se completa el minimo requierido \n")    

print("Tiempo total:", tiempoTotal)

    

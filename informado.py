from queue import PriorityQueue

# Definir las actividades y sus relaciones de dependencia
actividades = {
    'Actividad 1': {'materia': 1, 'tema': 1, 'subtema': 1, 'valor': 10, 'tiempo': 2, 'depende': [], 'obligatorio': False },
    'Actividad 2': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 20, 'tiempo': 3, 'depende': ['Actividad 1'], 'obligatorio': False },
    'Actividad 3': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 10, 'tiempo': 2, 'depende': [], 'obligatorio': False },
    'Actividad 4': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 15, 'tiempo': 5, 'depende': ['Actividad 2', 'Actividad 3'], 'obligatorio': False },
    'Actividad 5': {'materia': 1,'tema': 1, 'subtema': 1, 'valor': 25, 'tiempo': 3, 'depende': ['Actividad 1'], 'obligatorio': False },
    'Actividad 6': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 10, 'tiempo': 2, 'depende': [], 'obligatorio': False },
    'Actividad 7': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 26, 'tiempo': 1, 'depende': [], 'obligatorio': False },
    'Actividad 8': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 14, 'tiempo': 3, 'depende': ['Actividad 7'], 'obligatorio': False },
    'Actividad 9': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 8, 'tiempo': 2, 'depende': ['Actividad 6', 'Actividad 8'], 'obligatorio': False },
    'Actividad 10': {'materia': 2,'tema': 1, 'subtema': 1, 'valor': 21, 'tiempo': 1, 'depende': [], 'obligatorio': False }
}

# Definir las actividades obligatorias
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

# Definir la función heurística para estimar el score mínimo restante
def heuristica(actividades_restantes):
    valor_total = sum(prueba[a]['valor'] for a in actividades_restantes)
    tiempo_total = sum(prueba[a]['tiempo'] for a in actividades_restantes)
    valor_total = valor_total + tiempo_total
    return valor_total



# Definir la función para expandir un nodo del árbol de búsqueda
def expandir_nodo(nodo):
    actividades_restantes = nodo['actividades_restantes']
    nuevas_actividades = []
    for a in actividades_restantes:
        if all(d in nodo['actividades_ejecutadas'] for d in prueba[a]['depende']):
            nuevas_actividades.append(a)
    nuevos_nodos = []
    for a in nuevas_actividades:
        nuevas_actividades_restantes = actividades_restantes - {a}
        nuevas_actividades_ejecutadas = nodo['actividades_ejecutadas'] | {a}
        nuevo_tiempo = nodo['tiempo'] + prueba[a]['tiempo']
        nuevo_score = sum(prueba[a]['valor'] for a in nuevas_actividades_ejecutadas)
        nuevo_nodo = {
            'actividades_restantes': nuevas_actividades_restantes,
            'actividades_ejecutadas': nuevas_actividades_ejecutadas,
            'tiempo': nuevo_tiempo,
            'score': nuevo_score,
            'heuristica': heuristica(nuevas_actividades_restantes)
        }
        nuevos_nodos.append(nuevo_nodo)
    return nuevos_nodos

# Definir la función para buscar la solución utilizando A*
def buscar_solucion():
   
    nodo_inicial = {
        'actividades_restantes': set(prueba.keys()) - set(obligatorias),
        'actividades_ejecutadas': set(obligatorias),
        'tiempo': sum(prueba[a]['tiempo'] for a in prueba if prueba[a]['obligatorio'] == True),
        'score': sum(prueba[a]['valor'] for a in prueba if prueba[a]['obligatorio'] == True)
    }
    nodo_inicial['heuristica'] = heuristica(nodo_inicial['actividades_restantes'])
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((nodo_inicial['heuristica'], nodo_inicial))
    while not cola_prioridad.empty():
        _, nodo_actual = cola_prioridad.get()
        if nodo_actual['score'] >= 70:
            return nodo_actual['actividades_ejecutadas'], nodo_actual['tiempo'], nodo_actual['score']
        nuevos_nodos = expandir_nodo(nodo_actual)
        for hijo in nuevos_nodos:
            if cola_prioridad.queue:
                if hijo['heuristica'] == comparar:
                    hijo['heuristica'] = hijo['heuristica'] + 1
                else:   
                    cola_prioridad.put((hijo['heuristica'], hijo))
                    comparar = hijo['heuristica']
            else:
                 cola_prioridad.put((hijo['heuristica'], hijo))
                 comparar = hijo['heuristica']

    return None


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
                            solucion = buscar_solucion() 
                            if solucion:
                                print("Actividades ejecutadas:", solucion[0])
                                print("score:", solucion[2])
                                print("\n")
                                tiempoTotal = tiempoTotal + solucion[1]
                            else:
                                print("no se completa el minimo requerido \n")    

print("Tiempo total:", tiempoTotal)

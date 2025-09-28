
# =======================================================================
# IMPORTACIONES LIGERAS GLOBALES (NO USAN NUMPY/MATPLOTLIB)
# Estas son las únicas que deben estar fuera de las funciones para ahorrar memoria al iniciar.
# =======================================================================

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
import random
import time
import math
from .data import RULETAS, FORMULAS, UNIDADES, get_formula_by_id
from .models import Archivo


# ===============================================
# Vistas Generales
# ===============================================

def index(request):
    return render(request, "index.html")

def graficador(request):
    return render(request, "graficador_jsx.html")

# ===============================================
# Vista Optimizada de Graficador
# ===============================================

def grafico_png(request):
    """
    Genera un gráfico PNG.
    Todas las importaciones pesadas (numpy, matplotlib) están DENTRO de esta función 
    para ahorrar memoria al iniciar el servidor (evitar SIGKILL).
    """
    try:
        # Importaciones pesadas MOVILIZADAS DENTRO DE LA FUNCIÓN
        import numpy as np
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from io import BytesIO
    except ImportError as e:
        # Esto te alertará si te faltan numpy o matplotlib en requirements.txt
        return HttpResponseBadRequest(f"Error: Librería de gráficos faltante. Verifica requirements.txt: {e}")

    f = request.GET.get("f", "sin")
    x = np.linspace(-10, 10, 400)
    
    if f == "sin": 
        y = np.sin(x)
    elif f == "cos":
        y = np.cos(x)
    else: 
        y = np.zeros_like(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    buf = BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig) # Cierra la figura para liberar memoria inmediatamente
    buf.seek(0)
    
    return HttpResponse(buf.getvalue(), content_type='image/png')


# ===============================================
# Vistas de Archivos
# ===============================================

def upload(request):
    if request.method == "POST" and request.FILES.get('archivo'):
        f = request.FILES['archivo']
        Archivo.objects.create(nombre=f.name, archivo=f)
        return redirect('archivos')
    return render(request, "upload.html")

def archivos(request):
    return render(request, "archivos.html") 

# ===============================================
# Vistas de Ruleta y Fórmulas
# ===============================================

def ruleta_general(request):
    if request.method == "POST":
        unidad_id = request.POST.get('unidad_id', '')
        participantes_raw = request.POST.get('participants', '').strip()

        resultado = {}
        
        # Lógica para seleccionar un participante
        if participantes_raw:
            participantes = [p.strip() for p in participantes_raw.split(",") if p.strip()]
            if participantes:
                elegido = random.choice(participantes)
                resultado['participante'] = elegido
        
        # Lógica para seleccionar un problema de la unidad
        if unidad_id and unidad_id in RULETAS:
            unidad_data = RULETAS.get(unidad_id)
            ejercicios = unidad_data.get('ejercicios') or []
            if ejercicios:
                ejercicio = random.choice(ejercicios)
                opciones = ejercicio.get('opciones', [])
                respuesta_correcta_raw = ejercicio.get('respuesta', '').strip()

                def norm(s):
                    return s.strip()

                opciones_marcadas = []
                for op in opciones:
                    opciones_marcadas.append({
                        'texto': op,
                        'es_correcta': norm(op) == norm(respuesta_correcta_raw)
                    })

                resultado.update({
                    'problema': ejercicio.get('problema', ''),
                    'opciones': opciones_marcadas,
                    'respuesta': ejercicio.get('respuesta', ''),
                    'explicacion': ejercicio.get('explicacion', ''),
                    'unidad_nombre': unidad_data.get('nombre_unidad')
                })
        
        # En caso de que no se haya seleccionado ni unidad ni participantes, se devuelve un error
        if not unidad_id and not participantes_raw:
             return JsonResponse({'error': 'Debes seleccionar una unidad o introducir al menos un participante.'}, status=400)
        
        return JsonResponse(resultado)

    unidades = RULETAS.items()
    return render(request, "ruleta_general.html", {"unidades": unidades})


def formulas_view(request):
    """
    Controla la navegación a través de las fórmulas por unidad.
    """
    context = {
        'unidades': UNIDADES,
        'selected_unidad': None,
        'formulas': None,
        'selected_formula_details': None,
    }

    # 1. Manejar selección de Unidad
    selected_unidad = request.GET.get('unidad')
    if selected_unidad and selected_unidad in FORMULAS:
        context['selected_unidad'] = selected_unidad
        context['formulas'] = FORMULAS.get(selected_unidad)

        # 2. Manejar selección de Fórmula
        formula_id = request.GET.get('formula_id')
        if formula_id:
            try:
                formula_id = int(formula_id)
                details = get_formula_by_id(formula_id)
                if details:
                    context['selected_formula_details'] = details
            except ValueError:
                pass # Ignorar ID no válido

    return render(request, 'formulario.html', context)

def ir_a_drive(request):
    """
    Esta vista simplemente renderiza la plantilla 'libro.html'.
    """
    return render(request, 'libro.html', {})

# ===============================================
# Vistas de Juegos (Aritmética y Sudoku)
# ===============================================

def generate_question(operation_type):
    """
    Genera una pregunta matemática basada en el tipo de operación.
    """
    if operation_type == 'addition':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation_type == 'subtraction':
        num1 = random.randint(20, 100)
        num2 = random.randint(1, 20)
        question = f"{num1} - {num2}"
        answer = num1 - num2
    elif operation_type == 'multiplication':
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        question = f"{num1} * {num2}"
        answer = num1 * num2
    elif operation_type == 'division':
        num2 = random.randint(1, 12)
        num1 = num2 * random.randint(1, 12)
        question = f"{num1} / {num2}"
        answer = num1 // num2
    elif operation_type == 'mixed':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 10)
        operator1 = random.choice(['+', '-', '*'])
        operator2 = random.choice(['+', '-'])
        # Usamos eval con precaución en datos no ingresados por el usuario
        question = f"({num1} {operator1} {num2}) {operator2} {num3}"
        answer = eval(question)
    elif operation_type == 'advanced':
        advanced_ops = ['power', 'log', 'root']
        op = random.choice(advanced_ops)
        if op == 'power':
            base = random.randint(2, 5)
            exponent = random.randint(2, 4)
            question = f"{base} ** {exponent}"
            answer = base ** exponent
        elif op == 'log':
            base = random.randint(2, 5)
            power = random.randint(2, 4)
            num = base ** power
            question = f"log{base}({num})"
            # Usamos math importado globalmente
            answer = round(math.log(num, base))
        elif op == 'root':
            perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
            num = random.choice(perfect_squares)
            question = f"sqrt({num})"
            # Usamos math importado globalmente
            answer = int(math.sqrt(num))
    else:
        return "Elige una operación para empezar.", None
    
    return question, answer

def select_difficulty(request):
    """
    Muestra la página de selección de dificultad.
    """
    return render(request, 'select_difficulty.html')

def juego_aritmetico(request):
    time_limit = 30 # Segundos por nivel

    if request.method == "POST":
        # Se recibe la selección de operación desde el formulario de dificultad
        operation_type = request.POST.get('operation')
        if operation_type:
            # Inicializar el juego
            request.session['operation_type'] = operation_type
            request.session['score'] = 0
            request.session['questions_answered'] = 0
            request.session['start_time'] = time.time()
            request.session['last_correct'] = None
            question, answer = generate_question(operation_type)
            request.session['correct_answer'] = answer
            request.session['question'] = question
            request.session['time_remaining'] = time_limit
            return redirect('juego_aritmetico')
        
        # Lógica de juego, si el formulario POST no es de la selección inicial
        user_answer = request.POST.get('answer')
        correct_answer = request.session.get('correct_answer')
        
        # Validar la respuesta del usuario
        if user_answer and correct_answer is not None and int(user_answer) == correct_answer:
            request.session['score'] += 1
            request.session['questions_answered'] += 1
            request.session['last_correct'] = True
        else:
            request.session['last_correct'] = False

        # Generar una nueva pregunta
        operation_type = request.session.get('operation_type')
        if operation_type: # Asegurarse de que el tipo de operación esté en la sesión
             question, answer = generate_question(operation_type)
             request.session['correct_answer'] = answer
             request.session['question'] = question
        
        return redirect('juego_aritmetico')
    
    else: # GET request, para mostrar la pantalla de juego o fin de juego
        # Si no hay un tipo de operación en la sesión, redirigir a la selección
        if 'operation_type' not in request.session:
            return redirect('select_difficulty')

        # Calcular el tiempo restante para la plantilla
        elapsed_time = int(time.time() - request.session.get('start_time', 0))
        time_remaining = time_limit - elapsed_time

        context = {
            'question': request.session.get('question', 'Error de sesión'),
            'score': request.session.get('score', 0),
            'time_remaining': time_remaining,
            'last_correct': request.session.get('last_correct', None),
        }

        # Reiniciar el juego si el tiempo se ha agotado
        if time_remaining <= 0:
            final_score = request.session.get('score', 0)
            request.session.flush() # Limpiar la sesión para un nuevo juego
            return render(request, 'juego_aritmetico_fin.html', {'score': final_score})

        return render(request, 'juego_aritmetico.html', context)


def generar_tablero_sudoku():
    """
    Genera un tablero de Sudoku válido y resuelto, y luego oculta
    un número de celdas para crear el puzle.
    """
    def crear_tablero_resuelto(tablero):
        """
        Función recursiva de backtracking para llenar el tablero de Sudoku.
        """
        for fila in range(9):
            for columna in range(9):
                if tablero[fila][columna] == 0:
                    numeros = list(range(1, 10))
                    random.shuffle(numeros) 
                    for num in numeros:
                        if es_valido(tablero, fila, columna, num):
                            tablero[fila][columna] = num
                            if crear_tablero_resuelto(tablero):
                                return True
                            tablero[fila][columna] = 0 
                    return False
        return True

    def es_valido(tablero, fila, columna, num):
        """
        Verifica si el número 'num' es válido en la posición (fila, columna)
        """
        # Chequea la fila
        if num in tablero[fila]:
             return False

        # Chequea la columna
        for x in range(9):
            if tablero[x][columna] == num:
                return False

        # Chequea la subcuadrícula de 3x3
        fila_inicial = fila - fila % 3
        columna_inicial = columna - columna % 3
        for i in range(3):
            for j in range(3):
                if tablero[i + fila_inicial][j + columna_inicial] == num:
                    return False

        return True

    # 1. Crea un tablero vacío de 9x9
    tablero_completo = [[0 for _ in range(9)] for _ in range(9)]

    # 2. Llena el tablero usando el algoritmo de backtracking
    crear_tablero_resuelto(tablero_completo)

    # 3. Copia el tablero resuelto para crear el puzle
    tablero_puzle = [fila[:] for fila in tablero_completo]

    # 4. Elimina un número aleatorio de celdas
    celdas_a_ocultar = 40 
    celdas_ocultas = 0
    while celdas_ocultas < celdas_a_ocultar:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if tablero_puzle[fila][columna] != 0:
            tablero_puzle[fila][columna] = 0
            celdas_ocultas += 1

    return tablero_puzle

def sudoku_juego(request):
    """
    Vista principal que renderiza el template del juego.
    """
    if request.method == 'GET':
        tablero_inicial = generar_tablero_sudoku()
        return render(request, 'sudoku.html', {'tablero': tablero_inicial})

    elif request.method == 'POST':
        try:
             import json
             data = json.loads(request.body)
             tablero_usuario = data.get('tablero', [])
             return JsonResponse({'completado': True})
        except ImportError:
             # Si json no está importado globalmente
             import json 
             data = json.loads(request.body)
             tablero_usuario = data.get('tablero', [])
             return JsonResponse({'completado': True})
        except json.JSONDecodeError:
             return HttpResponseBadRequest("Datos POST inválidos.")
    
# --- Lógica del juego 24 (Sin cambios) ---
def generar_numeros(min_num=1, max_num=10, cantidad=4):
    """Genera una lista de números aleatorios."""
    return [random.randint(min_num, max_num) for _ in range(cantidad)]

def generar_objetivo(min_target=10, max_target=50):
    """Genera un número objetivo aleatorio."""
    return random.randint(min_target, max_target)

def juego_24(request):
    """Vista principal del juego. Renderiza el template y pasa los números."""
    
    numeros = generar_numeros()
    objetivo = generar_objetivo()
    
    contexto = {
        'numeros': numeros,
        'objetivo': objetivo,
        'numeros_js': ','.join(map(str, numeros)) 
    }
    
    return render(request, 'juego_24.html', contexto)
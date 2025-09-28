from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, Http404
from io import BytesIO
import random, time, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from .data import RULETAS, FORMULAS, UNIDADES, get_formula_by_id
from .models import Archivo


# ----------------- VISTAS BÁSICAS -----------------
def index(request):
    return render(request, "index.html")


def graficador(request):
    return render(request, "graficador_jsx.html")


def grafico_png(request):
    f = request.GET.get("f", "sin")
    x = np.linspace(-10, 10, 400)
    y = np.sin(x) if f == "sin" else np.zeros_like(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    buf = BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')


def upload(request):
    if request.method == "POST" and request.FILES.get('archivo'):
        f = request.FILES['archivo']
        Archivo.objects.create(nombre=f.name, archivo=f)
        return redirect('archivos')
    return render(request, "upload.html")


def archivos(request):
    archivos = Archivo.objects.all()
    return render(request, "archivos.html", {"archivos": archivos})


# ----------------- RULETA -----------------
def ruleta_general(request):
    if request.method == "POST":
        unidad_id = request.POST.get('unidad_id', '')
        participantes_raw = request.POST.get('participants', '').strip()
        resultado = {}

        # Participantes
        if participantes_raw:
            participantes = [p.strip() for p in participantes_raw.split(",") if p.strip()]
            if participantes:
                resultado['participante'] = random.choice(participantes)

        # Problema de unidad
        if unidad_id and unidad_id in RULETAS:
            unidad_data = RULETAS[unidad_id]
            ejercicios = unidad_data.get('ejercicios', [])
            if ejercicios:
                ejercicio = random.choice(ejercicios)
                opciones = ejercicio.get('opciones', [])
                respuesta_correcta = ejercicio.get('respuesta', '').strip()

                opciones_marcadas = [
                    {"texto": op, "es_correcta": op.strip() == respuesta_correcta}
                    for op in opciones
                ]

                resultado.update({
                    'problema': ejercicio.get('problema', ''),
                    'opciones': opciones_marcadas,
                    'respuesta': ejercicio.get('respuesta', ''),
                    'explicacion': ejercicio.get('explicacion', ''),
                    'unidad_nombre': unidad_data.get('nombre_unidad')
                })

        if not unidad_id and not participantes_raw:
            return JsonResponse({'error': 'Debes seleccionar una unidad o introducir al menos un participante.'}, status=400)

        return JsonResponse(resultado)

    return render(request, "ruleta_general.html", {"unidades": RULETAS.items()})


# ----------------- FORMULAS -----------------
def formulas_view(request):
    context = {
        'unidades': UNIDADES,
        'selected_unidad': None,
        'formulas': None,
        'selected_formula_details': None,
    }

    selected_unidad = request.GET.get('unidad')
    if selected_unidad and selected_unidad in FORMULAS:
        context['selected_unidad'] = selected_unidad
        context['formulas'] = FORMULAS[selected_unidad]

        formula_id = request.GET.get('formula_id')
        if formula_id:
            try:
                formula_id = int(formula_id)
                details = get_formula_by_id(formula_id)
                if details:
                    context['selected_formula_details'] = details
            except ValueError:
                pass

    return render(request, 'formulario.html', context)


def ir_a_drive(request):
    return render(request, 'libro.html', {})


# ----------------- JUEGO ARITMÉTICO -----------------
def generate_question(operation_type):
    """Genera una pregunta matemática basada en el tipo de operación."""
    if operation_type == 'addition':
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        return f"{num1} + {num2}", num1 + num2
    elif operation_type == 'subtraction':
        num1, num2 = random.randint(20, 100), random.randint(1, 20)
        return f"{num1} - {num2}", num1 - num2
    elif operation_type == 'multiplication':
        num1, num2 = random.randint(1, 12), random.randint(1, 12)
        return f"{num1} * {num2}", num1 * num2
    elif operation_type == 'division':
        num2 = random.randint(1, 12)
        num1 = num2 * random.randint(1, 12)
        return f"{num1} / {num2}", num1 // num2
    elif operation_type == 'mixed':
        num1, num2, num3 = random.randint(1, 20), random.randint(1, 20), random.randint(1, 10)
        op1, op2 = random.choice(['+', '-', '*']), random.choice(['+', '-'])
        return f"({num1} {op1} {num2}) {op2} {num3}", eval(f"({num1} {op1} {num2}) {op2} {num3}")
    elif operation_type == 'advanced':
        op = random.choice(['power', 'log', 'root'])
        if op == 'power':
            base, exp = random.randint(2, 5), random.randint(2, 4)
            return f"{base} ** {exp}", base ** exp
        elif op == 'log':
            base, exp = random.randint(2, 5), random.randint(2, 4)
            num = base ** exp
            return f"log{base}({num})", round(math.log(num, base))
        elif op == 'root':
            num = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
            return f"sqrt({num})", int(math.sqrt(num))
    return "Elige una operación para empezar.", None


def select_difficulty(request):
    return render(request, 'select_difficulty.html')


def juego_aritmetico(request):
    time_limit = 30
    if request.method == "POST":
        operation_type = request.POST.get('operation')
        if operation_type:
            request.session.update({
                'operation_type': operation_type,
                'score': 0,
                'questions_answered': 0,
                'start_time': time.time(),
                'last_correct': None
            })
            question, answer = generate_question(operation_type)
            request.session['correct_answer'] = answer
            request.session['question'] = question
            return redirect('juego_aritmetico')

        user_answer = request.POST.get('answer')
        if user_answer and str(request.session.get('correct_answer')) == user_answer:
            request.session['score'] += 1
            request.session['last_correct'] = True
        else:
            request.session['last_correct'] = False

        question, answer = generate_question(request.session['operation_type'])
        request.session['correct_answer'] = answer
        request.session['question'] = question
        return redirect('juego_aritmetico')

    if 'operation_type' not in request.session:
        return redirect('select_difficulty')

    elapsed = int(time.time() - request.session.get('start_time', 0))
    remaining = time_limit - elapsed

    context = {
        'question': request.session['question'],
        'score': request.session['score'],
        'time_remaining': max(remaining, 0),
        'last_correct': request.session['last_correct']
    }

    if remaining <= 0:
        request.session.flush()
        context['time_remaining'] = 0

    return render(request, 'juego_aritmetico.html', context)


# ----------------- SUDOKU -----------------
def generar_tablero_sudoku():
    def es_valido(tablero, fila, columna, num):
        if num in tablero[fila]: return False
        if num in [tablero[x][columna] for x in range(9)]: return False
        fi, ci = fila - fila % 3, columna - columna % 3
        for i in range(3):
            for j in range(3):
                if tablero[fi + i][ci + j] == num:
                    return False
        return True

    def crear_tablero_resuelto(tablero):
        for fila in range(9):
            for columna in range(9):
                if tablero[fila][columna] == 0:
                    numeros = list(range(1, 10))
                    random.shuffle(numeros)
                    for num in numeros:
                        if es_valido(tablero, fila, columna, num):
                            tablero[fila][columna] = num
                            if crear_tablero_resuelto(tablero): return True
                            tablero[fila][columna] = 0
                    return False
        return True

    tablero = [[0] * 9 for _ in range(9)]
    crear_tablero_resuelto(tablero)
    puzzle = [fila[:] for fila in tablero]

    ocultar = 40
    while ocultar > 0:
        f, c = random.randint(0, 8), random.randint(0, 8)
        if puzzle[f][c] != 0:
            puzzle[f][c] = 0
            ocultar -= 1
    return puzzle


def sudoku_juego(request):
    tablero_inicial = generar_tablero_sudoku()
    return render(request, 'sudoku.html', {'tablero': tablero_inicial})


# ----------------- JUEGO 24 -----------------
def generar_numeros(min_num=1, max_num=10, cantidad=4):
    return [random.randint(min_num, max_num) for _ in range(cantidad)]


def generar_objetivo(min_target=10, max_target=50):
    return random.randint(min_target, max_target)


def juego_24(request):
    numeros = generar_numeros()
    objetivo = generar_objetivo()
    return render(request, 'juego_24.html', {
        'numeros': numeros,
        'objetivo': objetivo,
        'numeros_js': ','.join(map(str, numeros))
    })

RULETAS = {

  "unidad1": {
      "nombre_unidad": "Unidad 1 - Sucesiones (Comprobemos lo aprendido)",
      "ejercicios": [
          {
            "problema": "Complete: 4, 8, __, 16, __, 24, … ¿Cuáles son los dos términos faltantes?",
            "respuesta": "12; 20",
            "explicacion": "La sucesión crece de +4: 4,8,12,16,20,24. Faltan 12 y 20.",
            "opciones": ["10; 12", "12; 20", "6; 10", "8; 14"]
          },
          {
            "problema": "Término general de la sucesión 3, 6, 9, 12, …",
            "respuesta": "a_n = 3n",
            "explicacion": "La diferencia común es 3. Para n=1 -> 3, se tiene a_n = 3n.",
            "opciones": ["a_n = 3n", "a_n = n+2", "a_n = 3n+1", "a_n = 2n+1"]
          },
          {
            "problema": "Dada la sucesión aritmética con a1=5 y a8=40, calcule S8 (suma de los 8 primeros términos).",
            "respuesta": "S8 = 180",
            "explicacion": "d = (40-5)/7 =5. S8 = 8/2*(5+40)=4*45=180.",
            "opciones": ["S8 = 180", "S8 = 145", "S8 = 200", "S8 = 160"]
          }
      ]
  },
  
  "unidad2": {
      "nombre_unidad": "Unidad 2 - Potenciación y Exponenciales (Comprobemos lo aprendido)",
      "ejercicios": [
          {
            "problema": "Calcule: 2^3 * 2^4",
            "respuesta": "128",
            "explicacion": "2^3 * 2^4 = 2^(3+4) = 2^7 = 128.",
            "opciones": ["128", "64", "32", "256"]
          },
          {
            "problema": "Resuelva: 4^(x+1) = 64",
            "respuesta": "x = 2",
            "explicacion": "64 = 4^3 => x+1=3 => x=2.",
            "opciones": ["x=2", "x=3", "x=1", "x=0"]
          }
      ]
  },
  
  "unidad3": {
      "nombre_unidad": "Unidad 3 - Logaritmos (Comprobemos lo aprendido)",
      "ejercicios": [
          {
            "problema": "Calcule log_2(32).",
            "respuesta": "5",
            "explicacion": "2^5 = 32.",
            "opciones": ["5", "4", "6", "10"]
          },
          {
            "problema": "Resuelva: log_2(x) = -5.",
            "respuesta": "1/32",
            "explicacion": "x = 2^{-5} = 1/32.",
            "opciones": ["1/32", "32", "-5", "2^5"]
          }
      ]
  },

  "unidad4": {
      "nombre_unidad": "Unidad 4 - Geometría Analítica (Comprobemos lo aprendido)",
      "ejercicios": [
          {
            "problema": "Encuentre la ecuación de la recta que pasa por (0,3) y tiene pendiente m=2.",
            "respuesta": "y = 2x + 3",
            "explicacion": "y - 3 = 2(x - 0) => y = 2x + 3.",
            "opciones": ["y = 2x + 3", "y = -2x + 3", "y = 3x + 2", "x = 3"]
          }
      ]
  },

  "unidad5": {
      "nombre_unidad": "Unidad 5 - Cónicas (Comprobemos lo aprendido)",
      "ejercicios": [
          {
            "problema": "Dada la elipse (x^2/25)+(y^2/16)=1, encuentre su centro, vértices y focos.",
            "respuesta": "Centro (0,0), Vértices (±5,0), Focos (±3,0)",
            "explicacion": "a^2=25 => a=5; b^2=16 => c^2=a^2-b^2=9 => c=3.",
            "opciones": ["Centro (0,0), Vértices (±5,0), Focos (±3,0)", "Centro (0,0), Vértices (±4,0), Focos (±2,0)", "Centro (0,0), Vértices (0,±5), Focos (±3,0)", "Centro (0,0), Vértices (±5,0), Focos (0,±3)"]
          }
      ]
  },
  
  "unidad6": {
      "nombre_unidad": "Unidad 6 - Técnicas de Conteo y Probabilidades (Comprobemos lo aprendido)",
      "ejercicios": [
          {
            "problema": "Se lanzan tres monedas. Probabilidad de obtener exactamente dos caras (escudos) y una cruz (número).",
            "respuesta": "3/8",
            "explicacion": "Combinaciones favorables: 3 (EEN, ENE, NEE) / 8 totales.",
            "opciones": ["3/8", "1/2", "1/4", "1/8"]
          },
          {
            "problema": "En una urna con 5 blancas, 10 verdes y 8 amarillas, probabilidad de extraer una verde.",
            "respuesta": "10/23",
            "explicacion": "10 favorables de 23 totales.",
            "opciones": ["10/23", "5/23", "8/23", "1/3"]
          },
          {
            "problema": "En el lanzamiento de dos dados, probabilidad de obtener suma 7.",
            "respuesta": "6/36 = 1/6",
            "explicacion": "Hay 6 combinaciones que suman 7 entre 36 totales.",
            "opciones": ["1/6", "1/4", "1/3", "1/12"]
          }
      ]
  }
}

ellipse_exercises = [
    {"problema":"(x^2/25)+(y^2/16)=1","respuesta":"Elipse ejemplo","explicacion":"a=5,b=4"}
]

# Archivo: formulas_matematicas_11mo_con_ejemplos.py

FORMULAS= {
    "Unidad 1: Sucesiones": [
        {
            "id": 101,
            "nombre": "Término general (Aritmética)",
            "formula": "a_n = a_1 + (n-1)d",
            "descripcion": "Calcula el enésimo término de una sucesión aritmética, donde 'd' es la diferencia común y 'a_1' el primer término.",
            "ejemplo": "Dada la sucesión (5, 8, 11, ...), con a₁=5 y d=3. El término general es a_{n} = 5 + (n-1)3."
        },
        {
            "id": 102,
            "nombre": "Suma de n términos (Aritmética)",
            "formula": "S_n = (n * (a_1 + a_n)) / 2",
            "descripcion": "Calcula la suma de los primeros 'n' términos de una sucesión aritmética.",
            "ejemplo": "La suma de los primeros 10 términos de la sucesión donde a₁=2 y a₁₀=20 es S₁₀ = (10(2 + 20))/2 = 110."
        },
        {
            "id": 103,
            "nombre": "Término general (Geométrica)",
            "formula": "a_n = a_1 * r^(n-1)",
            "descripcion": "Calcula el enésimo término de una sucesión geométrica, donde 'r' es la razón común y 'a_1' el primer término.",
            "ejemplo": "Dada la sucesión (3, 6, 12, ...), con a₁=3 y r=2. El término general es a_{n} = 3 * 2^{n-1}."
        },
        {
            "id": 104,
            "nombre": "Suma de n términos (Geométrica, r != 1)",
            "formula": "S_n = (a_1 * (r^n - 1)) / (r - 1)",
            "descripcion": "Calcula la suma de los primeros 'n' términos de una sucesión geométrica.",
            "ejemplo": "La suma de los primeros 4 términos de la sucesión donde a₁=2 y r=3 es S₄ = (2(3⁴ - 1))/(3 - 1) = 80."
        },
        {
            "id": 105,
            "nombre": "Notación de Sumatoria (Sigma)",
            "formula": "S = Sum_{k=1}^{n} a_k",
            "descripcion": "Representa la suma de los términos desde el índice k=1 hasta n.",
            "ejemplo": "La expresión Sum_{k=1}^{4} 2k representa la suma 2(1) + 2(2) + 2(3) + 2(4) = 20."
        }
    ],
    "Unidad 2: Potenciación y Funciones Exponenciales": [
        {
            "id": 201,
            "nombre": "Multiplicación de bases iguales",
            "formula": "a^m * a^n = a^{m+n}",
            "descripcion": "Al multiplicar potencias con la misma base, se suman los exponentes.",
            "ejemplo": "2³ * 2⁴ = 2^{3+4} = 2⁷ = 128."
        },
        {
            "id": 202,
            "nombre": "Potencia de una potencia",
            "formula": "(a^m)^n = a^{m * n}",
            "descripcion": "Al elevar una potencia a otro exponente, se multiplican los exponentes.",
            "ejemplo": "(5² )³ = 5^{2 * 3} = 5⁶ = 15625."
        },
        {
            "id": 203,
            "nombre": "División de bases iguales",
            "formula": "a^m / a^n = a^{m-n}",
            "descripcion": "Al dividir potencias con la misma base, se restan los exponentes.",
            "ejemplo": "x⁷ / x³ = x⁴."
        },
        {
            "id": 204,
            "nombre": "Exponente negativo",
            "formula": "a^{-n} = 1 / a^n",
            "descripcion": "Convierte un exponente negativo en un exponente positivo en el denominador de una fracción.",
            "ejemplo": "4^{-2} = 1 / 4^{2} = 1 / 16."
        },
        {
            "id": 205,
            "nombre": "Multiplicación de radicales",
            "formula": "sqrt[n]{a} * sqrt[n]{b} = sqrt[n]{a * b}",
            "descripcion": "El producto de radicales con el mismo índice es igual a la raíz del producto.",
            "ejemplo": "sqrt[3]{4} * sqrt[3]{2} = sqrt[3]{8} = 2."
        },
        {
            "id": 206,
            "nombre": "Propiedad de ecuaciones exponenciales",
            "formula": "Si a^p = a^q, entonces p = q",
            "descripcion": "Si las bases son iguales (y a ≠ 0, 1, -1), los exponentes deben ser iguales.",
            "ejemplo": "Si 2^{x} = 2⁵, entonces x = 5."
        }
    ],
    "Unidad 3: Logaritmo y Funciones Logarítmicas": [
        {
            "id": 301,
            "nombre": "Definición de logaritmo",
            "formula": "log_a M = x <=> M = a^x",
            "descripcion": "Establece la relación entre la forma logarítmica y la forma exponencial.",
            "ejemplo": "log₂ 8 = 3 <=> 8 = 2³."
        },
        {
            "id": 302,
            "nombre": "Logaritmo de un producto",
            "formula": "log_a (M * N) = log_a M + log_a N",
            "descripcion": "El logaritmo de un producto es la suma de los logaritmos.",
            "ejemplo": "log₁₀ (5 * 2) = log₁₀ 5 + log₁₀ 2."
        },
        {
            "id": 303,
            "nombre": "Logaritmo de una potencia",
            "formula": "log_a M^k = k * log_a M",
            "descripcion": "El logaritmo de una potencia es el exponente por el logaritmo de la base.",
            "ejemplo": "log₂ 16 = log₂ 2⁴ = 4 * log₂ 2 = 4(1) = 4."
        },
        {
            "id": 304,
            "nombre": "Fórmula de Cambio de Base",
            "formula": "log_a M = (log_b M) / (log_b a)",
            "descripcion": "Permite calcular un logaritmo en base 'a' usando una nueva base 'b'.",
            "ejemplo": "log₃ 10 = (log₁₀ 10) / (log₁₀ 3) ≈ 1 / 0.4771."
        }
    ],
    "Unidad 4: Geometría Analítica": [
        {
            "id": 401,
            "nombre": "Coordenada x de punto que divide en razón m:n",
            "formula": "x = (n * x_1 + m * x_2) / (m + n)",
            "descripcion": "Calcula la coordenada x del punto que divide un segmento con extremos (x₁, y₁) y (x₂, y₂) en una razón dada (m:n).",
            "ejemplo": "Para A(1, 0) y B(5, 0) en razón 1:1, la coordenada x es x = (1(1) + 1(5)) / (1 + 1) = 3."
        },
        {
            "id": 402,
            "nombre": "Circunferencia (Ordinaria, centro (h, k))",
            "formula": "(x-h)² + (y-k)² = r²",
            "descripcion": "Ecuación de una circunferencia con centro en (h, k) y radio 'r'.",
            "ejemplo": "Una circunferencia con centro en (3, -2) y radio 4 tiene la ecuación (x-3)² + (y+2)² = 16."
        }
    ],
    "Unidad 5: Cónicas": [
        {
            "id": 501,
            "nombre": "Parábola (Vértice en (0, 0), foco eje y)",
            "formula": "x² = 4py",
            "descripcion": "Ecuación de una parábola vertical con vértice en el origen, donde 'p' es la distancia del foco al vértice.",
            "ejemplo": "Una parábola con foco en (0, 3) tiene p=3, y su ecuación es x² = 4(3)y, o sea, x² = 12y."
        },
        {
            "id": 502,
            "nombre": "Elipse (Canónica, centro (0, 0), focos eje x)",
            "formula": "x² / a² + y² / b² = 1",
            "descripcion": "Ecuación de una elipse horizontal con centro en el origen, donde 'a' es el semieje mayor y 'b' el semieje menor.",
            "ejemplo": "Si a=5 y b=3, la ecuación es x² / 25 + y² / 9 = 1."
        },
        {
            "id": 503,
            "nombre": "Relación fundamental (Elipse)",
            "formula": "c² = a² - b²",
            "descripcion": "Relaciona la distancia del centro a los vértices ('a'), a los extremos del eje menor ('b'), y a los focos ('c').",
            "ejemplo": "Si a=5 y b=3, entonces c² = 5² - 3² = 16, por lo tanto, c=4 (distancia focal)."
        },
        {
            "id": 504,
            "nombre": "Hipérbola (Canónica, centro (0, 0), focos eje x)",
            "formula": "x² / a² - y² / b² = 1",
            "descripcion": "Ecuación de una hipérbola horizontal con centro en el origen.",
            "ejemplo": "Una hipérbola con a=4 y b=3 tiene la ecuación x² / 16 - y² / 9 = 1."
        },
        {
            "id": 505,
            "nombre": "Asíntotas (Hipérbola, focos eje x)",
            "formula": "y = +/- (b/a) * x",
            "descripcion": "Ecuación de las líneas asíntotas que guían las ramas de una hipérbola horizontal.",
            "ejemplo": "Para la hipérbola x² / 16 - y² / 9 = 1 (a=4, b=3), las asíntotas son y = +/- (3/4)x."
        }
    ],
    "Unidad 6: Técnicas de Conteo y Probabilidades": [
        {
            "id": 601,
            "nombre": "Probabilidad Teórica",
            "formula": "P(A) = n(A) / n(E)",
            "descripcion": "Calcula la probabilidad de un evento como la razón entre casos favorables 'n(A)' y casos posibles 'n(E)'.",
            "ejemplo": "La probabilidad de sacar un 5 en un dado de 6 caras es P(5) = 1/6."
        },
        {
            "id": 602,
            "nombre": "Regla de la Adición (Eventos cualesquiera)",
            "formula": "P(A U B) = P(A) + P(B) - P(A n B)",
            "descripcion": "Calcula la probabilidad de que ocurra el evento A o el evento B.",
            "ejemplo": "P(par o 5) = P(par) + P(5) - P(par y 5) = 3/6 + 1/6 - 0/6 = 4/6."
        },
        {
            "id": 603,
            "nombre": "Regla de la Adición (Eventos mutuamente excluyentes)",
            "formula": "P(A U B) = P(A) + P(B)",
            "descripcion": "Calcula la probabilidad de la unión de dos eventos que no pueden ocurrir simultáneamente.",
            "ejemplo": "P(par o impar) = P(par) + P(impar) = 3/6 + 3/6 = 1."
        },
        {
            "id": 604,
            "nombre": "Probabilidad Condicional (A dado B)",
            "formula": "P(A|B) = P(A n B) / P(B)",
            "descripcion": "Calcula la probabilidad de que ocurra A, dado que B ya ha ocurrido.",
            "ejemplo": "P(sacar 6 | sacar par) = P(sacar 6 y par) / P(sacar par) = (1/6) / (3/6) = 1/3."
        },
        {
            "id": 605,
            "nombre": "Regla de la Multiplicación (Eventos independientes)",
            "formula": "P(A n B) = P(A) * P(B)",
            "descripcion": "Calcula la probabilidad de que los eventos A y B ocurran simultáneamente o en secuencia.",
            "ejemplo": "P(cara en moneda y 5 en dado) = P(cara) * P(5) = (1/2) * (1/6) = 1/12."
        }
    ]
}

# --- Funciones auxiliares para la vista Django ---

def get_formula_by_id(formula_id):
    """Busca y retorna una fórmula por su ID único."""
    for formulas in FORMULAS.values():
        for formula in formulas:
            if formula.get("id") == formula_id:
                return formula
    return None

UNIDADES = list(FORMULAS.keys())

# Este código define la estructura de datos que usarás en tu archivo views.py
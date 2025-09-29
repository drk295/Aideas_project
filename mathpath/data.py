
RULETAS = {
  "unidad1": {
    "nombre_unidad": "Unidad 1 - Sucesiones (Comprobemos lo aprendido)",
    "ejercicios": [
      {
        "problema": "Complete: 4, 8, __, 16, __, 24, …. ¿Cuáles son los dos términos faltantes?",
        "respuesta": "12; 20",
        "explicacion": "Sucesión aritmética con diferencia d=4. Los términos son 4, 8, 12, 16, 20, 24. Faltan 12 y 20.",
        "opciones": ["10; 12", "12; 20", "6; 10", "8; 14"]
      },
      {
        "problema": "Calcule el término general $a_n$ de la sucesión: 3, 6, 9, 12, …",
        "respuesta": "$a_n = 3n$",
        "explicacion": "Es una sucesión aritmética con $a_1=3$ y $d=3$. El término general es $a_n = 3 + (n-1)3 = 3n$.",
        "opciones": ["$a_n = 3n$", "$a_n = n+2$", "$a_n = 3n+1$", "$a_n = 2n+1$"]
      },
      {
        "problema": "Calcule el término general $a_n$ de la sucesión: -1, -2, -3, -4, …",
        "respuesta": "$a_n = -n$",
        "explicacion": "El término 'n' multiplicado por -1 genera la sucesión.",
        "opciones": ["$a_n = n-2$", "$a_n = 1-n$", "$a_n = -n$", "$a_n = -2n+1$"]
      },
      {
        "problema": "Calcule el término general $a_n$ de la sucesión: 1/2, 2/3, 3/4, 4/5, …",
        "respuesta": "$a_n = n/(n+1)$",
        "explicacion": "El numerador es 'n' y el denominador es 'n+1'.",
        "opciones": ["$a_n = n/(n+1)$", "$a_n = (n-1)/n$", "$a_n = 1/2n$", "$a_n = 2n/(n+1)$"]
      },
      {
        "problema": "Calcule el término $a_{15}$ para la sucesión con término general $a_n = -n$.",
        "respuesta": "$a_{15} = -15$",
        "explicacion": "Sustituyendo $n=15$, se tiene $a_{15} = -15$.",
        "opciones": ["$a_{15} = 15$", "$a_{15} = -15$", "$a_{15} = -14$", "$a_{15} = 0$"]
      },
      {
        "problema": "Dada la sucesión aritmética con $a_1=5$ y $a_8=40$, calcule $S_8$ (suma de los 8 primeros términos).",
        "respuesta": "$S_8 = 180$",
        "explicacion": "Se utiliza la fórmula $S_n = n/2 \\cdot (a_1 + a_n)$. $S_8 = 8/2 \\cdot (5 + 40) = 4 \\cdot 45 = 180$.",
        "opciones": ["$S_8 = 180$", "$S_8 = 145$", "$S_8 = 200$", "$S_8 = 160$"]
      },
      {
        "problema": "Dada la sucesión aritmética 5, 11, 17, …, calcule el término $a_5$.",
        "respuesta": "$a_5 = 29$",
        "explicacion": "$a_1=5$, $d=6$. $a_5 = a_1 + 4d = 5 + 4(6) = 29$.",
        "opciones": ["$a_5 = 23$", "$a_5 = 35$", "$a_5 = 29$", "$a_5 = 27$"]
      },
      {
        "problema": "Dada una sucesión aritmética con $d=3$ y $a_4=5$, calcule el primer término $a_1$.",
        "respuesta": "$a_1 = -4$",
        "explicacion": "$a_4 = a_1 + 3d \\Rightarrow 5 = a_1 + 3(3) \\Rightarrow a_1 = 5 - 9 = -4$.",
        "opciones": ["$a_1 = 2$", "$a_1 = -4$", "$a_1 = 8$", "$a_1 = -1$"]
      },
      {
        "problema": "Dada una sucesión aritmética con $a_1=4$ y $a_3=16$, calcule la diferencia común $d$.",
        "respuesta": "$d = 6$",
        "explicacion": "$a_3 = a_1 + 2d \\Rightarrow 16 = 4 + 2d \\Rightarrow 12 = 2d \\Rightarrow d = 6$.",
        "opciones": ["$d = 4$", "$d = 6$", "$d = 8$", "$d = 12$"]
      },
      {
        "problema": "Calcule la suma de la sucesión aritmética: 1, 4, 7, …, 19.",
        "respuesta": "$S_n = 70$",
        "explicacion": "$a_1=1$, $d=3$, $a_n=19$. Se halla $n=7$. $S_7 = 7/2 \\cdot (1+19) = 70$.",
        "opciones": ["$S_n = 56$", "$S_n = 63$", "$S_n = 70$", "$S_n = 77$"]
      },
      {
        "problema": "En la sucesión geométrica 1, 4, 16, ___, ___, calcule la razón común ($r$).",
        "respuesta": "$r = 4$",
        "explicacion": "La razón se calcula dividiendo un término por el anterior: $4/1 = 4$.",
        "opciones": ["$r = 3$", "$r = 4$", "$r = 5$", "$r = 16$"]
      },
      {
        "problema": "Dada la sucesión geométrica 5, 15, 45, …, determine el término $a_5$.",
        "respuesta": "$a_5 = 405$",
        "explicacion": "$a_1=5$, $r=3$. $a_5 = a_1 \\cdot r^{5-1} = 5 \\cdot 3^4 = 5 \\cdot 81 = 405$.",
        "opciones": ["$a_5 = 135$", "$a_5 = 405$", "$a_5 = 243$", "$a_5 = 1215$"]
      },
      {
        "problema": "Calcule $a_1$ para una sucesión geométrica con $r=2$ y $a_4=64$.",
        "respuesta": "$a_1 = 8$",
        "explicacion": "$a_4 = a_1 \\cdot r^3 \\Rightarrow 64 = a_1 \\cdot 2^3 \\Rightarrow 64 = 8 \\cdot a_1 \\Rightarrow a_1 = 8$.",
        "opciones": ["$a_1 = 32$", "$a_1 = 8$", "$a_1 = 16$", "$a_1 = 4$"]
      },
      {
        "problema": "Calcule la suma $S_3$ para la sucesión geométrica con $a_1=1$ y $r=4$.",
        "respuesta": "$S_3 = 21$",
        "explicacion": "$S_3 = 1 \\cdot (1 - 4^3) / (1 - 4) = (1 - 64) / -3 = -63 / -3 = 21$.",
        "opciones": ["$S_3 = 16$", "$S_3 = 21$", "$S_3 = 64$", "$S_3 = 17$"]
      },
      {
        "problema": "Exprese la suma $1+2+3+\\cdots+10$ usando la notación Sigma.",
        "respuesta": "$\\Sigma_{k=1}^{10} k$",
        "explicacion": "La sumatoria es de los primeros 10 números enteros, comenzando en $k=1$.",
        "opciones": ["$\\Sigma_{k=1}^{10} k$", "$\\Sigma_{k=1}^{10} 2k$", "$\\Sigma_{k=1}^{10} (k+1)$", "$\\Sigma_{k=0}^{9} k$"]
      }
    ]
  },
  "unidad2": {
    "nombre_unidad": "Unidad 2 - Funciones Exponenciales",
    "ejercicios": [
      {
        "problema": "Calcule el valor de $f(-2)$ para la función exponencial $f(x) = 2^x$.",
        "respuesta": "1/4",
        "explicacion": "$f(-2) = 2^{-2} = 1/2^2 = 1/4$.",
        "opciones": ["1/2", "1/4", "-4", "4"]
      },
      {
        "problema": "Calcule el valor de $f(2)$ para la función exponencial $f(x) = (1/2)^x$.",
        "respuesta": "1/4",
        "explicacion": "$f(2) = (1/2)^2 = 1/4$.",
        "opciones": ["4", "2", "1/2", "1/4"]
      },
      {
        "problema": "Resuelva para $x$: Si $2^x = 32$, halle $x$.",
        "respuesta": "$x = 5$",
        "explicacion": "$2^x = 32$. Como $32 = 2^5$, entonces $x=5$.",
        "opciones": ["$x = 4$", "$x = 5$", "$x = 6$", "$x = 3$"]
      },
      {
        "problema": "Resuelva para $x$: Si $(1/2)^x = 1/16$, halle $x$.",
        "respuesta": "$x = 4$",
        "explicacion": "$(1/2)^x = 1/16$. Como $1/16 = (1/2)^4$, entonces $x=4$.",
        "opciones": ["$x = 2$", "$x = -4$", "$x = 4$", "$x = 8$"]
      },
      {
        "problema": "Determine la asíntota horizontal de la función $f(x) = 3^x - 1$.",
        "respuesta": "$y = -1$",
        "explicacion": "La función básica $3^x$ tiene una asíntota en $y=0$. Al restarle 1, la asíntota se desplaza a $y=-1$.",
        "opciones": ["$y = 0$", "$y = 3$", "$x = 0$", "$y = -1$"]
      },
      {
        "problema": "Indique si la función $f(x) = (1/3)^x$ es creciente o decreciente.",
        "respuesta": "Decreciente",
        "explicacion": "Una función exponencial $f(x) = a^x$ es decreciente si $0 < a < 1$. En este caso, $a=1/3$.",
        "opciones": ["Creciente", "Decreciente", "Constante", "No se puede determinar"]
      },
      {
        "problema": "Resuelva la ecuación exponencial $4^x = 1/64$.",
        "respuesta": "$x = -3$",
        "explicacion": "$4^x = 1/4^3 = 4^{-3}$, por lo tanto $x=-3$.",
        "opciones": ["$x = 3$", "$x = -3$", "$x = 1/3$", "$x = 4$"]
      },
      {
        "problema": "El crecimiento de una población de bacterias se modela con $P(t) = 100 \\cdot 2^t$, donde $t$ es en horas. ¿Cuántas bacterias habrá después de 3 horas?",
        "respuesta": "800",
        "explicacion": "$P(3) = 100 \\cdot 2^3 = 100 \\cdot 8 = 800$.",
        "opciones": ["200", "400", "800", "1600"]
      },
      {
        "problema": "El valor de un auto se deprecia según $V(t) = 20000 \\cdot (0.9)^t$. ¿Cuál es la tasa de depreciación anual?",
        "respuesta": "10%",
        "explicacion": "La base es $b = 1+r$. Si $b=0.9$, entonces $0.9 = 1 + r$, lo que implica $r = -0.1$ o una depreciación del 10%.",
        "opciones": ["20%", "90%", "1%", "10%"]
      },
      {
        "problema": "Si $f(x) = e^x$, calcule $f(0)$.",
        "respuesta": "1",
        "explicacion": "Cualquier número elevado a la potencia cero es 1. $e^0 = 1$.",
        "opciones": ["0", "e", "1", "$1/e$"]
      },
      {
        "problema": "Resuelva para $x$: $3^{x+1} = 27$.",
        "respuesta": "$x = 2$",
        "explicacion": "$3^{x+1} = 3^3 \\Rightarrow x+1 = 3 \\Rightarrow x = 2$.",
        "opciones": ["$x = 1$", "$x = 2$", "$x = 3$", "$x = -1$"]
      },
      {
        "problema": "Determine el dominio de la función exponencial $f(x) = 5^x$.",
        "respuesta": "Todos los números reales ($\\mathbb{R}$)",
        "explicacion": "El dominio de cualquier función exponencial de la forma $a^x$ es el conjunto de todos los números reales.",
        "opciones": ["$x \\geq 0$", "$x > 0$", "$x \\neq 0$", "Todos los números reales ($\\mathbb{R}$)"]
      },
      {
        "problema": "¿Cuál es la gráfica de la función $f(x) = 4^x$?",
        "respuesta": "Una curva creciente que pasa por (0,1) con asíntota $y=0$.",
        "explicacion": "Toda función $a^x$ con $a>1$ es creciente, pasa por el punto $(0,1)$ y tiene una asíntota horizontal en $y=0$.",
        "opciones": ["Una curva decreciente que pasa por (1,0).", "Una línea recta.", "Una curva creciente que pasa por (0,1) con asíntota $y=0$.", "Una parábola."]
      },
      {
        "problema": "Resuelva para $x$: $5^{2x} = 25^{x+1}$.",
        "respuesta": "Sin solución (identidad que implica $2=2$)",
        "explicacion": "$5^{2x} = (5^2)^{x+1} \\Rightarrow 5^{2x} = 5^{2x+2} \\Rightarrow 2x = 2x+2 \\Rightarrow 0 = 2$. No hay solución real (es una inconsistencia).",
        "opciones": ["$x = 0$", "$x = 1$", "Sin solución (identidad que implica $0=2$)", "$x = -1$"]
      },
      {
        "problema": "Resuelva para $x$: $4^{3x-1} = 1/16$.",
        "respuesta": "$x = -1/3$",
        "explicacion": "$4^{3x-1} = 4^{-2} \\Rightarrow 3x-1 = -2 \\Rightarrow 3x = -1 \\Rightarrow x = -1/3$.",
        "opciones": ["$x = -1$", "$x = 1/3$", "$x = -1/3$", "$x = 0$"]
      }
    ]
  },
  "unidad3": {
    "nombre_unidad": "Unidad 3 - Logaritmos y funciones logarítmicas",
    "ejercicios": [
      {
        "problema": "Calcule $\\log_2(8)$.",
        "respuesta": "3",
        "explicacion": "El logaritmo responde a la pregunta: ¿A qué exponente se debe elevar 2 para obtener 8? ($2^3 = 8$).",
        "opciones": ["2", "3", "4", "8"]
      },
      {
        "problema": "Calcule $\\log_3(1/9)$.",
        "respuesta": "-2",
        "explicacion": "$3^{-2} = 1/3^2 = 1/9$.",
        "opciones": ["2", "-3", "-2", "3"]
      },
      {
        "problema": "Exprese en forma exponencial: $\\log_3(81)=4$.",
        "respuesta": "$3^4 = 81$",
        "explicacion": "La forma general es $\\log_b(a)=c$ equivalente a $b^c=a$.",
        "opciones": ["$4^3 = 81$", "$3^4 = 81$", "$81^4 = 3$", "$3^{81} = 4$"]
      },
      {
        "problema": "Exprese en forma logarítmica: $2^3=8$.",
        "respuesta": "$\\log_2(8) = 3$",
        "explicacion": "La base 2 se mantiene como base del logaritmo.",
        "opciones": ["$\\log_3(8) = 2$", "$\\log_8(2) = 3$", "$\\log_2(8) = 3$", "$\\log_3(2) = 8$"]
      },
      {
        "problema": "Simplifique $\\log(81) - \\log(9)$ usando las propiedades de los logaritmos.",
        "respuesta": "$\\log(9)$",
        "explicacion": "$\\log(a) - \\log(b) = \\log(a/b)$. $\\log(81/9) = \\log(9)$.",
        "opciones": ["$\\log(72)$", "$\\log(9)$", "$\\log(729)$", "$\\log(1/9)$"]
      },
      {
        "problema": "Resuelva: $\\log_2(x)=5$.",
        "respuesta": "$x = 32$",
        "explicacion": "$\\log_2(x)=5$ es equivalente a $2^5 = x$. Por lo tanto, $x = 32$.",
        "opciones": ["$x = 10$", "$x = 32$", "$x = 25$", "$x = 1/32$"]
      },
      {
        "problema": "Calcule $\\log_5(5)$.",
        "respuesta": "1",
        "explicacion": "El logaritmo de la base siempre es 1 ($\\log_b(b)=1$).",
        "opciones": ["0", "5", "1", "25"]
      },
      {
        "problema": "Calcule $\\ln(e^4)$.",
        "respuesta": "4",
        "explicacion": "El logaritmo natural ($\\ln$) es $\\log_e$. $\\ln(e^4) = 4$.",
        "opciones": ["$e$", "1", "4", "$1/4$"]
      },
      {
        "problema": "Simplifique $2 \\log_b(x) + \\log_b(y)$.",
        "respuesta": "$\\log_b(x^2 y)$",
        "explicacion": "Se usa la propiedad de potencia y la de la suma: $\\log_b(x^2) + \\log_b(y) = \\log_b(x^2 y)$.",
        "opciones": ["$\\log_b(2x+y)$", "$\\log_b(x^2 y)$", "$\\log_b(xy^2)$", "$2 \\log_b(x+y)$"]
      },
      {
        "problema": "Resuelva para $x$: $\\log_x(49)=2$.",
        "respuesta": "$x = 7$",
        "explicacion": "En forma exponencial: $x^2 = 49$. La base del logaritmo debe ser positiva, por lo tanto $x=7$.",
        "opciones": ["$x = 49$", "$x = 7$", "$x = 2$", "$x = 1/7$"]
      },
      {
        "problema": "Determine la asíntota vertical de la función logarítmica $f(x) = \\log(x-3)$.",
        "respuesta": "$x = 3$",
        "explicacion": "El argumento del logaritmo debe ser positivo. $x-3 > 0 \\Rightarrow x > 3$. La asíntota es $x=3$.",
        "opciones": ["$y = 0$", "$x = 0$", "$x = 3$", "$y = -3$"]
      },
      {
        "problema": "Desarrolle la expresión $\\log_5(a^3/b)$.",
        "respuesta": "$3 \\log_5(a) - \\log_5(b)$",
        "explicacion": "Se usan las propiedades del cociente y de la potencia: $\\log_5(a^3) - \\log_5(b) = 3 \\log_5(a) - \\log_5(b)$.",
        "opciones": ["$\\log_5(3a) - \\log_5(b)$", "$3 \\log_5(a) / \\log_5(b)$", "$3 \\log_5(a) - \\log_5(b)$", "$\\log_5(3a) - b$"]
      },
      {
        "problema": "Resuelva para $x$: $\\log_4(x+2) = 1$.",
        "respuesta": "$x = 2$",
        "explicacion": "En forma exponencial: $4^1 = x+2 \\Rightarrow 4 = x+2 \\Rightarrow x = 2$.",
        "opciones": ["$x = 4$", "$x = 6$", "$x = 2$", "$x = -1$"]
      },
      {
        "problema": "Calcule $\\log(1000)$, donde $\\log$ es el logaritmo base 10.",
        "respuesta": "3",
        "explicacion": "$10^3 = 1000$.",
        "opciones": ["100", "2", "3", "10"]
      },
      {
        "problema": "Si $\\log_b(x)=3$ y $\\log_b(y)=2$, halle $\\log_b(x/y)$.",
        "respuesta": "1",
        "explicacion": "$\\log_b(x/y) = \\log_b(x) - \\log_b(y) = 3 - 2 = 1$.",
        "opciones": ["5", "6", "1", "$3/2$"]
      }
    ]
  },
  "unidad4": {
    "nombre_unidad": "Unidad 4 - Geometría Analítica",
    "ejercicios": [
      {
        "problema": "Determine la distancia entre los puntos $A(1,2)$ y $B(4,6)$.",
        "respuesta": "5",
        "explicacion": "$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{3^2 + 4^2} = \\sqrt{9+16} = 5$.",
        "opciones": ["$\\sqrt{13}$", "5", "7", "$\\sqrt{5}$"]
      },
      {
        "problema": "Halle el punto medio del segmento que une $C(-4,1)$ y $D(2,7)$.",
        "respuesta": "$(-1, 4)$",
        "explicacion": "$M = ((-4+2)/2, (1+7)/2) = (-2/2, 8/2) = (-1, 4)$.",
        "opciones": ["$(1, 4)$", "$(-1, 4)$", "$(-2, 3)$", "$(2, 3)$"]
      },
      {
        "problema": "Encuentre la pendiente de la recta que pasa por $(1,2)$ y $(4,6)$.",
        "respuesta": "$4/3$",
        "explicacion": "$m = (y_2 - y_1) / (x_2 - x_1) = (6 - 2) / (4 - 1) = 4/3$.",
        "opciones": ["$1/3$", "$3/4$", "$4/3$", "2"]
      },
      {
        "problema": "Determine la ecuación de la recta que pasa por $(1,-1)$ y $(3,5)$.",
        "respuesta": "$y = 3x - 4$",
        "explicacion": "$m = (5 - (-1)) / (3 - 1) = 6/2 = 3$. $y - 5 = 3(x - 3) \\Rightarrow y = 3x - 9 + 5 \\Rightarrow y = 3x - 4$.",
        "opciones": ["$y = 3x + 4$", "$y = 3x - 4$", "$y = -3x + 2$", "$y = x + 2$"]
      },
      {
        "problema": "Determine la ecuación de la circunferencia con centro en $(0,0)$ y radio 5.",
        "respuesta": "$x^2 + y^2 = 25$",
        "explicacion": "La ecuación es $(x-h)^2 + (y-k)^2 = r^2$. Con $h=0, k=0, r=5$.",
        "opciones": ["$x^2 + y^2 = 5$", "$x^2 + y^2 = 25$", "$(x-5)^2 + (y-5)^2 = 0$", "$(x-0)^2 + (y-0)^2 = 5$"]
      },
      {
        "problema": "Halle la ecuación de la circunferencia con centro en $(2,3)$ y radio 4.",
        "respuesta": "$(x-2)^2 + (y-3)^2 = 16$",
        "explicacion": "La ecuación es $(x-h)^2 + (y-k)^2 = r^2$. $(x-2)^2 + (y-3)^2 = 4^2 = 16$.",
        "opciones": ["$(x+2)^2 + (y+3)^2 = 16$", "$(x-2)^2 + (y-3)^2 = 4$", "$(x-2)^2 + (y-3)^2 = 16$", "$x^2 + y^2 = 16$"]
      },
      {
        "problema": "Halle la pendiente de una recta perpendicular a $y = 2x + 1$.",
        "respuesta": "$m = -1/2$",
        "explicacion": "La pendiente de la recta dada es $m_1=2$. La pendiente perpendicular es $m_2 = -1/m_1 = -1/2$.",
        "opciones": ["$m = 2$", "$m = -2$", "$m = 1/2$", "$m = -1/2$"]
      },
      {
        "problema": "¿Cuál es la forma general de la ecuación de la recta $y = -3x + 5$?",
        "respuesta": "$3x + y - 5 = 0$",
        "explicacion": "La forma general es $Ax + By + C = 0$. $3x + y - 5 = 0$.",
        "opciones": ["$x + 3y + 5 = 0$", "$3x + y - 5 = 0$", "$y + 3x = 5$", "$3x - y + 5 = 0$"]
      },
      {
        "problema": "Encuentre el centro de la circunferencia con ecuación $x^2 + y^2 - 6x + 4y - 12 = 0$.",
        "respuesta": "$C(3, -2)$",
        "explicacion": "Centro $C(-D/2, -E/2)$. $D=-6, E=4$. $C(-(-6)/2, -4/2) = (3, -2)$.",
        "opciones": ["$C(-6, 4)$", "$C(6, -4)$", "$C(3, -2)$", "$C(-3, 2)$"]
      },
      {
        "problema": "Calcule el radio de la circunferencia $x^2 + y^2 = 49$.",
        "respuesta": "$r = 7$",
        "explicacion": "La forma es $x^2 + y^2 = r^2$. $r^2 = 49$, por lo tanto $r=7$.",
        "opciones": ["$r = 49$", "$r = 7$", "$r = 14$", "$r = 24.5$"]
      },
      {
        "problema": "Determine si las rectas $L_1: y = 3x+2$ y $L_2: y = 3x-5$ son paralelas, perpendiculares o secantes.",
        "respuesta": "Paralelas",
        "explicacion": "Ambas rectas tienen la misma pendiente $m=3$, por lo que son paralelas.",
        "opciones": ["Perpendiculares", "Secantes", "Paralelas", "Coincidentes"]
      },
      {
        "problema": "Encuentre la ecuación de la recta que pasa por $(0, -5)$ y tiene pendiente $m = 2$.",
        "respuesta": "$y = 2x - 5$",
        "explicacion": "Se utiliza la forma pendiente-intersección $y = mx + b$. El intercepto $b = -5$. $y = 2x - 5$.",
        "opciones": ["$y = -5x + 2$", "$y = 2x - 5$", "$y = 2(x-5)$", "$x = 2y - 5$"]
      },
      {
        "problema": "Calcule la distancia del origen $(0,0)$ a la recta $3x - 4y + 10 = 0$.",
        "respuesta": "2",
        "explicacion": "Distancia: $|3(0) - 4(0) + 10| / \\sqrt{3^2 + (-4)^2} = 10 / \\sqrt{25} = 10/5 = 2$.",
        "opciones": ["$10$", "$5$", "$2$", "$0$"]
      },
      {
        "problema": "Dado el vector $\\vec{v} = \\langle 3, 4 \\rangle$, calcule su magnitud (o módulo).",
        "respuesta": "$|\\vec{v}| = 5$",
        "explicacion": "La magnitud es $|\\vec{v}| = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = 5$.",
        "opciones": ["$|\\vec{v}| = 7$", "$|\\vec{v}| = 5$", "$|\\vec{v}| = 3.5$", "$|\\vec{v}| = \\sqrt{7}$"]
      },
      {
        "problema": "Encuentre el radio de la circunferencia con centro en $(1, -2)$ y que pasa por el punto $(4, 2)$.",
        "respuesta": "$r = 5$",
        "explicacion": "El radio es la distancia entre los dos puntos: $r = \\sqrt{(4-1)^2 + (2-(-2))^2} = \\sqrt{3^2 + 4^2} = 5$.",
        "opciones": ["$r = 9$", "$r = 5$", "$r = 25$", "$r = \\sqrt{21}$"]
      }
    ]
  },
  "unidad5": {
    "nombre_unidad": "Unidad 5 - Cónicas",
    "ejercicios": [
      {
        "problema": "Determine la ecuación de la parábola con vértice en el origen y foco en $(0,2)$.",
        "respuesta": "$x^2 = 8y$",
        "explicacion": "Es una parábola vertical con vértice $(0,0)$ y $p=2$. La forma es $x^2 = 4py$. $x^2 = 4(2)y = 8y$.",
        "opciones": ["$y^2 = 8x$", "$x^2 = 8y$", "$x^2 = 4y$", "$y^2 = -8x$"]
      },
      {
        "problema": "Halle la ecuación de la parábola con vértice en $(0,0)$ y directriz $y=-3$.",
        "respuesta": "$x^2 = 12y$",
        "explicacion": "La directriz $y=-p$ implica $p=3$. La forma es $x^2 = 4py = 4(3)y = 12y$.",
        "opciones": ["$y^2 = 12x$", "$x^2 = 12y$", "$x^2 = -12y$", "$y^2 = -12x$"]
      },
      {
        "problema": "Halle la ecuación de la elipse con centro en el origen, $a=5$, $b=3$ (eje mayor en $x$).",
        "respuesta": "$x^2/25 + y^2/9 = 1$",
        "explicacion": "$a^2=25$, $b^2=9$. La forma horizontal es $x^2/a^2 + y^2/b^2 = 1$.",
        "opciones": ["$x^2/9 + y^2/25 = 1$", "$x^2/25 + y^2/9 = 1$", "$x^2 + y^2 = 25$", "$9x^2 + 25y^2 = 225$"]
      },
      {
        "problema": "Dada la elipse $x^2/25 + y^2/16 = 1$, encuentre su centro y vértices principales.",
        "respuesta": "Centro $(0,0)$, Vértices $(\\pm 5,0)$",
        "explicacion": "$a^2=25 \\Rightarrow a=5$. El centro es $(0,0)$ y los vértices en el eje x son $(\\pm a, 0)$.",
        "opciones": ["Centro $(0,0)$, Vértices $(\\pm 5,0)$", "Centro $(0,0)$, Vértices $(0,\\pm 4)$", "Centro $(0,0)$, Vértices $(\\pm 3,0)$", "Centro $(0,0)$, Vértices $(\\pm 4,0)$"]
      },
      {
        "problema": "Halle la ecuación de la hipérbola con centro en el origen, vértices $(\\pm 3,0)$ y asíntotas $y=\\pm x$.",
        "respuesta": "$x^2/9 - y^2/9 = 1$",
        "explicacion": "Vértices en $x$ implican $a=3$ ($a^2=9$). Asíntotas $y=\\pm (b/a)x$ implican $b/3=1 \\Rightarrow b=3$ ($b^2=9$).",
        "opciones": ["$x^2/3 - y^2/3 = 1$", "$x^2/9 - y^2/9 = 1$", "$y^2/9 - x^2/9 = 1$", "$x^2/9 + y^2/9 = 1$"]
      },
      {
        "problema": "En la parábola $y^2 = -20x$, ¿cuáles son las coordenadas del foco?",
        "respuesta": "$F(-5, 0)$",
        "explicacion": "Es una parábola horizontal de la forma $y^2 = 4px$. $4p = -20 \\Rightarrow p = -5$. El foco es $(p, 0)$.",
        "opciones": ["$F(5, 0)$", "$F(-5, 0)$", "$F(0, 5)$", "$F(0, -5)$"]
      },
      {
        "problema": "Para la elipse $x^2/100 + y^2/64 = 1$, calcule la distancia focal ($2c$).",
        "respuesta": "12",
        "explicacion": "$a^2=100, b^2=64$. $c^2 = a^2 - b^2 = 100 - 64 = 36 \\Rightarrow c = 6$. La distancia focal es $2c=12$.",
        "opciones": ["$6$", "$36$", "12", "16"]
      },
      {
        "problema": "Determine el centro de la hipérbola dada por la ecuación $(x-1)^2/4 - (y+2)^2/9 = 1$.",
        "respuesta": "$C(1, -2)$",
        "explicacion": "El centro es $(h, k)$. Aquí $h=1$ y $k=-2$.",
        "opciones": ["$C(4, 9)$", "$C(-1, 2)$", "$C(1, -2)$", "$C(-4, -9)$"]
      },
      {
        "problema": "Una cónica tiene un foco en $(0, 4)$ y la directriz $y = -4$. ¿Qué cónica es?",
        "respuesta": "Parábola",
        "explicacion": "Es una parábola, ya que se define como el lugar geométrico de los puntos que equidistan de un foco y una directriz.",
        "opciones": ["Elipse", "Hipérbola", "Circunferencia", "Parábola"]
      },
      {
        "problema": "Determine la excentricidad ($e$) de una elipse si su semieje mayor ($a$) es 5 y la distancia focal ($c$) es 3.",
        "respuesta": "$e = 3/5$",
        "explicacion": "La excentricidad es $e = c/a$. $e = 3/5$.",
        "opciones": ["$e = 5/3$", "$e = 4/5$", "$e = 3/5$", "$e = 1$"]
      },
      {
        "problema": "La ecuación $4x^2 - 9y^2 = 36$ representa una:",
        "respuesta": "Hipérbola",
        "explicacion": "Al dividir por 36, se obtiene $x^2/9 - y^2/4 = 1$. La resta de términos cuadráticos indica una hipérbola.",
        "opciones": ["Elipse", "Parábola", "Circunferencia", "Hipérbola"]
      },
      {
        "problema": "¿Cuál es la ecuación de la directriz de la parábola $y^2 = 16x$?",
        "respuesta": "$x = -4$",
        "explicacion": "$4p = 16 \\Rightarrow p = 4$. La directriz de una parábola horizontal es $x = -p$.",
        "opciones": ["$x = 4$", "$y = 4$", "$x = -4$", "$y = -4$"]
      },
      {
        "problema": "Una elipse tiene $a=10$ y $b=6$. ¿Cuál es la longitud del eje menor?",
        "respuesta": "12",
        "explicacion": "El semieje menor es $b=6$. La longitud del eje menor es $2b = 2(6) = 12$.",
        "opciones": ["$10$", "$20$", "$12$", "$6$"]
      },
      {
        "problema": "Determine la ecuación de la hipérbola con centro en $(0,0)$, $a=4$ y $b=3$ (eje transverso en $y$).",
        "respuesta": "$y^2/16 - x^2/9 = 1$",
        "explicacion": "El eje transverso en $y$ significa que el término $y^2$ es positivo. $y^2/a^2 - x^2/b^2 = 1$.",
        "opciones": ["$x^2/16 - y^2/9 = 1$", "$y^2/16 - x^2/9 = 1$", "$x^2/9 - y^2/16 = 1$", "$y^2/9 - x^2/16 = 1$"]
      },
      {
        "problema": "Determine el foco de la parábola $(y-1)^2 = 8(x-3)$.",
        "respuesta": "$F(5, 1)$",
        "explicacion": "Vértice $V(3, 1)$. $4p=8 \\Rightarrow p=2$. La parábola abre hacia la derecha. Foco $(h+p, k) = (3+2, 1) = (5, 1)$.",
        "opciones": ["$F(3, 3)$", "$F(5, 1)$", "$F(3, -1)$", "$F(1, 1)$"]
      }
    ]
  },
  "unidad6": {
    "nombre_unidad": "Unidad 6 - Técnicas de Conteo y Probabilidades",
    "ejercicios": [
      {
        "problema": "¿De cuántas maneras se pueden ordenar las letras de la palabra “MAMA”?",
        "respuesta": "6",
        "explicacion": "Permutación con repetición: $4! / (2!2!) = 24 / 4 = 6$.",
        "opciones": ["4", "12", "6", "24"]
      },
      {
        "problema": "¿Cuántos números de tres cifras distintas se pueden formar con los dígitos 1, 2, 3, 4, 5?",
        "respuesta": "60",
        "explicacion": "Permutación sin repetición: $P(5, 3) = 5! / (5-3)! = 5 \\cdot 4 \\cdot 3 = 60$.",
        "opciones": ["120", "60", "20", "15"]
      },
      {
        "problema": "¿De cuántas maneras se pueden escoger 3 estudiantes de un grupo de 10?",
        "respuesta": "120",
        "explicacion": "Combinación: $C(10, 3) = 10! / (3!7!) = 10 \\cdot 9 \\cdot 8 / (3 \\cdot 2 \\cdot 1) = 120$.",
        "opciones": ["720", "30", "10", "120"]
      },
      {
        "problema": "En una bolsa hay 6 bolas blancas y 4 negras. ¿Cuál es la probabilidad de que al extraer una sea blanca?",
        "respuesta": "$6/10 = 3/5$",
        "explicacion": "Casos favorables/Totales: $6 / (6+4) = 6/10$.",
        "opciones": ["4/10", "6/10 = 3/5", "1/2", "3/10"]
      },
      {
        "problema": "Se lanzan tres monedas. Probabilidad de obtener exactamente dos caras (escudos) y una cruz (número).",
        "respuesta": "$3/8$",
        "explicacion": "Casos totales: 8. Casos favorables (CCE, CEC, ECC): 3. $P=3/8$.",
        "opciones": ["$3/8$", "1/2", "1/4", "1/8"]
      },
      {
        "problema": "En el lanzamiento de dos dados, probabilidad de obtener suma 7.",
        "respuesta": "$6/36 = 1/6$",
        "explicacion": "Hay 6 combinaciones que suman 7 (1+6, 2+5, 3+4, 4+3, 5+2, 6+1) entre 36 totales.",
        "opciones": ["1/6", "1/4", "1/3", "1/12"]
      },
      {
        "problema": "¿De cuántas maneras se pueden sentar 5 personas en una fila?",
        "respuesta": "120",
        "explicacion": "Es una permutación de 5 elementos: $P(5) = 5! = 5 \\cdot 4 \\cdot 3 \\cdot 2 \\cdot 1 = 120$.",
        "opciones": ["25", "20", "120", "5"]
      },
      {
        "problema": "Se extrae una carta al azar de una baraja española (40 cartas). ¿Cuál es la probabilidad de que sea un as?",
        "respuesta": "$4/40 = 1/10$",
        "explicacion": "Hay 4 ases en 40 cartas. $P = 4/40 = 1/10$.",
        "opciones": ["$1/40$", "$4/40 = 1/10$", "$1/4$", "$10/40$"]
      },
      {
        "problema": "Se lanzan 4 monedas. ¿Cuántos resultados posibles hay?",
        "respuesta": "16",
        "explicacion": "Por el principio de multiplicación: $2 \\cdot 2 \\cdot 2 \\cdot 2 = 2^4 = 16$.",
        "opciones": ["8", "16", "4", "32"]
      },
      {
        "problema": "En una carrera con 8 corredores, ¿de cuántas formas se pueden asignar los tres primeros puestos?",
        "respuesta": "336",
        "explicacion": "Permutación: $P(8, 3) = 8 \\cdot 7 \\cdot 6 = 336$.",
        "opciones": ["24", "40320", "56", "336"]
      },
      {
        "problema": "¿Cuántos comités de 2 hombres y 3 mujeres se pueden formar con 5 hombres y 6 mujeres?",
        "respuesta": "200",
        "explicacion": "Combinación: $C(5, 2) \\cdot C(6, 3) = 10 \\cdot 20 = 200$.",
        "opciones": ["30", "150", "200", "720"]
      },
      {
        "problema": "Al lanzar un dado, ¿cuál es la probabilidad de obtener un número par o un número mayor que 4?",
        "respuesta": "$4/6 = 2/3$",
        "explicacion": "Números pares: {2, 4, 6}. Números mayores que 4: {5, 6}. Unión: {2, 4, 5, 6}. $P=4/6$.",
        "opciones": ["$1/2$", "$1/3$", "$4/6 = 2/3$", "$5/6$"]
      },
      {
        "problema": "Una clave tiene 3 letras distintas seguidas de 2 dígitos distintos (del 0 al 9). ¿Cuántas claves son posibles?",
        "respuesta": "1,404,000",
        "explicacion": "Letras: $P(26, 3) = 26 \\cdot 25 \\cdot 24 = 15600$. Dígitos: $P(10, 2) = 10 \\cdot 9 = 90$. Total: $15600 \\cdot 90 = 1,404,000$.",
        "opciones": ["$1,757,600$", "$1,404,000$", "$156,000$", "$676,000$"]
      },
      {
        "problema": "Probabilidad de sacar un rey y luego una reina (sin reemplazo) de una baraja de 52 cartas.",
        "respuesta": "$4/663$",
        "explicacion": "$P(Rey) = 4/52$. $P(Reina|Rey) = 4/51$. $P = (4/52) \\cdot (4/51) = 16/2652 = 4/663$.",
        "opciones": ["$1/169$", "$1/13 \\cdot 1/13$", "$4/663$", "$1/200$"]
      },
      {
        "problema": "¿Cuántos resultados distintos hay al tirar dos dados de 6 caras?",
        "respuesta": "36",
        "explicacion": "Principio de multiplicación: $6 \\cdot 6 = 36$.",
        "opciones": ["12", "6", "36", "18"]
      }
    ]
  }
}

import simplejson as json
from django.shortcuts import render
# Otras importaciones de Django...

# Tu diccionario de fórmulas CORRECTO (sin $ en 'formula' y con doble \\):

FORMULAS = {
    "Unidad 1: Sucesiones": [
        {
            "id": 101,
            "nombre": "Término general (Aritmética)",
            "formula": "$a_n = a_1 + (n-1)d$",
            "descripcion": "Calcula el enésimo término de una sucesión aritmética, donde '$d$' es la diferencia común y '$a_1$' el primer término.",
            "ejemplo": "Dada la sucesión (5, 8, 11, ...), con $a_1=5$ y $d=3$. El término general es $a_n = 5 + (n-1)3$."
        },
        {
            "id": 102,
            "nombre": "Suma de n términos (Aritmética)",
            "formula": "$S_n = \\frac{n(a_1 + a_n)}{2}$",
            "descripcion": "Calcula la suma de los primeros '$n$' términos de una sucesión aritmética.",
            "ejemplo": "La suma de los primeros 10 términos de la sucesión donde $a_1=2$ y $a_{10}=20$ es $S_{10} = \\frac{10(2 + 20)}{2} = 110$."
        },
        {
            "id": 103,
            "nombre": "Término general (Geométrica)",
            "formula": "$a_n = a_1 \\cdot r^{n-1}$",
            "descripcion": "Calcula el enésimo término de una sucesión geométrica, donde '$r$' es la razón común y '$a_1$' el primer término.",
            "ejemplo": "Dada la sucesión (3, 6, 12, ...), con $a_1=3$ y $r=2$. El término general es $a_n = 3 \\cdot 2^{n-1}$."
        },
        {
            "id": 104,
            "nombre": "Suma de n términos (Geométrica, r != 1)",
            "formula": "$S_n = \\frac{a_1 (r^n - 1)}{r - 1}$",
            "descripcion": "Calcula la suma de los primeros '$n$' términos de una sucesión geométrica.",
            "ejemplo": "La suma de los primeros 4 términos de la sucesión donde $a_1=2$ y $r=3$ es $S_4 = \\frac{2(3^4 - 1)}{3 - 1} = 80$."
        },
        {
            "id": 105,
            "nombre": "Notación de Sumatoria (Sigma)",
            "formula": "$S = \\sum_{k=1}^{n} a_k$",
            "descripcion": "Representa la suma de los términos desde el índice $k=1$ hasta $n$.",
            "ejemplo": "La expresión $\\sum_{k=1}^{4} 2k$ representa la suma $2(1) + 2(2) + 2(3) + 2(4) = 20$."
        }
    ],
    "Unidad 2: Potenciación y Funciones Exponenciales": [
        {
            "id": 201,
            "nombre": "Multiplicación de bases iguales",
            "formula": "$a^m \\cdot a^n = a^{m+n}$",
            "descripcion": "Al multiplicar potencias con la misma base, se suman los exponentes.",
            "ejemplo": "$2^3 \\cdot 2^4 = 2^{3+4} = 2^7 = 128$."
        },
        {
            "id": 202,
            "nombre": "Potencia de una potencia",
            "formula": "$(a^m)^n = a^{m \\cdot n}$",
            "descripcion": "Al elevar una potencia a otro exponente, se multiplican los exponentes.",
            "ejemplo": "$(5^2 )^3 = 5^{2 \\cdot 3} = 5^6 = 15625$."
        },
        {
            "id": 203,
            "nombre": "División de bases iguales",
            "formula": "$\\frac{a^m}{a^n} = a^{m-n}$",
            "descripcion": "Al dividir potencias con la misma base, se restan los exponentes.",
            "ejemplo": "$\\frac{x^7}{x^3} = x^4$."
        },
        {
            "id": 204,
            "nombre": "Exponente negativo",
            "formula": "$a^{-n} = \\frac{1}{a^n}$",
            "descripcion": "Convierte un exponente negativo en un exponente positivo en el denominador de una fracción.",
            "ejemplo": "$4^{-2} = \\frac{1}{4^2} = \\frac{1}{16}$."
        },
        {
            "id": 205,
            "nombre": "Multiplicación de radicales",
            "formula": "$\\sqrt[n]{a} \\cdot \\sqrt[n]{b} = \\sqrt[n]{a \\cdot b}$",
            "descripcion": "El producto de radicales con el mismo índice es igual a la raíz del producto.",
            "ejemplo": "$\\sqrt[3]{4} \\cdot \\sqrt[3]{2} = \\sqrt[3]{8} = 2$."
        },
        {
            "id": 206,
            "nombre": "Propiedad de ecuaciones exponenciales",
            "formula": "$Si\\ a^p = a^q, entonces\\ p = q$",
            "descripcion": "Si las bases son iguales (y $a \\neq 0, 1, -1$), los exponentes deben ser iguales.",
            "ejemplo": "Si $2^x = 2^5$, entonces $x = 5$."
        }
    ],
    "Unidad 3: Logaritmo y Funciones Logarítmicas": [
        {
            "id": 301,
            "nombre": "Definición de logaritmo",
            "formula": "$\\log_a M = x \\iff M = a^x$",
            "descripcion": "Establece la relación entre la forma logarítmica y la forma exponencial.",
            "ejemplo": "$\\log_2 8 = 3 \\iff 8 = 2^3$."
        },
        {
            "id": 302,
            "nombre": "Logaritmo de un producto",
            "formula": "$\\log_a (M \\cdot N) = \\log_a M + \\log_a N$",
            "descripcion": "El logaritmo de un producto es la suma de los logaritmos.",
            "ejemplo": "$\\log_{10} (5 \\cdot 2) = \\log_{10} 5 + \\log_{10} 2$."
        },
        {
            "id": 303,
            "nombre": "Logaritmo de una potencia",
            "formula": "$\\log_a M^k = k \\cdot \\log_a M$",
            "descripcion": "El logaritmo de una potencia es el exponente por el logaritmo de la base.",
            "ejemplo": "$\\log_2 16 = \\log_2 2^4 = 4 \\cdot \\log_2 2 = 4(1) = 4$."
        },
        {
            "id": 304,
            "nombre": "Fórmula de Cambio de Base",
            "formula": "$\\log_a M = \\frac{\\log_b M}{\\log_b a}$",
            "descripcion": "Permite calcular un logaritmo en base '$a$' usando una nueva base '$b$'.",
            "ejemplo": "$\\log_3 10 = \\frac{\\log_{10} 10}{\\log_{10} 3} \\approx \\frac{1}{0.4771}$."
        }
    ],
    "Unidad 4: Geometría Analítica": [
        {
            "id": 401,
            "nombre": "Coordenada x de punto que divide en razón m:n",
            "formula": "$x = \\frac{n x_1 + m x_2}{m + n}$",
            "descripcion": "Calcula la coordenada $x$ del punto que divide un segmento con extremos $(x_1, y_1)$ y $(x_2, y_2)$ en una razón dada ($m:n$).",
            "ejemplo": "Para $A(1, 0)$ y $B(5, 0)$ en razón $1:1$, la coordenada $x$ es $x = \\frac{1(1) + 1(5)}{1 + 1} = 3$."
        },
        {
            "id": 402,
            "nombre": "Circunferencia (Ordinaria, centro (h, k))",
            "formula": "$(x-h)^2 + (y-k)^2 = r^2$",
            "descripcion": "Ecuación de una circunferencia con centro en $(h, k)$ y radio '$r$'.",
            "ejemplo": "Una circunferencia con centro en $(3, -2)$ y radio $4$ tiene la ecuación $(x-3)^2 + (y+2)^2 = 16$."
        }
    ],
    "Unidad 5: Cónicas": [
        {
            "id": 501,
            "nombre": "Parábola (Vértice en (0, 0), foco eje y)",
            "formula": "$x^2 = 4py$",
            "descripcion": "Ecuación de una parábola vertical con vértice en el origen, donde '$p$' es la distancia del foco al vértice.",
            "ejemplo": "Una parábola con foco en $(0, 3)$ tiene $p=3$, y su ecuación es $x^2 = 4(3)y$, o sea, $x^2 = 12y$."
        },
        {
            "id": 502,
            "nombre": "Elipse (Canónica, centro (0, 0), focos eje x)",
            "formula": "$\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$",
            "descripcion": "Ecuación de una elipse horizontal con centro en el origen, donde '$a$' es el semieje mayor y '$b$' el semieje menor.",
            "ejemplo": "Si $a=5$ y $b=3$, la ecuación es $\\frac{x^2}{25} + \\frac{y^2}{9} = 1$."
        },
        {
            "id": 503,
            "nombre": "Relación fundamental (Elipse)",
            "formula": "$c^2 = a^2 - b^2$",
            "descripcion": "Relaciona la distancia del centro a los vértices ('$a$'), a los extremos del eje menor ('$b$'), y a los focos ('$c$').",
            "ejemplo": "Si $a=5$ y $b=3$, entonces $c^2 = 5^2 - 3^2 = 16$, por lo tanto, $c=4$ (distancia focal)."
        },
        {
            "id": 504,
            "nombre": "Hipérbola (Canónica, centro (0, 0), focos eje x)",
            "formula": "$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$",
            "descripcion": "Ecuación de una hipérbola horizontal con centro en el origen.",
            "ejemplo": "Una hipérbola con $a=4$ y $b=3$ tiene la ecuación $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$."
        },
        {
            "id": 505,
            "nombre": "Asíntotas (Hipérbola, focos eje x)",
            "formula": "$y = \\pm \\frac{b}{a} x$",
            "descripcion": "Ecuación de las líneas asíntotas que guían las ramas de una hipérbola horizontal.",
            "ejemplo": "Para la hipérbola $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$ ($a=4, b=3$), las asíntotas son $y = \\pm \\frac{3}{4}x$."
        }
    ],
    "Unidad 6: Técnicas de Conteo y Probabilidades": [
        {
            "id": 601,
            "nombre": "Probabilidad Teórica",
            "formula": "$P(A) = \\frac{n(A)}{n(E)}$",
            "descripcion": "Calcula la probabilidad de un evento como la razón entre casos favorables '$n(A)$' y casos posibles '$n(E)$'.",
            "ejemplo": "La probabilidad de sacar un 5 en un dado de 6 caras es $P(5) = \\frac{1}{6}$."
        },
        {
            "id": 602,
            "nombre": "Regla de la Adición (Eventos cualesquiera)",
            "formula": "$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$",
            "descripcion": "Calcula la probabilidad de que ocurra el evento $A$ o el evento $B$.",
            "ejemplo": "$P(\\text{par o } 5) = P(\\text{par}) + P(5) - P(\\text{par } \\cap \\text{ } 5) = \\frac{3}{6} + \\frac{1}{6} - \\frac{0}{6} = \\frac{4}{6}$."
        },
        {
            "id": 603,
            "nombre": "Regla de la Adición (Eventos mutuamente excluyentes)",
            "formula": "$P(A \\cup B) = P(A) + P(B)$",
            "descripcion": "Calcula la probabilidad de la unión de dos eventos que no pueden ocurrir simultáneamente.",
            "ejemplo": "$P(\\text{par o impar}) = P(\\text{par}) + P(\\text{impar}) = \\frac{3}{6} + \\frac{3}{6} = 1$."
        },
        {
            "id": 604,
            "nombre": "Probabilidad Condicional (A dado B)",
            "formula": "$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$",
            "descripcion": "Calcula la probabilidad de que ocurra $A$, dado que $B$ ya ha ocurrido.",
            "ejemplo": "$P(\\text{sacar } 6 | \\text{ sacar par}) = \\frac{P(\\text{sacar } 6 \\cap \\text{ par})}{P(\\text{sacar par})} = \\frac{1/6}{3/6} = \\frac{1}{3}$."
        },
        {
            "id": 605,
            "nombre": "Regla de la Multiplicación (Eventos independientes)",
            "formula": "$P(A \\cap B) = P(A) \\cdot P(B)$",
            "descripcion": "Calcula la probabilidad de que los eventos $A$ y $B$ ocurran simultáneamente o en secuencia.",
            "ejemplo": "$P(\\text{cara y } 5) = P(\\text{cara}) \\cdot P(5) = \\frac{1}{2} \\cdot \\frac{1}{6} = \\frac{1}{12}$."
        }
    ]
}

def get_formula_by_id(formula_id):
    """Busca y retorna una fórmula por su ID único."""
    try:
        formula_id = int(formula_id)
    except (TypeError, ValueError):
        return None
    
    for formulas in FORMULAS.values():
        for formula in formulas:
            if formula.get("id") == formula_id:
                return formula
    return None

UNIDADES = list(FORMULAS.keys())


def formulas_view(request):
    selected_unidad = request.GET.get('unidad')
    formula_id = request.GET.get('formula_id')
    
    formula_obj = None
    selected_formula_details_json = None
    
    if formula_id:
        formula_obj = get_formula_by_id(formula_id)

        if formula_obj:
            # *** SERIALIZACIÓN CLAVE PARA DJANGO ***
            # Convertimos el objeto Python a una cadena JSON aquí, en la vista.
            selected_formula_details_json = json.dumps(formula_obj, ensure_ascii=False)
    
    context = {
        'unidades': UNIDADES,
        'selected_unidad': selected_unidad,
        # Pasamos la cadena JSON serializada al contexto
        'selected_formula_details_json': selected_formula_details_json, 
        
        # También pasamos el objeto de Python por si se necesita para obtener el nombre en el template
        'selected_formula_details': formula_obj, 
        
        'formulas': FORMULAS.get(selected_unidad) if selected_unidad else None,
    }

    return render(request, 'nombre_de_tu_template.html', context)
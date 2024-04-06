from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# funcion suma
def suma(num1, num2):
    resultado = num1 + num2
    return "La suma de {} y {} es: {}".format(num1, num2, resultado)

# funcion resta
def resta(num1, num2):
    resultado = num1 - num2
    return "La resta de {} y {} es: {}".format(num1, num2, resultado)

# funcion multiplicacion
def multiplicacion(num1, num2):
    resultado = num1 * num2
    return "La multiplicacion de {} y {} es: {}".format(num1, num2, resultado)

# funcion division
def division(num1, num2):
    resultado = num1 / num2
    return "La division de {} y {} es: {}".format(num1, num2, resultado)

#El que va adespachar el resultado del endpoit
dispatcher = SoapDispatcher(
    "ejercicio-uno-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace = True,
    ns = True,
)

dispatcher.register_function(
    "Suma",
    suma,
    returns={"resultado": str},
    args={"num1": int, "num2": int},
)

dispatcher.register_function(
    "Resta",
    resta,
    returns={"resultado": str},
    args={"num1": int, "num2": int},
)

dispatcher.register_function(
    "Multiplicacion",
    multiplicacion,
    returns={"resultado": str},
    args={"num1": int, "num2": int},
)

dispatcher.register_function(
    "Division",
    division,
    returns={"resultado": str},
    args={"num1": int, "num2": int},
)

def main():
    try:
        server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
        server.dispatcher = dispatcher
        print("Servidor SOAP iniciando en http://localhost:8000/")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        server.server_close()


if __name__ == "__main__":
    main()
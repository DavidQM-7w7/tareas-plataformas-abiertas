from flask import Blueprint, request, jsonify

estudiantes_endpoints = Blueprint(
    'estudiantes_endpoints',
    __name__
)

@estudiantes_endpoints.route('/hola', methods=['GET'])
def hola():

    return jsonify({
        "mensaje": "Bienvenido a la API de estudiantes"
    }), 200


@estudiantes_endpoints.route('/saludo', methods=['GET'])
def saludo():

    nombre = request.args.get('nombre')

    if not nombre:

        return jsonify({
            "mensaje": "Debe de ingresar el nombre del estudiante"
        }), 400

    return jsonify({
        "mensaje": f"Hola {nombre}"
    }), 200
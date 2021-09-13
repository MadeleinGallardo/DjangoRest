# api view
from rest_framework.views import APIView
from rest_framework.views import Response
# para el POST
from rest_framework import status
from rest_framework import serializers


class HelloApiView(APIView):
    '''api view de prueba'''
    # HelloSerializer en la clase q esta en serialier
    # es la manera estandar q se usa para obtener el serializador vasado en clases de api
    serializers_class = serializers.HelloSerializer
    # funcion get

    def get(self, request, format=None):
        '''retornar lista de caracteristicas del Apiview'''
        '''Tengo que retornar un objeto de response'''
        an_apiview = [
            'Usamos metodos HTTP como funciones( get, post, patch, put, delete',
            'Es similar a una vista tradicional de django',
            'Nos da mayor control sobre la logica de la app',
            'Esta mapeado manualmente a los url'

        ]
        '''Convierte la info en json, tiene q ser lista o diccionario'''
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, resquest):
        '''Crea un mensaje con neustro nombre '''
        # data = request.data pasa los datos
        serializer = self.serializers_class(data=resquest.data)

        # decir si esto es valido o no

        if serializer.is_valid():
            # si es valido veo el nombre de adentro
            # name esta definido en serializers
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

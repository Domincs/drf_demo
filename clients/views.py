from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from clients.models import Client


class ClientsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = Client.objects.filter().values()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.data:
            return Response(
                {"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            email = request.data["email"]

            Client.objects.create(
                first_name=first_name, last_name=last_name, email=email
            )
            return Response(
                {"message": "Client successfully created!"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            print("error: ", e)
            return Response(
                {"error": "Could not create client."},
                status=status.HTTP_400_BAD_REQUEST,
            )

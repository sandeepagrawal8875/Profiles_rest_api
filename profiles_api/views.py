from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiview = [
            "User HTTP methods as function(get,post,put,delete)",
            "is similar to start django view",
            "gives you the most control",
            "gives you the asus vivobook control",
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
from .mongo import tazakhabar_collection
from .serializers import TazaKhabarSerializer

class khabarListCreate(APIView):
    def post(self, request):
        serializer = TazaKhabarSerializer(data=request.data)
        if serializer.is_valid():
            res = tazakhabar_collection.insert_one(serializer.validated_data)
            return Response({"id": str(res.inserted_id)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class khabarDetail(APIView):
    def get(self, request, khabar_id):
        try:
            record = tazakhabar_collection.find_one({"_id": ObjectId(khabar_id)})
        except:
            return Response({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)

        if record:
            record["id"] = str(record["_id"])
            record.pop("_id")
            return Response(record)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, khabar_id):
        try:
            result = tazakhabar_collection.delete_one({"_id": ObjectId(khabar_id)})
        except:
            return Response({"error": "Invalid ID format"}, status=status.HTTP_400_BAD_REQUEST)

        if result.deleted_count:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

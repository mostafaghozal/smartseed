from rest_framework.views import APIView
from rest_framework.response import Response

from Farm.models import Farm
from Farm.serializers import FarmSerializer
from .models import Crop
from .serializers import CropSerializer
# from rest_framework.permissions import AllowAny

class CropView(APIView):
	# permission_classes = (AllowAny, )

	def get(self, request, format=None):
		farm_id = request.GET.get('farm_id')
		print(farm_id)
		try:
			crops = Crop.objects.filter(farm__id=farm_id)
			print(crops)
			serializer = CropSerializer(crops, many=True)
			return Response(serializer.data)
		except:
			return Response('Crop does not exists.')
		
	def post(self, request, format=None):
		try:
			crop = Crop()
			crop.farm = Farm.objects.get(id=request.data.get('farm_id'))
			crop.crop_type = request.data.get('crop_type')
			crop.longitude = request.data.get('longitude')
			crop.latitude = request.data.get('latitude')
			crop.save()
			print("crop",crop)
			serializer = CropSerializer(crop, many=False)
			return Response(serializer.data)
		except Exception as e:
			return Response(e)


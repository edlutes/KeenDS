from django.shortcuts import render
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view

from .serializers import FileSerializer, DataSerializer

import csv
import threading
from .models import Row


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
      
      file_serializer = FileSerializer(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          # Split the parsing thread
          # Instead of calling straight into parse_csv_data this should probably go through some data validation
          thread = threading.Thread(target =parse_csv_data, kwargs={'csv_file': file_serializer.data.get("file") })
          thread.start()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DataList(generics.ListCreateAPIView):
    queryset = Row.objects.all()
    serializer_class = DataSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Row.objects.all()
    serializer_class = DataSerializer

    
# Not used but could be needed depending on on long it takes to save the file
#@retry((FileNotFoundError, IOError), delay=1, backoff=2, max_delay=10, tries=100)
def parse_csv_data(csv_file):


    # Need to handle file format.  Currently passed in as /media/<file_name>
    csv_file = "."+csv_file

    with open (csv_file, mode ='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            observation_date = row['Observation Date']
            retail_sales_volume = row['Retail Sales Volume']
            retail_price = row['Retail Price']
            acv_distribution = row['ACV Distribution']
            competition = row['Competition']
            edlp = row['EDLP']
            trade_any_promo = row['Trade Any Promo']
            tv = row['TV']
            print_ad = row['Print']
            online_display = row['Online Display']
            preroll_video = row['Pre-roll Video']
            paid_search = row['Paid Search']
            public_relations = row['Public Relations']
            fsi = row['FSI']
            digital_coupon = row['Digital Coupon']
            shopper_marketing = row['Shopper Marketing']

            new_row=Row(Observation_Date=observation_date, 
                        Retail_Sales_Volume=retail_sales_volume, 
                        Retail_Price=retail_price, 
                        Acv_Distribution=acv_distribution,
                        Competition = competition,
                        Edlp = edlp,
                        Trade_Any_Promo = trade_any_promo,
                        Tv = tv,
                        Print_Ad = print_ad,
                        Online_Display = online_display,
                        Preroll_Video = preroll_video,
                        Paid_Search = paid_search,
                        Public_Relations = public_relations,
                        Fsi = fsi,
                        Digital_Coupon = digital_coupon,
                        Shopper_Marketing = shopper_marketing
                        )
            new_row.save()

    return







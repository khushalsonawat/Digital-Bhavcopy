from rest_framework import status
from rest_framework.response import Response




# class MarketDataView(ListAPIView):
#     queryset = MarketDataInfo.objects.all()

#     def check_symbol(self, symbol):
#         try:
#             obj = Details.objects.all().filter(symbol=symbol)
#         except:
#             return None

#         return obj

#     def get(self, request, symbol):
#         obj = self.check_symbol(symbol)
#         if obj:
#             instance = self.get_queryset.filter(symbol__symbol=symbol)
#             if instance:
#                 print(type(instance.data))

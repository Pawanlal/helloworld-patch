from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from .pagination import MyLimitOffsetPagination
from .permissions import IsStaffUser
from .serializers import InfoModelSerializer
from .models import Info


class InfoModelCreateAPIView(CreateAPIView):
    serializer_class = InfoModelSerializer
    # def get_serializer_class(self):
    #     return InfoModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        print("Ok the serializer is saved.")


class InfoModelListAPIView(ListAPIView):
    # queryset = Info.objects.all()
    serializer_class = InfoModelSerializer
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    permission_classes = [IsStaffUser, ]

    search_fields = ['name']
    order_fields = ['name', 'id']
    filterset_fields = ['name']

    def get_queryset(self):
        return Info.objects.all()


class InfoModelDestroyAPIView(DestroyAPIView):
    queryset = Info.objects.all()


class InfoModelUpdateAPIView(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer


class InfoModelRetrieveAPIView(RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer


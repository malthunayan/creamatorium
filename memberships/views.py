from django.forms import forms
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from branches.models import Branch


class ListMemberships(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = membershipsAPIs

    def get_queryset(self):
        queryset = Membership.objects.all()
        gym = self.request.query_params.get('gym',None)
        branch = self.request.query_params.get('branch',None)
        if gym is not None:
            branches = list(Branch.objects.filter(gym=gym).values_list('id', flat=True))
            queryset = queryset.filter(branch__in=branches)
        if branch is not None:
            queryset = queryset.filter(branch=branch)
        return queryset


class RetiveAndUpdateMemberships(generics.RetrieveUpdateAPIView):
    serializer_class = membershipsAPIs
    queryset = Membership.objects.all()

#payments
class ListAndCreateMembershipsPayments(generics.ListCreateAPIView):
    serializer_class = membershipPaymentsAPIs
    def get_queryset(self):
        queryset = MembershipPayments.objects.all()
        membership = self.request.query_params.get('membership', None)
        if membership is not None:
            queryset = queryset.filter(membership=membership)
        return queryset


class RetiveAndUpdateMembershipsPayments(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = membershipPaymentsAPIs
    queryset = MembershipPayments.objects.all()



class createMemberWithPayment(APIView):
    def post(self, request):
        memberShipSerializer = membershipsAPIView(data=request.data['membership'])
        if memberShipSerializer.is_valid():
            memberShipSerializer.save()
            request.data['payment']['membership'] = memberShipSerializer.data['id']
            paymentSerializer = membershipPaymentsAPIs(data=request.data['payment'])
            if paymentSerializer.is_valid():
                paymentSerializer.save()
            return Response(memberShipSerializer.data, status=status.HTTP_201_CREATED)
        return Response(memberShipSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

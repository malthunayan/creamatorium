from rest_framework import  generics
from .serializers import *
from branches.models import Branch


class ListAndCreateMemberships(generics.ListCreateAPIView):
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


class ListAndCreateMembershipsPayments(generics.ListCreateAPIView):
    serializer_class = membershipPaymentsAPIs
    def get_queryset(self):
        queryset = MembershipPayments.objects.all()
        membership = self.request.query_params.get('membership', None)
        if membership is not None:
            queryset = queryset.filter(membership__in=membership)
        return queryset


class RetiveAndUpdateMembershipsPayments(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = membershipPaymentsAPIs
    queryset = Membership.objects.all()



# Create your views here.

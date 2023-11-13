from rest_framework import generics, status
from rest_framework.response import Response
from .models import Operation
from .serializers import OperationSerializer
from .helpers import evaluate_expression


class EvaluateExpressionView(generics.CreateAPIView):
    serializer_class = OperationSerializer

    def create(self, request, *args, **kwargs):
        expression = request.data.get('expression')
        try:
            result = evaluate_expression(expression)
            operation = Operation.objects.create(expression=expression, result=result)
            serializer = self.get_serializer(operation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class HistoryView(generics.ListAPIView):
    queryset = Operation.objects.all().order_by('-timestamp')
    serializer_class = OperationSerializer

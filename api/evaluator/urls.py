from django.urls import path
from .views import EvaluateExpressionView, HistoryView

urlpatterns = [
    path('evaluate/', EvaluateExpressionView.as_view(), name='evaluate_expression'),
    path('history/', HistoryView.as_view(), name='operation_history'),
]

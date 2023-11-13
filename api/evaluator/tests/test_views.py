from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch


class EvaluateExpressionViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_evaluate_expression_view_success(self):
        data = {'expression': '2 + 2'}
        response = self.client.post('/api/evaluate/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('result', response.data)
        # Add more assertions as needed

    @patch('evaluator.views.evaluate_expression', side_effect=Exception('Some error'))
    def test_evaluate_expression_view_error(self, mock_evaluate_expression):
        data = {'expression': 'invalid_expression'}
        response = self.client.post('/api/evaluate/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)
        # Add more assertions as needed


class HistoryViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_history_view(self):
        response = self.client.get('/api/history/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions as needed

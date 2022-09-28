from django.shortcuts import render
from rest_framework import generics
from .models import Expenses, Income, Category
from accounting.serializers import ExpensesSerializer, IncomeSerializer, CategorySerializer


class ExpenseAPIView(generics.ListAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer


class IncomeAPIView(generics.ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class CategiryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
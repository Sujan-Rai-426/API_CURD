from django.shortcuts import render

from .models import Note, Transaction
from .serializers import Note_Serializer, Transaction_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Sum


# Create your views here.
@api_view(['GET', 'POST'])
def Note_View(request):
    queryset = Note.objects.all()
    serializer = Note_Serializer(queryset, many=True)
    return Response(
        { "data" : serializer.data }
    )


@api_view( ["GET", "POST"] )
def Transaction_View(request):
    queryset = Transaction.objects.all().order_by("-pk")
    serializer = Transaction_Serializer(queryset, many=True)
    return Response(
        { 
            "data" : serializer.data, 
            "total" : round(queryset.aggregate(total = Sum("amount")) ['total'] or 0, 2)  # <-- To get total at last
        }
    )

# class for performing the CURD operations
class Transaction_View_Class(APIView):
    
    # GET method
    def get(self, request):
        queryset = Transaction.objects.all().order_by("-pk")
        serializer = Transaction_Serializer(queryset, many=True)
        return Response(
            { "data" : serializer.data, "total" : queryset.aggregate(total = Sum("amount")) ['total'] or 0 }
        )
    
    # POST method
    def post(self, request):  # sourcery skip: class-extract-method
        data = request.data #taking data from user
        serializer = Transaction_Serializer(data = data) #Serialize the data taken from user 
        if not serializer.is_valid(): # Check if the data entered by user is valid or not and if not return error , 
            return Response(
                {"message" : "data not saved", "error" : serializer.errors }
            )
        serializer.save() #if valid than store to database or save
        return Response(
            { "message": "data saved", "data": serializer.data }
        )
    
    # PUT method
    def put(self, request):
        return Response(
            { "message": "this is a put method" }
        )
    
    # PATCH method --> for partial updation
    def patch(self, request):
        data = request.data
        if not data.get('id'):    # if not ID return error
            return Response(
                {"message": "Data updation failed!", "error": "data ID is required" }
            )
        
        # get specific transaction data that need to be updated , with help of  id 
        transaction = Transaction.objects.get(id = data.get('id') )
        serializer = Transaction_Serializer(transaction, data = data, partial = True )
        
        if not serializer.is_valid(): # Check if the data entered by user is valid or not and if not return error , 
            return Response(
                {"message" : "data not saved", "error" : serializer.errors }
            )
        serializer.save() #if valid than store to database or save
        return Response(
            { "message": "data saved", "data": serializer.data }
        )
        
    
    # DELETE method
    def delete(self, request):
        data = request.data
        if not data.get('id'):    # if not ID return error
            return Response(
                {"message": "Data updation failed!", "error": "data ID is required" }
            )
        
        # get specific transaction data that need to be updated , with help of  id 
        transaction = Transaction.objects.get(id = data.get('id') ).delete()
        return Response(
            { "message": "data deleted", "data": {} }
        )



# Class for performing CURD operation in the Note model 
class Note_View_Class(APIView):
    
    # Put operation function [C->Create]
    def post(self, request):
        data = request.data
        serializer = Note_Serializer(data, many=True)
        if not serializer.is_valid(): 
            return Response(
                { "message": "Data Creation Failed", "error": serializer.error }
            )       
        serializer.save()     
        return Response(  
            {  "data" : serializer.data  }
        )

    
    # Get Operation fucntion [R-> READ]
    def get(self, request):
        queryset = Note.objects.all().order_by("-pk")
        serializer = Note_Serializer(queryset, many=True)
        return Response(
            {"data" : serializer.data}
        )
    
    
    # Patch Operation (U -> Update)
    def patch(self, request):
        data = request.data
        if not data.get("-id"):
            return Response(
                { "message": "Data Updation Failed!" , "error" : "Data ID is needed." }
            )
        note = Note.objects.get(id = data.get("id") )
        serializer = Note_Serializer(note, data=data, partial = True)
        if not serializer.is_valid():
            return Response(
                { "message": "data not save", "error": serializer.error }
            )
        serializer.save()
        return Response(
            { "data" : serializer.data }
        )
    
    
    # DELETE method
    def delete(self, request):
        data = request.data
        if not data.get('id'):    # if not ID return error
            return Response(
                {"message": "Data updation failed!", "error": "data ID is required" }
            )
        
        # get specific transaction data that need to be updated , with help of  id 
        note = Note.objects.get(id = data.get('id') ).delete()
        return Response(
            { "message": "data deleted", "data": {} }
        )
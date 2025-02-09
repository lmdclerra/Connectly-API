from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

# Create your views here.

# R - Read from CRUD
def get_users(request):
    try:
        users = list(User.objects.values('id', 'username','email', 'created_at'))
        return JsonResponse(users, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
# R - Read SINGLE User from CRUD
def get_user(request, user_id):
    if request.method == 'GET':
        try:            
            user = User.objects.filter(id=user_id).first()            
            return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


# C - Create from CRUD
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create(username=data['username'], email=data['email'])
            return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400) 
        
# U - Update from CRUD
@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)           
            user = User.objects.filter(id=user_id).first()            
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.save() # save user back to database
            return JsonResponse({'id': user.id, 'message': 'User updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# D - Delete from CRUD
@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.filter(id=user_id).first()            
            user.delete() # delete user from the database
            return JsonResponse({'message': 'User deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


def get_posts(request):
    try:
        posts = list(Post. objects.values('id', 'content', 'author', 'created_at'))
        return JsonResponse(posts, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def create_post(request):
    # import pdb; pdb.set_trace()  # Add this breakpoint
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            author = User.objects.get(id=data['author'])
            post = Post.objects.create(content=data['content'], author=author)
            return JsonResponse({'id': post.id, 'message': 'Post created successfully'}, status=201)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
class UserListCreate(APIView):
    def get(self, request):
                users = User.objects.all()
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)
            
    def post(self, request):
                serializer = UserSerializer (data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_Request)


class PostListCreate(APIView):
    def get(self, request):
          posts = Post.objects.all()
          serializer = PostSerializer(posts, many=True)
          return Response(serializer.data)
     
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_Request)


class CommentListCreate(APIView):
    def get(self, request):
          comments = Comment.objects.all()
          serializer = CommentSerializer(comments, many=True)
          return Response(serializer.data)
     
     
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


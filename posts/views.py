from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Post

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
            # user = User.objects.filter(id=user_id).first()
            user = get_object_or_404(User, id=user_id) # filter one record if found
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
            # user = User.objects.filter(id=user_id).first()
            user = get_object_or_404(User, id=user_id)            
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.save()
            return JsonResponse({'id': user.id, 'message': 'User updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# D - Delete from CRUD
@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            # user = User.objects.filter(id=user_id).first()
            user = get_object_or_404(User, id=user_id)
            user.delete()
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
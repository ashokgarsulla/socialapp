from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def feed_view(request):
    print("feed working....................")
    if request.user.is_authenticated:
        print('....user Authenticated.....')
        print(request.user.id)
        if request.method == 'POST':
            print("Succce post.......called")
            fm = PostForm(request.POST,request.FILES)

            print('----------------')
            print(fm)
            # if post.is_valid():
            #     post.save()
            # print()
            return HttpResponseRedirect('/postlist')
        else:
            fm = PostForm()
        return render(request,'feed/createpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/accounts/login')
        


# def feed_view(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             fm = PostForm()
#             return render(request,'feed/createpost.html',{'form':fm})
#         else:
#             fm = PostForm()
#     else:
#         return HttpResponseRedirect('/accounts/login')
    



def post_list_view(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        print(posts)
        for i in posts:
            print(i.userid)
            print(i.caption)
            print(i.attachment)
            print("-----------------")
        return render(request,'feed/postlist.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/accounts/login')
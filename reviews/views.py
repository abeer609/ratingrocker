from django.shortcuts import render,get_object_or_404,redirect
from myAdmin.models import Category,Product,Review,BlogPost, PostReview
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.mail import send_mail
from supabase import create_client, Client
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

def send_notification_email(name, email):
    subject = 'Contact Form'
    message = 'Someone filled the form'
    from_email = 'ayushguptaa@yahoo.com'
    recipient_list = ['ayushguptaa@yahoo.com']
    send_mail(subject, message, from_email, recipient_list)

# def error_handling(request, product_id, product_slug):
#     categories = Category.objects.all()
#     all_categories = categories
#     categories = categories[:6]
#     latest_reviews = Review.objects.order_by('id')[:6]
#     return render(request, 'home.html',{'categories': categories,'reviews':latest_reviews,'all_categories':all_categories})

def home(request):
    categories = Category.objects.all()
    all_categories = categories
    categories = categories[:6]
    latest_reviews = Review.objects.order_by('id')[:6]
    return render(request, 'home.html',{'categories': categories,'reviews':latest_reviews,'all_categories':all_categories})

# def custom_redirect_view(request, review_text):
#     categories = Category.objects.all()
#     all_categories = categories
#     categories = categories[:6]
#     latest_reviews = Review.objects.order_by('id')[:6]
#     return render(request, 'home.html',{'categories': categories,'reviews':latest_reviews,'all_categories':all_categories})
    
def privacy_policy(request):
    categories = Category.objects.all()
    all_categories = categories
    return render(request, 'privacy_policy.html',{'all_categories': all_categories})

def terms(request):
    categories = Category.objects.all()
    all_categories = categories
    return render(request, 'terms.html',{'all_categories': all_categories})

def faq(request):
    categories = Category.objects.all()
    all_categories = categories
    return render(request, 'faq.html',{'all_categories': all_categories})

def about_us(request):
    categories = Category.objects.all()
    all_categories = categories
    return render(request, 'about.html',{'all_categories': all_categories})

def category_products(request,category_id, slug):
    try:
        category = Category.objects.get(id=category_id)
        
        products = Product.objects.filter(category=category)
        product_count = products.count()
        categories = Category.objects.all()
        all_categories = categories
        return render(request, 'category.html', {'all_categories': all_categories,'category': category, 'products': products,'product_count':product_count,'categories':categories})
    except Category.DoesNotExist:
        all_categories = Category.objects.all()
        categories = Category.objects.all()
        return render(request, 'all_category.html', {'all_categories': all_categories,'categories':categories})
    

# @login_required(login_url='/user/login')
# def product_review(request,product_id, slug):
#     categories = Category.objects.all()
#     all_categories = categories
#     product = get_object_or_404(Product, pk=product_id, slug=slug)
#     if request.method == 'POST':
#         user =  request.user if request.user.is_authenticated else request.POST['username']
#         title = request.POST['title']
#         text = request.POST['text']
#         rating = int(request.POST['rating-input'])
#         image = request.FILES.get('image')
#         subject = f'New Review Submitted'
#         message = f'A new review has been submitted for product--> "{product}": {text}'
#         from_email = 'judekilos@gmail.com'
#         recipient_list = ['ratingrocker2023@gmail.com']
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         review = Review(product=product, user=user, title=title, text=text, rating=rating, image=image)
#         review.save()
#         return redirect("home")

#     return render(request, 'write-review.html',{'all_categories': all_categories,'product':product})

def read_review(request,product_id, slug):
    categories = Category.objects.all()
    all_categories = categories
    try:
        product = Product.objects.get(pk=product_id, slug=slug)
    except Product.DoesNotExist:
        return redirect("home")
    # product_name = product.name

    reviews = Review.objects.filter(product_id=product_id)
    print(reviews)
    return render(request, 'read-reviews.html',{'product': product, 'reviews': reviews})


    # url: str = 'https://jjaunsecfiwnxpllmyub.supabase.co'
    # key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqYXVuc2VjZml3bnhwbGxteXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTkwNzg2MjEsImV4cCI6MjAxNDY1NDYyMX0.8JZW25HmZG8YGVE6j2iQaAv7Jh_QPv-H5eaBRzl4kIQ"
    # supabase: Client = create_client(url, key)

    # data, count = supabase.table('reviews').select('*').eq('product_id', product_id).execute()
    
    # reviews = Review.objects.filter(product=product)
    # if not data:
    #     reviews = []
    # else:
    #     reviews = data[1]
    # return render(request, 'read-reviews.html',{'all_categories': all_categories,'product': product, 'reviews': reviews, 'product_name' : product_name})

def blog(request):
    categories = Category.objects.all()
    all_categories = categories
    blog_posts = BlogPost.objects.all()
    return render(request, 'all_blog.html', {'all_categories': all_categories,'blog_posts': blog_posts})

def blog_detail(request,blog_id, slug):
    categories = Category.objects.all()
    all_categories = categories
    try:
        blog_post = BlogPost.objects.get(id=blog_id, slug=slug)
    except BlogPost.DoesNotExist:
        return redirect("home")
    
    return render(request, 'blog_post_detail.html', {'all_categories': all_categories,'blog_post': blog_post})

def all_category(request):
    all_categories = Category.objects.all()
    categories = Category.objects.all()
    return render(request, 'all_category.html', {'all_categories': all_categories,'categories':categories})

def search(request):
    try:
        categories = Category.objects.all()
        all_categories = categories
        query = request.POST.get('query')
        category = request.POST.get('category')
        product_query = Product.objects.all()
        if category != 'All Categories':
            selected_category = Category.objects.get(category_name=category)
            product_query = product_query.filter(category=selected_category)
    
            
        product_query = product_query.filter(Q(name__icontains=query) | Q(description__icontains=query))
        filtered_products = product_query.distinct()
        return render(request, 'search.html', {'all_categories': all_categories,'products': filtered_products,'query':query})
    except Category.DoesNotExist:
        categories = Category.objects.all()
        all_categories = categories
        categories = categories[:6]
        latest_reviews = Review.objects.order_by('id')[:6]
        return render(request, 'home.html',{'categories': categories,'reviews':latest_reviews,'all_categories':all_categories})


def product_review(request, product_id, product_slug):
    
    categories = Category.objects.all()
    all_categories = categories
    try:
        product = Product.objects.get(pk=product_id, slug=product_slug)
    except Product.DoesNotExist:
        return redirect("home")

    if request.method == 'POST':
        user = request.POST['username']
        title = request.POST['title']
        text = request.POST['text']
        rating = int(request.POST['rating-input'])
        image = request.FILES.get('image')
        Review.objects.create(username=user, product_id=product_id, title=title, text=text, rating=rating, image=image)
        return redirect("home")


         

        
        # url: str = 'https://jjaunsecfiwnxpllmyub.supabase.co'
        # key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqYXVuc2VjZml3bnhwbGxteXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTkwNzg2MjEsImV4cCI6MjAxNDY1NDYyMX0.8JZW25HmZG8YGVE6j2iQaAv7Jh_QPv-H5eaBRzl4kIQ"
        # supabase: Client = create_client(url, key)

 
        # supabase_table = "reviews"

  
        # review = {
        #     "user": user,
        #     "title": title,
        #     "text": text,
        #     "rating": rating,
        #     "product_name": product.name,
        #     "product_id": product_id
        # }
        # data, count = supabase.table('reviews').insert(review).execute()

        
        # subject = 'New Review Submitted'
        # message = f'A new review has been submitted for product "{product}": {text}'
        # from_email = 'judekilos@gmail.com'
        # recipient_list = ['ratingrocker2023@gmail.com']
        # send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        # return redirect("home")
    return render(request, 'write-review.html', {'all_categories': all_categories, 'product': product})

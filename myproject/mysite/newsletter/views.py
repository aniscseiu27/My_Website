from django.contrib import messages
from urllib import quote_plus
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, SignUpForm
from .forms import UserPostForm
from .models import SignUp
from .models import UserPost

def home(request):
	title = "Sign Up Now"
	form = SignUpForm(request.POST or None)


	context = {
	    "title": title,
	    "form": form,
	}

	

	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
			instance.full_name = full_name


		#if not instance.full_name:
		#	instance.full_name = "anis"
		instance.save()

		context = {
		"title": "Thank you"
		}

	if request.user.is_authenticated and request.user.is_staff:
		#print(SignUp.objects.all())
		# i=1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i+=1

		queryset=SignUp.objects.all().order_by("-timestamp")#.filter(full_name__iexact="anis")
		print(SignUp.objects.all().order_by("-timestamp").filter(full_name__iexact="anis").count())

		context = {
		   "queryset": queryset
		}

	return render(request, 'home.html', context)


def contact(request):
	title = "Contact Us"
	title_align_center = False
	form = ContactForm(request.POST or None)

	if form.is_valid():
		#for key, value in form.cleaned_data.iteritems():
		#	print key, value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		#print email, message, full_name

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'aniscseiu@gmail.com']
		contact_message = "%s %s via %s"%(
			form_full_name,
		    form_message,
		    form_email)

		send_mail(subject, 
			contact_message, 
			from_email,
			to_email, 
			fail_silently=True)
		
		return HttpResponseRedirect('/contact/success/')

		


	context = {
	    "form": form,
	    "title": title,
	    "title_align_center": title_align_center,
	}

	return render(request, "forms.html", context)

def contact_success(request):
	return render(request, 'contact_success.html')

def index(request):
	return (request, 'blog/blog.html')


def post_create(request):
	form = UserPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		if not request.user.is_authenticated():
			raise Http404("You have not logged in yet ! Please Log in first :)")
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	    "form": form,
	}
	return render(request, "post/post_form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(UserPost, id=id)

    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,   
    }

    return render(request, "post/post_detail.html", context)

def post_list(request):
	queryset_list = UserPost.objects.all() # order_by ("-timestamp")

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 10) # show 25 contacts per page

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page
	    queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
	return render(request, "post/post_list.html", context)



def post_update(request, id=None):
	instance = get_object_or_404(UserPost, id=id)

	form = UserPostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Saved", extra_tags="some-tag")
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
	    "title": instance.title,
	    "instance": instance,
	    "form": form,
	}
	return render(request, "post/post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(UserPost, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("post:list")

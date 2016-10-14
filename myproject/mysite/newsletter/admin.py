from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp, Post
from .models import UserPost

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp", "updated"]
	form = SignUpForm
	#class meta:
		#model = SignUp

class UserPostAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	class meta:
		model = UserPost
			

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Post)
admin.site.register(UserPost, UserPostAdmin)

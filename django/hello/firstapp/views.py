# from .forms import UserForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from.models import UpnGnssProject100
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from django.views.generic import ListView, DetailView, CreateView, TemplateView

from django.contrib.auth.decorators import login_required, permission_required


from django.db.models import Q

from django_tables2 import SingleTableView

from .tables import dataTable



def index(request):
	upn = list(UpnGnssProject100.objects.all())
	return render (request, 'index.html', {'data': upn})


# Вывод странички about
def about(request):
	return render (request, 'about.html')
	
# @login_required
# @permission_required(['firstapp.change_UpnGnssProject100', 'firstapp.view_UpnGnssProject100'], raise_exception=True)
def edit(request , id):
	try:
		UpnGnss = UpnGnssProject100.objects.get(id=id)

		if request.method =="POST":
			UpnGnss.region = request.POST.get("region")
			UpnGnss.nameua = request.POST.get("nameua")
			UpnGnss.nameen = request.POST.get("nameen")
			UpnGnss.coatuu_code = request.POST.get("coatuu_code")
			UpnGnss.y = request.POST.get("y")
			UpnGnss.x = request.POST.get("x")
			UpnGnss.status_np_za_admin_podil = request.POST.get("status_np_za_admin_podil")
			UpnGnss.districtce = request.POST.get("districtce")
			UpnGnss.meteo = request.POST.get("meteo")
			UpnGnss.status = request.POST.get("status")
			UpnGnss.norway_project = request.POST.get("norway_project")
			UpnGnss.grounding = request.POST.get("grounding")
			UpnGnss.site_repor = request.POST.get("site_repor")
			UpnGnss.reconaissa = request.POST.get("reconaissa")
			UpnGnss.cabinet = request.POST.get("cabinet")
			UpnGnss.statusid = request.POST.get("statusid")
			UpnGnss.dgk = request.POST.get("dgk")
			UpnGnss.dgk_contac = request.POST.get("dgk_contac")
			UpnGnss.agreement = request.POST.get("agreement")
			UpnGnss.primary_co = request.POST.get("primary_co")
			UpnGnss.rigc_ready = request.POST.get("rigc_ready")
			UpnGnss.sitechange = request.POST.get("sitechange")
			UpnGnss.installati = request.POST.get("installati")
			UpnGnss.notes = request.POST.get("notes")
			UpnGnss.save()
			return HttpResponseRedirect("/")
		else:
			return render(request, "edit.html", {"UpnGnss":UpnGnss})
	except UpnGnssProject100.DoesNotExist:
		return HttpResponseNotFound("<h2>Object not found</h2>")


# @permission_required(['firstapp.view_UpnGnssProject100'])
# Вывод странички map
def map(request):
	return render (request, 'map.html')


# Работа поиска на страничке!!!(поиск даных по имени на укр и англ)
class search(ListView):
	model = UpnGnssProject100
	template_name = 'search_results.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = UpnGnssProject100.objects.filter(
			Q(nameua__icontains=query) | Q(nameen__icontains=query)
			)
		return object_list 



# Відображення форми реєстрації аккаунту V.1.0

# class RegisterUser(TemplateView):
# 	template_name = "register.html"

# 	def dispatch(self, request, *args, **kwargs):
# 		context = {}
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			email = request.POST.get('email')
# 			password = request.POST.get('password')
# 			password2 = request.POST.get('password2')

# 			if password == password2:
# 				User.objects.create_user(username, email, password)
# 				return redirect(reverse("login"))
# 			else:
# 				context['error'] = "Passwords don\'t match"
# 				# return redirect(reverse("register"))
# 		return render(request, self.template_name, context)



# Відображення форми реєстрації аккаунту V.2.0

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})






# Відображення сторінки Входу в аккаунт V.1.0



# class LoginView(TemplateView):
# 	template_name = "login.html"

# 	def dispatch(self, request, *args, **kwargs):
# 		context = {}
# 		if request.method == 'POST':
# 			username = request.POST['username']
# 			password = request.POST['password']
# 			user = authenticate(request, username=username, password=password)
# 			if user is not None:
# 				login(request,user)
# 				return redirect("profile")
# 			else:
# 				context['error'] = "Login or password is incorrect"
# 		return render(request, self.template_name, context)




# Відображення сторінки Входу в аккаунт V.2.0 (не використовується через користування views з корневих папок django)



# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})






# Відображення сторінки профілю



def profile(request):
	return render(request, 'registration/profile.html', {'section': 'profile'})






# ТЕЕЕЕСТТТТ DjangoTables2!!! не закінчений!

class data_table(SingleTableView):
	model = UpnGnssProject100
	table_class = dataTable
	template_name = 'index_test.html'
	table_pagination = False



# def search(request):
# 	upn_search = list(UpnGnssProject100.objects.all())
# 	return render (request, 'search_results.html', {'data_search': upn_search})











"""def index(request):
	if request.method == "POST":
		name = request.POST.get("name")
		# age = request.POST.get("age")		#получения значения поля age
		return HttpResponse("<h2>Hello, {0}</h2>".format(name))
	else:
		userform = UserForm()
		return render(request, "index.html", {"form": userform})"""



"""def index(request):
	langs = ["English", "German", "French", "Spanish", "Chinese"]
	data = {"n": 0}
	return render(request, "index.html", context={"langs": langs})
	return render(request, "index.html",context=data)"""







"""def mainpage(request):
	return HttpResponse("Main page")

def about(request):
	return HttpResponse("About")

def contact(request):
	return HttpResponseRedirect("/about")

def details(request):
	return HttpResponsePermanentRedirect("/")
"""



"""def products(request, productid = 21):
	output = "<h2>Product № {0}</h2>".format(productid)
	return HttpResponse(output)

def users(request, id = 1, name= "Ron"):
	output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id,name)
	return HttpResponse (output)
"""



"""def index(request):
	return HttpResponse("<h2>Main page!</h2>")

def about(request):
	return HttpResponse("<h2>about</h2>")

def contact(request):
	return HttpResponse("<h2>Contacts</h2>")

"""

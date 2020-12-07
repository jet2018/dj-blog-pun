from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Gallery, About, AboutTheParty, Achievement, Prospective, Candidate, Blog
from django.core.mail import send_mail
from .forms import galleryForm
# Create your views here.

class HomePage(TemplateView):
    template_name = 'powerapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        context["top_three_posts"] = Blog.objects.filter(is_published=True).order_by('-upload_date')[:3]
        context["next_three_posts"] = Blog.objects.filter(is_published=True).order_by('-upload_date')[3:6]
        context["last_three_posts"] = Blog.objects.filter(is_published=True).order_by('-upload_date')[6:9]
        
        context["top_three_images"] = Gallery.objects.filter(is_published=True).order_by('-upload_date')[:3]
        context["next_three_images"] = Gallery.objects.filter(is_published=True).order_by('-upload_date')[3:6]
        context["last_three_images"] = Gallery.objects.filter(is_published=True).order_by('-upload_date')[7:9]

        context['why_nrm'] = AboutTheParty.objects.all()[:1]
        return context

class Sensitisation(TemplateView):
    template_name = 'powerapp/sensitisation.html'

class GalleryView(ListView):
    paginate_by = 12
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'powerapp/gallery.html'

    def get_queryset( self ):
        gallery = super().get_queryset()
        gallery =Gallery.objects.filter(is_published = True).order_by('-upload_date')
        return gallery


def addImage(request):
    addedBy = User.objects.get(pk = request.user.id)
    if request.method == 'POST' and request.FILES:
        pik = request.FILES['image']
        gallary = Gallery.objects.create(Image =pik, short_description=request.POST.get('short_description'), added_by = addedBy)
        if gallary:
            messages.success(request, 'Your image has been submitted for further reviews. Thank you for your contribution.')
            redirect('powerapp:gallery')
        else:
            messages.error(request, 'There was an error submitting your image, please try again')
            redirect('powerapp:gallery')
    return redirect('powerapp:gallery')

class aboutUsView(TemplateView):
    template_name = 'powerapp/aboutUs.html'
#     i have to seend three rows of the most current photos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context


# done
class aboutParty(TemplateView):
    template_name = 'powerapp/about_the_party.html'
#     i have to seend three rows of the most current photos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nrm"] = AboutTheParty.objects.all()[:1]
        return context


# achievements of the party
# done 
class AchievementsView(ListView):
    paginate_by = 9
    model = Achievement
    context_object_name = 'achievements'
    template_name = 'powerapp/achievements.html'

    def get_queryset( self ):
        achievements = super().get_queryset()
        achievements =Achievement.objects.filter(is_published = True).order_by('-upload_date')
        return achievements

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context

# done
class DetailedAchievement(DetailView):
    template_name='powerapp/single-achievement.html'
    model = Achievement
    context_object_name = 'achievement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context





# prospectives
# done
class ProspectivesView(ListView):
    paginate_by = 9
    model = Prospective
    context_object_name = 'prospectives'
    template_name = 'powerapp/prospectives.html'

    def get_queryset( self ):
        prospectives = super().get_queryset()
        prospectives =Prospective.objects.filter(is_published =True).order_by('-upload_date')
        return prospectives

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context

# done
class DetailedProspective(DetailView):
    template_name='powerapp/single-prospective.html'
    model = Prospective
    context_object_name = 'prospective'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context


# blogs
# done
class BlogView(ListView):
    template_name='powerapp/blog.html'
    model = Blog
    paginate_by = 9
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        context["blog"] = Blog.objects.filter(is_published=True).order_by('-upload_date')
        return context
# done
class DetailedBlog(DetailView):
    template_name='powerapp/single-blog.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context

class CandidatesView(ListView):
    template_name='powerapp/candidates.html'
    model = Candidate
    paginate_by = 9
    context_object_name = 'candidates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        context["candidates"] = Candidate.objects.filter(is_published=True)
        return context

# done
class DetailedCandidate(DetailView):
    template_name='powerapp/single-blog.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fullAbout"] = About.objects.all()[:1]
        return context
# i stoped here, to resume from here tomorrow
def addCandidate(request):
    addedBy = User.objects.get(pk = request.user.id)
    if request.method == 'POST' and request.FILES:
        pik = request.FILES['image']
        full_name = request.POST['full_name']
        full_name = request.POST['full_name']
        full_name = request.POST['full_name']
        full_name = request.POST['full_name']
        full_name = request.POST['full_name']

        if gallary:
            messages.success(request, 'Your image has been submitted for further reviews. Thank you for your contribution.')
            redirect('powerapp:gallery')
        else:
            messages.error(request, 'There was an error submitting your image, please try again')
            redirect('powerapp:gallery')
    return redirect('powerapp:gallery')


def createAccount(request):
    if request.is_ajax():
        username= request.POST.get('username')
        email= request.POST.get('email')
        password1= request.POST.get('password1')
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        password2= request.POST.get('password2')

        if password1 != password2:
            result = "Passwords are not matching"
            classNow = 'danger'
        else:
            if User.objects.filter(username=username).exists():
                result = "The username is already taken"
                classNow = 'warning'
            elif User.objects.filter(email=email).exists():
                result = "The email is associated with another account"
                classNow = 'warning'
            else:
                user = User.objects.create_user(username = username,password=password2,  email = email, first_name = fname, last_name=lname)
                user.save()
                result = "Account created successfully, you can now login"
                classNow = 'success'

        return JsonResponse({"result":result, "class":classNow}, status = 200)
        # am here


def login(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            result = "Login successfull"
            classNow ="success"
        else:
            result = "No member is associated with the given credentials"
            classNow = "danger"
        return JsonResponse({"result":result, "class":classNow}, status = 200)
    return render(request, "powerapp/index.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def likeapost(request):
    if request.is_ajax():
        post = get_object_or_404(Gallery, pk = request.GET.get('id'))
        if post.likes.filter(id = request.user.id).exists():
            post.likes.remove(request.user)
        else:
           post.likes.add(request.user)

        countNow = post.total_likes
        return JsonResponse({
            "result":'ok',
            'countNow':countNow
        })


def sendEmail(request):
    if request.is_ajax():
        emailFrom = request.POST.get('email')
        emailTo = 'example@gmail.com'
        body = request.POST.get('body')
        subject = request.POST.get('name')

        mysend = send_mail(subject,body,emailFrom, [emailTo])
        if mysend:
            return JsonResponse({'result':True}, status = 200)
        else:
            return JsonResponse({'result':False}, status = 400)
    return





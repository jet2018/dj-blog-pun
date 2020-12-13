from django.urls import path
from .views import (
    HomePage,
    AchievementsView,
    DetailedAchievement,
    login,
    logout,
    aboutUsView,
    aboutParty,
    CandidatesView,
    DetailedCandidate,
    createAccount,
    likeapost,
    sendEmail,
    GalleryView,
    ProspectivesView,
    DetailedProspective,
    BlogView,
    Sensitisation,
    DetailedBlog,
    addImage,
    # manifesto,
    addCandidate,
    )

app_name='powerapp'
urlpatterns = [
    # index page
    path("", HomePage.as_view(), name="index"),
    # candidates
    path("candidates", CandidatesView.as_view(), name="candidates"),
    path("candidates/<pk>/short-profile", DetailedCandidate.as_view(), name="candidate-details"),
    # achievements
    path("achievements", AchievementsView.as_view(), name="achievements"),
    path("achievements/<pk>/details", DetailedAchievement.as_view(), name="achievement-details"),
    # prospectives
    path("prospectives", ProspectivesView.as_view(), name="prospectives"),
    path("prospectives/<pk>", DetailedProspective.as_view(), name="prospective-detail"),
    # gallery
    path('gallery', GalleryView.as_view(), name="gallery"),
    # auth
    path("login", login, name="login"),
    path("signup", createAccount, name="signup"),
    path("logout", logout, name="logout"),
    # postlikes
    path("like", likeapost, name="likeImage"),
    # path("manifesto", manifesto, name="manifesto"),
    # about
    path("about-us", aboutUsView.as_view(), name="about-us"),
    path("about-the-party", aboutParty.as_view(), name="about-nrm"),
    # full blog
    path("blog", BlogView.as_view(), name="blog"),
    path("blog/<pk>/details", DetailedBlog.as_view(), name="single-blog"),
    # send an email
    path('send-email', sendEmail, name="sendEmail"),
    path('add-image', addImage, name="addImage"),
    path('add-candidate', addCandidate, name="add-candidate"),
    path("sensitisation", Sensitisation.as_view(), name="sensitisation"),

]

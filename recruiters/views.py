from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Applicants, Selected
from candidates.models import Profile, Skill
from .forms import NewJobForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponse


def rec_details(request):
    context = {
        'rec_home_page': "active",
        'rec_navbar': 1,
    }
    return render(request, 'recruiters/details.html', context)

def download_resume(request, username):
    profile = get_object_or_404(Profile)
    if not profile.resume:
        return HttpResponse("Resume not found")
    response = HttpResponse(profile.resume, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.resume.name}"'
    return response
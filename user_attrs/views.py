from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render

from .models import UserAttribute

User = get_user_model()


@login_required
def index(request):
    UserFormSet = inlineformset_factory(
        parent_model=User,
        model=UserAttribute,
        fields=('att_name', 'score', 'hidden'),
        extra=1,
    )

    if request.method == 'POST':
        formset = UserFormSet(request.POST, request.FILES, instance=request.user)
        if formset.is_valid():
            formset.save()

    formset = UserFormSet(instance=request.user)
    return render(request, context={'formset': formset}, template_name='index.html')

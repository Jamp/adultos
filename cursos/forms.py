# -*- coding: utf-8 -*-
from django import forms
from models import Region


class DistritoForm(forms.Form):
    nombre = forms.CharField(max_length=20, min_length=4)
    region = forms.ModelChoiceField(queryset=Region.objects.all())

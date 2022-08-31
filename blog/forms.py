from django import forms
from blog.models import Post
from patient_doctor.models import Appoinment
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

# -------------------------------------------------

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','category','summary','content','draft']
        labels = {'title':'Title','image':'Image','category':'Category','summary':'Summary','content':'Content'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title','maxlength':'200'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-select'}),
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Content'})
        }

class AForm(forms.ModelForm):
    specification = forms.CharField(max_length=225)
    add_date = forms.DateField(widget=AdminDateWidget())
    start_time = forms.TimeField(widget=AdminTimeWidget())


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = ['specification','add_date','start_time']
        labels = {'specification':'Specification','add_date':'Add Date','start_time':'Time'}
        widgets = {
        'specification':forms.TextInput(attrs={'class':'form-control'}),
        'add_date' : AdminDateWidget(),
        'start_time' : AdminTimeWidget()
        }

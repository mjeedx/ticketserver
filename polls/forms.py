from django.forms import ModelForm
from polls.models import Img


class UploadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UploadForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['userId'].required = False


    class Meta:
        model = Img
        fields = ('title', 'categoryId', 'photo', 'userId', 'ip')

# class UploadForm(forms.Form):
#     userId = forms.IntegerField
#     title = forms.CharField
#     categoryId = forms.CharField
#     photo = forms.ImageField

from django import forms
from .models import PostModel, Comment, Profile


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))

    class Meta:
        model = PostModel
        fields = ('title', 'content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))

    class Meta:
        model = Comment
        fields = ('content',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'firstname', 'lastname', 'age', 'website', 'gender'

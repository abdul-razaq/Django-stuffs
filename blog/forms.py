from django import forms
from .models import Post

# Create a form for the Post model
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)
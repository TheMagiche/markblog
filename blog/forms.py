from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text','thumbnail')
        
        widgets ={
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            # 'thumbnail': forms.ImageField(attrs={'class': 'thumbnail card-img-top'}),
        }



class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
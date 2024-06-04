# LIBRARIES
from django import forms

# MODELS
from .models import BlogPageComment



# FORM CLASSES



class CommentForm(forms.ModelForm):
    
    class Meta:

        model = BlogPageComment

        fields = [
            'text',
        ]

    text = forms.CharField(max_length=1500, label="Body", widget=forms.Textarea(attrs={'class':'md-textarea form-control', 'placeholder':'comment here...', 'rows':'4',}))# max max_length = required

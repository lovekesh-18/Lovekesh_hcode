from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name','user_email','user_text']
        labels = {
            'username' : 'Name',
            'user_email' : 'Email',
            'user_text' : 'Comment'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('user_email')
        print("My Email")
        print(email)
        errors = {}
        if email == None:
            errors['user_email'] = forms.ValidationError("Email is invalid")
        elif not email.endswith('gmail.com'):
            errors['user_email'] = forms.ValidationError("Email is invalid")
        
        if errors:
            for field,error in errors.items():
                self.add_error(field,error)
        
        return cleaned_data
from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name" ,max_length = 200)
#     review_text = forms.CharField(label="Feedback" , widget = forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating" , min_value=1 , max_value=10)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        labels = {
            'username' : 'Your Name',
            'review_text' : 'Your Feedback',
            'rating' : 'Rating'
        }

        error_messages = {
            'username' : {
                'required': 'User Name is required',
                'max_length' : 'Please enter shorter Feedback'
            }
        }
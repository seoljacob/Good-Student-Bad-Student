from django import forms
from .models import MyModel


class FirstForm(forms.ModelForm):
    q1 = forms.ChoiceField(label="What age group do you belong to?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Under 21"), (2, "22-25"), (3, "Over 26")))
    q2 = forms.ChoiceField(label="Which of the following genders do you identify as?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Female"), (2, "Male"), (3, "Other")))
    q3 = forms.ChoiceField(label="If you graduated high school, what type of school did you go to? (Click 'Other' if "
                                 "you didn't attend or graduate high school)",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Private"), (2, "Public"), (3, "Other")))
    q4 = forms.ChoiceField(label="Are you involved in additional work outside of school?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Yes"), (2, "No")))
    q5 = forms.ChoiceField(label="Do you engage in activities such as arts or sports on a regular basis?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Yes"), (2, "No")))
    q6 = forms.ChoiceField(label="Are you currently in a romantic relationship?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Yes"), (2, "No")))
    q7 = forms.ChoiceField(label="What is your current living situation?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Rental home"), (2, "Dormitory"), (3, "Family home"), (4, "Other")))

    class Meta:
        model = MyModel
        fields = []


class SecondForm(forms.ModelForm):
    q8 = forms.ChoiceField(label="How often do you read non-scientific books?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Never"), (2, "Sometimes"), (3, "Often")))
    q9 = forms.ChoiceField(label="How often do you read scientific books?",
                           widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                           choices=((1, "Never"), (2, "Sometimes"), (3, "Often")))
    q10 = forms.ChoiceField(label="What kind of impact have your projects had on your overall success?",
                            widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                            choices=((1, "Positive"), (2, "Negative"), (3, "Neutral")))
    q11 = forms.ChoiceField(label="How often do you attend your classes?",
                            widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                            choices=((1, "Always"), (2, "Sometimes"), (3, "Never")))
    q12 = forms.ChoiceField(label="Do you take notes during class?",
                            widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                            choices=((1, "Never"), (2, "Sometimes"), (3, "Always")))
    q13 = forms.ChoiceField(label="What was your CGPA in the previous term?",
                            widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                            choices=((1, "Less than 2.0"), (2, "2.0-2.49"), (3, "2.5-2.99"), (4, "3-3.49")
                                     , (5, "above 3.49")))
    q14 = forms.ChoiceField(label="What do you expect your CGPA to be when you graduate?",
                            widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                            choices=((1, "Less than 2.0"), (2, "2.0-2.49"), (3, "2.5-2.99"), (4, "3-3.49")
                                     , (5, "above 3.49")))

    class Meta:
        model = MyModel
        fields = []

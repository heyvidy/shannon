from django import forms

Labels = (
    ('dc', 'Digital Communications'),
    ('mec', 'Micro Electronic Circuits'),
    ('sc', 'Sat Comm'),
    ('mp', 'Micro Processors'),
    ('ap', 'Antenna & Propogation'),
    ('os', 'Operating Systems'),
)
class DocumentForm(forms.Form):
    name = forms.CharField()
    label = forms.ChoiceField(choices=Labels)
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
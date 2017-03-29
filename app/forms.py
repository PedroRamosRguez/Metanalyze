from django import forms

class AlgorithmForm(forms.Form):
    CHOICES_dataOutput = (
        ('table', 'Table'),
        ('plot', 'Plot'),
        ('table-plot', 'Table and Plot'),
    )
    CHOICES_bound = (
        ('minimum', 'Minimum'),
        ('average', 'Average'),
        ('maximum', 'Maximum'),
    )
    nAlgorithms = forms.CharField(widget = forms.TextInput(attrs = {'name':'nAlgorithms','id': 'nAlgorithms',
        'placeholder': 'Insert the number of algorithms', 'oninput': 'checkAlgorithm()'}),required=False)
              
    idAlgorithm = forms.CharField(widget = forms.TextInput(attrs={'id':'idAlgorithm',
        'placeholder':'Introduce the identificator for this algorithm','oninput':'configureAlgorithm()'}),required=False)
    
    file = forms.FileField(widget=forms.FileInput(attrs = {'id':'file'}),required=False)
    
    fileName = forms.CharField(widget=forms.TextInput(attrs = {'class':'file-path validate',
        'placeholder':'Select file to run the test'}),required=False)

    nVariablesAlgorithm = forms.CharField(widget=forms.TextInput(attrs = {'id':'nVariablesAlgorithm',
        'name':'nVariablesAlgorithm','placeholder':'Introduce the number of variables for this algorithm'}),required=False)

    dataOutput = forms.ChoiceField(widget=forms.RadioSelect(attrs = {'class': 'with-gap dataOutput'}),choices=CHOICES_dataOutput, required=True)
    
    nObjetives = forms.CharField(widget = forms.TextInput(attrs= {'id': 'nObjetives','name': 'nObjetives',
        'placeholder': 'Insert the number of objetives'}),required=True)

    nExecutions = forms.CharField(widget = forms.TextInput(attrs= {'id': 'nExecutions','name': 'nExecutions',
        'placeholder': 'Insert the number of executions done'}),required=True)

    step = forms.CharField(widget = forms.TextInput(attrs= {'id': 'step','name': 'step',
        'placeholder': 'Insert the number of steps'}),required=True)

    stopCondition = forms.CharField(widget = forms.TextInput(attrs= {'id': 'stopCondition','name': 'stopCondition',
        'placeholder': 'Insert the stop condition'}),required=True)

    bound = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=CHOICES_bound,required=True)
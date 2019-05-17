from django import forms

class AlgorithmForm(forms.Form):
    CHOICES_dataOutput = (
        ('table', 'Table'),
        ('plot', 'Plot'),
        ('table-plot', 'Table and Plot'),
    )
    CHOICES_statisticTest =(
        ('yes','Yes'),
        ('no','No')
    )
    CHOICES_evaluations =(
        ('number_of_evaluation','Number of evaluation'),
        ('time','Time')
    )
    CHOICES_metrics = (
        ('hypervolume','Hypervolume'),
    )
    CHOICES_bounds = (
        ('minimum','Minimum'),
        ('average','Average'),
        ('maximum','Maximum'),
    )

    bounds = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = CHOICES_bounds, required = True)

    data_output = forms.ChoiceField(widget = forms.RadioSelect(attrs = {'class': 'with-gap dataOutput'}),choices = CHOICES_dataOutput, required = True)

    evaluation = forms.ChoiceField(widget = forms.RadioSelect(attrs = {'class': 'with-gap dataOutput'}),choices = CHOICES_evaluations,required = False)

    file_input = forms.FileField(widget = forms.FileInput(attrs = {'id':'file'}),required = False)
    
    file_name = forms.CharField(widget = forms.TextInput(attrs = {'class':'file-path validate',
        'placeholder':'Select file to run the test'}),required = False)

    id_algorithm = forms.CharField(widget = forms.TextInput(attrs = {'id':'idAlgorithm',
        'placeholder':'Introduce the identificator for this algorithm','oninput':'configureAlgorithm()'}),required = False)

    metrics = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = CHOICES_metrics, required = True)

    n_algorithms = forms.CharField(widget = forms.TextInput(attrs = {'name':'nAlgorithms','id': 'nAlgorithms',
        'placeholder': 'Insert the number of algorithms', 'oninput': 'checkAlgorithm()'}),required = True)
    
    n_executions = forms.CharField(widget = forms.TextInput(attrs = {'id': 'nExecutions','name': 'nExecutions',
        'placeholder': 'Insert the number of executions done'}),required = True)

    n_objectives = forms.CharField(widget = forms.TextInput(attrs = {'id': 'nObjectives','name': 'nObjetives',
        'placeholder': 'Insert the number of objectives'}),required = True)
    
    n_variables_algorithm = forms.CharField(widget = forms.TextInput(attrs = {'id':'nVariablesAlgorithm',
        'name':'nVariablesAlgorithm','placeholder':'Introduce the number of variables for this algorithm'}),required = False)

    statistic_test = forms.ChoiceField(widget = forms.RadioSelect(attrs = {'class': 'with-gap dataOutput'}),choices = CHOICES_statisticTest, required = True)

    step = forms.CharField(widget = forms.TextInput(attrs = {'id': 'step','name': 'step',
        'placeholder': 'Insert the number of steps'}),required = True)

    stop_condition = forms.CharField(widget = forms.TextInput(attrs= {'id': 'stopCondition','name': 'stopCondition',
        'placeholder': 'Insert the stop condition'}),required=True)

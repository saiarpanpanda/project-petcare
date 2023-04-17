from django import forms
from .models import BloodReport
from .models import DogPatient

class DogPatientForm(forms.ModelForm):
    registration_no = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    class Meta:
        model = DogPatient
        fields = [
            'registration_no',
            'name',
            'breed',
            'species',
            'age',
            'weight',
            'gender',
            'owner_name',
            'owner_phone'
        ]
        




class BloodReportForm(forms.ModelForm):
    
    blood_type = forms.ChoiceField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    Thyroid = forms.ChoiceField(choices=[('T3', 'T3'), ('T4','T4'), ('T5','T5')])
    LFT = forms.ChoiceField(choices=[('AST','AST'),('ALT','ALT'),('ALP','ALP'),('BLT','BLT'),('BID','BID'),('TPRO','TPRO'),('ALB','ALB'),('GLB','GLB')])
    Lipid_Profile = forms.ChoiceField(choices=[('HDL','HDL'),('LDL','LDL'),('TRIG','TRIG'),('VLDL','VLDL'),('T,CHOL','T.CHOL'),('LDH','LDH')])
    
    class Meta:
        model = BloodReport
        fields = [ 'patient_name',
                   'blood_type', 
                   'hemoglobin_level',
                   'Thyroid',
                   'LFT',
                   'Lipid_Profile',
                   'KFT',
                   'urine_cultune',
                   'Anbiotic_Sensitivity_Test',
                   'Glucose',
                   'Skin_CULTURE',
                   'STOOL_TEST',
                   'PHYSICAL_EXAMINATION_OF_URINE',
                   'Pancreatic_Enzyymes',
                   'Inflammation',
                   'Complete_Blood_Count',
                   'Blood_Protozoa',
        ]
        
    
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
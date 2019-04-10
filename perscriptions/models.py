from django.db import models
from django.db.models import Sum
from django.forms import ModelForm

# Create your models here.
class Drug(models.Model) :
    DrugName = models.TextField()
    isOpioid = models.BooleanField()

    def get_top_prescriptions(self):
        prescriptions = Prescriptions.objects.filter(Drug=self).order_by('-QuanityPerscribed')[:10]
        return prescriptions
    def get_average_perscribed(self):
        prescriptions = Prescriptions.objects.filter(Drug=self)

        total_perscribed = prescriptions.aggregate(Sum('QuanityPerscribed'))['QuanityPerscribed__sum']
        return round(total_perscribed / prescriptions.count(), 2)




class Prescriber(models.Model) :
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female)'))
    DoctorID = models.IntegerField(blank=False)
    Fname = models.CharField(blank=True, max_length=100)
    Lname = models.CharField(blank=True, max_length=100)
    Gender = models.CharField(db_index =True, choices=GENDER_CHOICES, default='M', max_length=100)
    State = models.CharField(blank=True, max_length=100)
    Credentials = models.CharField(blank=True, max_length=100)
    Specialty = models.CharField(blank=True, max_length=100)
    OpioidPrescriber = models.BooleanField()
    TotalPrescriptions = models.IntegerField(blank=True, default=0)

    def get_drugs_perscribed(self):
        prescriptions = Prescriptions.objects.filter(Prescriber=self).order_by('-QuanityPerscribed')
        return prescriptions
    class Meta:
        permissions = (
            ("can_crud", "Has Ability to Create Update and Delete"),
        )



class PrescriberForm(ModelForm):
    class Meta:
        model = Prescriber
        fields = ['DoctorID', 'OpioidPrescriber', 'Fname', 'Lname', 'Gender', 'State', 'Credentials', 'Specialty']
        labels = {
            "Fname": "First Name",
            "Lname": "Last Name",
            "OpioidPrescriber": "Do they perscribe Opioids?"
        }
    def __init__(self, *args, **kwargs):
        super(PrescriberForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs\
                .update({
                    'class': 'form-control'
                })

class Prescriptions(models.Model) :
    Prescriber =  models.ForeignKey(Prescriber, on_delete=models.CASCADE)
    Drug =  models.ForeignKey(Drug, on_delete=models.CASCADE)
    QuanityPerscribed = models.IntegerField()

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescriptions
        fields = ['QuanityPerscribed']
        labels = {
            "QuanityPerscribed": "Quantity Perscribed"
        }
    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs\
                .update({
                    'class': 'form-control',
                })

class PrescriptionAddForm(ModelForm):
    class Meta:
        model = Prescriptions
        fields = ['Drug', 'QuanityPerscribed']
        labels = {
            "QuanityPerscribed": "Quantity Perscribed"
        }

    # def clean_Drug(self):
    #     data = self.cleaned_data['Drug']
    #     print('YESSIR')
    #     return data

    def __init__(self, *args, **kwargs):
        super(PrescriptionAddForm, self).__init__(*args, **kwargs)
        self.fields['Drug'].label_from_instance = lambda obj: "%s" % obj.DrugName.capitalize()
        for field in self.fields:
            self.fields[field].widget.attrs\
                .update({
                    'class': 'form-control',
                })

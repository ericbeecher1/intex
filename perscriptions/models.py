from django.db import models
from django.db.models import Sum
from django.forms import ModelForm
import requests
import json

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

    def get_similar_drugs(self):
        url = "https://ussouthcentral.services.azureml.net/workspaces/ae4a498eb76b4f1784a29fda49093be0/services/ffaca78d20174bc7b1583bdd2deb92fe/execute"

        querystring = {"api-version":"2.0"}

        payload = "{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"Drug\"\n      ],\n      \"Values\": [\n        [\n          \"value\"\n        ]\n      ]\n    }\n  }\n}"
        headers = {
            'Authorization': "Bearer o05HlLUn/JRKL0KJ3CbRguzX7+5yO3+mjE0d4/MY76xorX+jayTT9JeXDbEMxoCMtEMvNN36d3wHwpDCcrABqA==",
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        name_list = json.loads(response.text)['Results']['output1']['value']['Values'][0]
        similar_drugs = Drug.objects.filter(DrugName__in=name_list)
        return similar_drugs




class Prescriber(models.Model) :
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female)'))
    STATE_CHOICES = (("AL", "Alabama"),("AK", "Alaska"),("AS", "American Samoa"),("AZ", "Arizona"),("AR", "Arkansas"),("CA", "California"),("CO", "Colorado"),("CT", "Connecticut"),("DE", "Delaware"),("DC", "District Of Columbia"),("FM", "Federated States Of Micronesia"),("FL", "Florida"),("GA", "Georgia"),("GU", "Guam"),("HI", "Hawaii"),("ID", "Idaho"),("IL", "Illinois"),("IN", "Indiana"),("IA", "Iowa"),("KS", "Kansas"),("KY", "Kentucky"),("LA", "Louisiana"),("ME", "Maine"),("MH", "Marshall Islands"),("MD", "Maryland"),("MA", "Massachusetts"),("MI", "Michigan"),("MN", "Minnesota"),("MS", "Mississippi"),("MO", "Missouri"),("MT", "Montana"),("NE", "Nebraska"),("NV", "Nevada"),("NH", "New Hampshire"),("NJ", "New Jersey"),("NM", "New Mexico"),("NY", "New York"),("NC", "North Carolina"),("ND", "North Dakota"),("MP", "Northern Mariana Islands"),("OH", "Ohio"),("OK", "Oklahoma"),("OR", "Oregon"),("PW", "Palau"),("PA", "Pennsylvania"),("PR", "Puerto Rico"),("RI", "Rhode Island"),("SC", "South Carolina"),("SD", "South Dakota"),("TN", "Tennessee"),("TX", "Texas"),("UT", "Utah"),("VT", "Vermont"),("VI", "Virgin Islands"),("VA", "Virginia"),("WA", "Washington"),("WV", "West Virginia"),("WI", "Wisconsin"),("WY", "Wyoming"))

    DoctorID = models.IntegerField(blank=False)
    Fname = models.CharField(blank=True, max_length=100)
    Lname = models.CharField(blank=True, max_length=100)
    Gender = models.CharField(db_index =True, choices=GENDER_CHOICES, default='M', max_length=100)
    State = models.CharField(db_index =True, choices=STATE_CHOICES, max_length=100)
    Credentials = models.CharField(blank=True, max_length=100)
    Specialty = models.CharField(blank=True, max_length=100)
    OpioidPrescriber = models.BooleanField()
    TotalPrescriptions = models.IntegerField(blank=True, default=0)

    def get_drugs_perscribed(self):
        prescriptions = Prescriptions.objects.filter(Prescriber=self).order_by('-QuanityPerscribed')
        return prescriptions

    def get_high_risk(self):
        similar_prescribers = self.get_similar_prescribers()
        high_risk = False
        if self.get_percentage_opioids() > 0:
            high_risk = True
            high_percent = self.get_percentage_opioids()
            for similar_prescriber in similar_prescribers:
                if similar_prescriber.get_percentage_opioids() > high_percent:
                    high_risk = False
                    high_percent = similar_prescriber.get_percentage_opioids()

        return high_risk


    def get_percentage_opioids(self):
        prescriptions = self.get_drugs_perscribed()
        opioid_total = 0
        for prescription in prescriptions:
            if prescription.Drug.isOpioid:
                opioid_total = opioid_total + prescription.QuanityPerscribed

        return opioid_total/self.TotalPrescriptions


    def get_similar_prescribers(self):
        url = "https://ussouthcentral.services.azureml.net/workspaces/ae4a498eb76b4f1784a29fda49093be0/services/f3ff562a3a1146419167d5eb85ee7842/execute"

        querystring = {"api-version":"2.0"}

        payload = "{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"DoctorID\"\n      ],\n      \"Values\": [\n        [\n          \""+str(self.DoctorID)+"\"\n        ]\n      ]\n    }\n  }\n}"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer +0z0SepdQKBMbeUzRzKw0XYv79TnSJhGbqQPiexyxAUIxozRo9xAFlAjfqZ1tBeTf8Hz4S1BDJSVtkK5oBJ5Wg==",
            'cache-control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        id_list = json.loads(response.text)['Results']['output1']['value']['Values'][0]
        similar_prescribers = Prescriber.objects.filter(DoctorID__in=id_list)
        return similar_prescribers
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

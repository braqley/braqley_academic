from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
# from static import toy_email_list

import csv

authorized_emails = []
with open('static/toy_email_list.csv') as f:
    course_list = csv.DictReader(f)
    for row in course_list:
        authorized_emails.append(row["Email"])


class RestrictEmailAdapter(DefaultAccountAdapter):


    def clean_email(self,email):
        RestrictedList = authorized_emails
        if email not in RestrictedList:
            raise ValidationError('You are restricted from registering. Please contact admin.')
        return email
from django.db import models

# Create your models here.
class CardInfo(models.Model):
    Christmas_Day = 'CHD'
    Canada_Day = 'CAD'
    Thanksgiving = 'THG'
    Valentines_Day = 'VTD'
    New_Year = 'NYD'
    Other = 'OTH'

    holiday_choices = (
      (Christmas_Day, 'Christmas Day'),
      (New_Year, 'New Year'),
      (Valentines_Day, 'Valentines Day'),
      (Canada_Day, 'Canada Day'),
      (Thanksgiving, 'Thanksgiving'),
      (Other, 'Other'),
    )

    Holiday_Choice = models.CharField(max_length=3, choices=holiday_choices, default='Christmas Day')
    Recipient_Name = models.CharField(max_length=40)
    Recipient_Location = models.CharField(max_length=40)
    #Short_Message = models.TextField(max_length=200)
    Your_Name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return ('Card ' + str(self.id))
    '''
    def __str__(self):
        return str(self.id)

    
    def save(self, *args, **kwargs):
        #generate_img = 
        return None
    '''

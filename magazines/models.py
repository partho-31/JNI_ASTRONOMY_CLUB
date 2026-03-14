import uuid
from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator,MaxValueValidator
from cloudinary.models import CloudinaryField



class Magazine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length= 200)
    sub_title = models.TextField(blank=True, null=True)
    cover_img = CloudinaryField('image',default='default_for_cover_r4fftg',blank=True,null=True)
    discription = models.TextField()
    outcomes = models.TextField()
    
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read_time = models.CharField(max_length= 100)
    status = models.CharField(max_length=10, default= "Pending")


    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name= 'magazines')

    def __str__(self):
        return self.title



class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length= 200)
    sub_title = models.TextField(blank=True, null=True)
    cover_img = CloudinaryField('image',default='default_for_cover_r4fftg',blank=True,null=True)
    discription = models.TextField()

    heading_01 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_01 = models.TextField(blank=True, null=True)
    heading_02 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_02 = models.TextField(blank=True, null=True)
    heading_03 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_03 = models.TextField(blank=True, null=True)
    heading_04 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_04 = models.TextField(blank=True, null=True)
    heading_05 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_05 = models.TextField(blank=True, null=True)
    heading_06 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_06 = models.TextField(blank=True, null=True)
    heading_07 = models.CharField(max_length= 200, blank=True, null=True)
    paragraph_07 = models.TextField(blank=True, null=True)   

    quoter = models.CharField(max_length= 200, blank=True, null=True)
    quotes = models.TextField(blank=True, null=True)

    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read_time = models.CharField(max_length= 100)
    status = models.CharField(max_length=10, default= "Pending")


    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name= 'articles')
    magazine = models.ForeignKey(Magazine,on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title



class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.CharField(max_length=200, blank=True, null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,null= True, blank=True, related_name='reviews')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.comment} - {self.user}"
    


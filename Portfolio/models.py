from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=128)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    technology_used = models.CharField(max_length=500)
    framework_used = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=500)
    github_link = models.URLField(blank=True, null=True)
    web_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == "image":
                field.upload_to = f"images/Projects/"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Social_Site_Connection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(null=True, blank=True)
    facebook = models.URLField(default="")
    instagram = models.URLField(null=True, blank=True)
    stack_overflow = models.URLField(null=True, blank=True)
    hackerrank = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Social Site Connections"

    def __str__(self):
        return self.user.username


expiry_date_choices = (
    ("1", "none"),
)


class Achievment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=128)
    enrolled_in = models.DateField()
    finished_in = models.DateField()
    position_holding = models.CharField(max_length=100, null=True, blank=True)
    venue = models.TextField(max_length=500)
    expiry_date = models.CharField(max_length=200, choices=expiry_date_choices)
    certificate = models.FileField(upload_to="Acievments/")
    certificate_url = models.URLField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Pics(models.Model):
    OptionalPic = models.ImageField(upload_to="images/", blank=True, null=True)
    alternative_text = models.CharField(max_length=40, default="")

    class Meta:
        verbose_name_plural = "Pics"

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == "OptionalPic":
                field.upload_to = f"images/OptionalPic/"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.alternative_text


class MyDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tell_about_me_your_self = models.TextField(max_length=500)
    profile_pic = models.ImageField(default="", upload_to="media/images/")
    alternative_text = models.CharField(max_length=40, default="")
    optional_pic = models.ForeignKey(Pics, on_delete=models.CASCADE, null=True, blank=True)
    social_site_connection_details = models.ForeignKey(Social_Site_Connection, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="Resume/", null=True, blank=True)
    projects_detail = models.ManyToManyField(Project, related_name="projects")
    achievment_details = models.ForeignKey(Achievment, on_delete=models.CASCADE)

    # created_date=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == "profile_pic":
                field.upload_to = f"images/{self.user.username}/ProfilePic/"
            if field.name == "resume":
                field.upload_to = f"Resume/{self.user.username}/"
        super().save(*args, **kwargs)

    def __str__(self):
        return ("{} " + "{}").format(self.user.first_name, self.user.last_name)


class Subscribe(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    query = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.email


class ContactBackend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gmail = models.EmailField(default="")
    password = models.CharField(max_length=200, verbose_name="App Password (gmail)")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Us Backend"

    def __str__(self):
        return self.user.username

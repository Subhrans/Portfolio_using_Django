from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Under_Graduation(models.Model):
    Institute_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=120)
    year_of_graduated = models.DateField()


class Post_Graduation(models.Model):
    Institute_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=120)
    year_of_graduated = models.DateField()


class Secondary_Examination(models.Model):
    name = models.CharField(max_length=128)
    year_of_pass_out = models.DateField()


class Higher_Secondary_Examination(models.Model):
    name = models.CharField(max_length=128)
    year_of_pass_out = models.DateField()


class Qualification(models.Model):
    secondary_examination_details = models.ForeignKey(Secondary_Examination, on_delete=models.CASCADE)

    higher_secondary_examination_details = models.ForeignKey(Higher_Secondary_Examination, on_delete=models.CASCADE)

    under_graduation_details = models.ForeignKey(Under_Graduation, on_delete=models.CASCADE)

    post_graduation_details = models.ForeignKey(Post_Graduation, on_delete=models.CASCADE)


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
    email = models.EmailField()
    github = models.URLField()
    hackerrank = models.URLField()
    linkedIn = models.URLField()


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
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
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
    last_name =models.CharField(max_length=128)
    email = models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.email
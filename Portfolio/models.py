from django.db import models


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
    technology_used = models.CharField(max_length=500)
    framework_used = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=500)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Social_Site_Connection(models.Model):
    email = models.EmailField()
    github = models.URLField()
    hackerrank = models.URLField()
    linkedIn = models.URLField()


expiry_date_choices = (
    ("1", "none"),
)


class Achievment(models.Model):
    event_name = models.CharField(max_length=128)
    enrolled_in = models.DateField()
    finished_in = models.DateField()
    position_holding = models.CharField(max_length=100, null=True, blank=True)
    venue = models.TextField(max_length=500)
    expiry_date = models.CharField(max_length=200, choices=expiry_date_choices)
    certificate = models.FileField(upload_to="Acievments/")
    certificate_url = models.URLField(null=True, blank=True)


class Pics(models.Model):
    OptionalPic = models.ImageField(upload_to="media/images/", blank=True, null=True)

    def __str__(self):
        return self.OptionalPic


class MyDetail(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    tell_about_me_your_self = models.TextField(max_length=500)
    profile_pic = models.ImageField(default="", upload_to="media/images/")
    optional_pic = models.ForeignKey(Pics, on_delete=models.CASCADE, null=True, blank=True)
    social_site_connection_details = models.ForeignKey(Social_Site_Connection, on_delete=models.CASCADE)

    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    projects_detail = models.ForeignKey(Project, on_delete=models.CASCADE)
    achievment_details = models.ForeignKey(Achievment, on_delete=models.CASCADE)

    def __str__(self):
        return ("{} " + "{}").format(self.first_name, self.last_name)


class Subscribe(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.name

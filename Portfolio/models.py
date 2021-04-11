from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from allauth.account.signals import email_confirmed


def email_confirmed_receiver(request, email_address, **kwargs):
    pass


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, editable=False)
    language_used = models.ForeignKey(Language, on_delete=models.CASCADE, default="", null=True, unique=False)
    framework_used = models.CharField(max_length=500, null=True, blank=True)
    technologies_used = models.TextField(help_text="like Databases,Front-End,API's etc", null=True,
                                         blank=True)
    description = models.TextField(max_length=500)
    github_link = models.URLField(blank=True, null=True)
    web_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(allow_unicode=True, default="", editable=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == "image":
                field.upload_to = f"images/Projects/"
        self.slug = slugify(self.name + self.language_used.name + str(self.created_date))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Social_Site_Connection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    event_name = models.CharField(max_length=128)
    enrolled_in = models.DateField()
    finished_in = models.DateField()
    position_holding = models.CharField(max_length=100, null=True, blank=True)
    venue = models.TextField(max_length=500)
    expiry_date = models.CharField(max_length=200, choices=expiry_date_choices)
    certificate = models.FileField(upload_to="Acievments/")
    certificate_url = models.URLField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


# class Pics(models.Model):
#     OptionalPic = models.ImageField(upload_to="images/", blank=True, null=True)
#     alternative_text = models.CharField(max_length=40, default="")
#
#     class Meta:
#         verbose_name_plural = "Pics"
#
#     def save(self, *args, **kwargs):
#         for field in self._meta.fields:
#             if field.name == "OptionalPic":
#                 field.upload_to = f"images/OptionalPic/"
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.alternative_text


class MyDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    tell_about_me_your_self = models.TextField(max_length=500)
    profile_pic = models.ImageField(default="", upload_to="media/images/")
    profile_alternative_text = models.CharField(max_length=40, default="")
    optional_pic = models.ImageField(upload_to="images/", blank=True, null=True)
    optional_alternative_text = models.CharField(max_length=40, default="about-my-image", editable=False)
    social_site_connection_details = models.ForeignKey(Social_Site_Connection, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="Resume/", null=True, blank=True)
    projects_detail = models.ManyToManyField(Project, related_name="projects")
    achievment_details = models.ForeignKey(Achievment, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=16, default="",
                                      help_text="(Hint) add spaces for format the number as mine")
    url = models.URLField(default="", editable=False)
    slug = models.SlugField(allow_unicode=True, editable=False, default="")

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if field.name == "profile_pic":
                field.upload_to = f"images/{self.user.username}/ProfilePic/"
            if field.name == "OptionalPic":
                field.upload_to = f"images/{self.user.username}/OptionalPic/"
            if field.name == "resume":
                field.upload_to = f"Resume/{self.user.username}/"

        self.slug = slugify(self.user)
        self.url = self.slug
        super().save(*args, **kwargs)

    def __str__(self):
        return ("{} " + "{}").format(self.user.first_name, self.user.last_name)


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, editable=False)
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    query = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.email


class MailBackend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gmail = models.EmailField(default="")
    password = models.CharField(max_length=200, verbose_name="App Password (gmail)",
                                help_text="(Note): If You Dont't Have gmail App Password, Create that first else sending email is not being processed")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Mail Backend"

    def __str__(self):
        return self.user.username

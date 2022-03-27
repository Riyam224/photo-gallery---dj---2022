
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Photo(models.Model):
    name = models.CharField(_("name"), max_length=250)
    image = models.ImageField(_("image"), upload_to='photo/')
    category = models.ForeignKey("Category",  related_name="photo_category", verbose_name=_("category"), on_delete=models.CASCADE)
    desc = models.TextField(_("desc"))


    

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("photo", kwargs={"id": self.id})



class Category(models.Model):
    name = models.CharField(_("name"), max_length=250)
    user = models.ForeignKey(User, related_name="category_user", verbose_name=_("user"), on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

   
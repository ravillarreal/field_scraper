from django.db import models


# Create your models here.


class Tag(models.Model):
    """Tag model to store element tags"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Refer(models.Model):
    """Intern purpose for merging similar fields"""

    name = models.CharField(max_length=255)
    help = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.name = self.name.lower().replace(" ", "_")
        super(Refer, self).save(*args, **kwargs)


class Element(models.Model):
    """Element model that contains html element information"""

    text = models.CharField(max_length=255)
    parent = models.ForeignKey("Element", on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    refers = models.ForeignKey(Refer, on_delete=models.CASCADE)


class Attribute(models.Model):
    """Element attributes"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Value(models.Model):
    """Model for storing element's attributes value"""

    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('element', 'attribute')

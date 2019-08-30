from django.db import models


class Configuration(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=100)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=100)
    config = models.ForeignKey(Configuration, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ViewType(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=100)

    def __str__(self):
        return self.name


class View(models.Model):
    name = models.CharField(verbose_name=u'Название в меню', max_length=100)
    name_view = models.CharField(verbose_name=u'Название в классе', max_length=100, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    type = models.ForeignKey(ViewType, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name=u'Описание', max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=100)
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=u'Описание', max_length=2000, blank=True, null=True)
    decision = models.TextField(verbose_name=u'Решение', max_length=2000, blank=True, null=True)
    attachment = models.ImageField(upload_to='error/attachment', blank=True, verbose_name='вложение')

    def __str__(self):
        return self.title
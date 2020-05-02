from django.db import models


# Категория деятельности
class ActivityCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название")
    slug = models.SlugField(db_index=True)
    # prepopulated_fields = {"slug": ("name",)}

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сфера деятельности компании'
        verbose_name_plural = 'Сферы деятельности компании'


# Карта/Визитка пользователя
class Card(models.Model):
    # user = models.OneToOneField()
    image = models.ImageField(upload_to='avatar', verbose_name="Фотография/Логотип")
    first_name = models.CharField(max_length=40, verbose_name="Имя", help_text='Ваше имя')
    second_name = models.CharField(max_length=40, verbose_name="Фамилия", blank=True, null=True, default=None)
    last_name = models.CharField(max_length=40, verbose_name="Отчество", blank=True, null=True, default=None)
    company_name = models.CharField(max_length=40, verbose_name="Название компании/ИП")
    company_activity = models.ForeignKey(ActivityCategory, on_delete=models.SET_NULL,
                                         verbose_name='Деятельность компании')
    position_in_company = models.CharField(max_length=200, verbose_name='Должность')
    site = models.URLField(verbose_name='Сайт')
    description = models.TextField(verbose_name='Описание')

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Визитка'
        verbose_name_plural = 'Визитки'


# Телефон
class Telephone(models.Model):
    TELEPHONE_TYPES = [
        ('wr', 'Рабочий'),
        ('mob', 'Мобильный'),
        ('home', 'Домашний'),
        ('home', 'Домашний'),
    ]
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    telephone_type = models.CharField(max_length=4, choices=TELEPHONE_TYPES)
    telephone = models.CharField(max_length=13)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.card}'

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


# E-mails
class Email(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    email = models.EmailField()

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.card}'

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'


# Социальные сети
class SocialNetwork(models.Model):
    name = models.CharField(max_length=25)
    url = models.URLField()
    logo = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'


# Социальные сети пользователя
class CardSocialNetwork(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    social_network = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.card}'

    class Meta:
        verbose_name = 'Социальная сеть пользователя'
        verbose_name_plural = 'Социальные сети пользователя'


# Адреса
class Address(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.TextField()

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.card}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


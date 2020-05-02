from django.contrib import admin
from . import models


# Категория деятельности
@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'slug',
		'is_active',
	]

	list_filter = [
		'name',
		'slug',
		'is_active',
	]

	list_editable = [
		'name',
		'slug',
		'is_active',
	]
	search_fields = [
		'name',
		'slug',
	]
	prepopulated_fields = {"slug": ("name",)}


# Формы для паралельного создания email/телефонов
class TelephoneInline(admin.TabularInline):
	model = models.Telephone
	extra = 0  # колличество авт созд полей


class EmailInline(admin.TabularInline):
	model = models.Email
	extra = 0  # колличество авт созд полей


class CardSocialNetworkInline(admin.TabularInline):
	model = models.CardSocialNetwork
	extra = 0  # колличество авт созд полей


class AddressInline(admin.TabularInline):
	model = models.Address
	extra = 0  # колличество авт созд полей


# Карта/Визитка пользователя
@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
	list_display = [
		'first_name',
		'second_name',
		'company_name',
		'company_activity',
		'is_active',
	]

	list_filter = [
		'first_name',
		'second_name',
		'company_name',
		'company_activity',
		'is_active',
	]

	list_editable = [
		'is_active',
	]
	search_fields = [
		'first_name',
		'second_name',
		'company_name',
		'company_activity',
	]
	# подключение вложенной модели
	inlines = [TelephoneInline, EmailInline, CardSocialNetworkInline, AddressInline, ]


# Телефон
@admin.register(models.Telephone)
class TelephoneAdmin(admin.ModelAdmin):
	list_display = [
		'card',
		'telephone_type',
		'telephone',
		'is_active',
	]

	list_filter = [
		'card',
		'telephone_type',
		'telephone',
		'is_active',
	]

	list_editable = [
		'is_active',
	]
	search_fields = [
		'card',
		'telephone_type',
		'telephone',
		'is_active',
	]


# E-mails
@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = [
		'card',
		'email',
		'is_active',
	]

	list_filter = [
		'card',
		'email',
		'is_active',
	]

	list_editable = [
		'email',
		'is_active',
	]
	search_fields = [
		'card',
		'email',
		'is_active',
	]


# Социальные сети
@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'url',
		'is_active',
	]

	list_filter = [
		'name',
		'url',
		'is_active',
	]

	list_editable = [
		'name',
		'url',
		'is_active',
	]
	search_fields = [
		'name',
		'url',
		'is_active',
	]


# Социальные сети пользователя
@admin.register(models.CardSocialNetwork)
class CardSocialNetworkAdmin(admin.ModelAdmin):
	list_display = [
		'card',
		'social_network',
		'nickname',
		'is_active',
	]

	list_filter = [
		'card',
		'social_network',
		'nickname',
		'is_active',
	]

	list_editable = [
		'nickname',
		'is_active',
	]
	search_fields = [
		'card',
		'social_network',
		'nickname',
		'is_active',
	]


# Адреса
@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = [
		'card',
		'country',
		'region',
		'city',
		'address',
		'is_active',
	]

	list_filter = [
		'card',
		'country',
		'region',
		'city',
		'address',
		'is_active',
	]

	list_editable = [
		'card',
		'country',
		'region',
		'city',
		'address',
		'is_active',
	]
	search_fields = [
		'card',
		'country',
		'region',
		'city',
		'address',
		'is_active',
	]







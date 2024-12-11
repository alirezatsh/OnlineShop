from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AboutUs , Installment
from django.core.mail import send_mail
from django.conf import settings  

@receiver(post_save, sender=AboutUs)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        subject = 'پیام جدید در فرم تماس با ما'
        message = (
            f'یک پیام جدید ثبت شده:\n\n'
            f'نام: {instance.name} {instance.lastName}\n'
            f'شماره تلفن: {instance.phoneNumber}\n'
            f'پیام: {instance.comment}\n'
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  
            [settings.EMAIL_HOST_USER],  
            fail_silently=False,
        )



@receiver(post_save, sender=Installment)
def notify_installment(sender, instance, created, **kwargs):
    if created:
        subject = 'قسط جدید ثبت شد'
        message = (
            f'یک قسط جدید ثبت شده:\n\n'
            f'نام: {instance.name} {instance.lastName}\n'
            f'شماره تلفن: {instance.phoneNumber}\n'
            f'نام محصول: {instance.productName}\n'
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  
            [settings.EMAIL_HOST_USER],  
            fail_silently=False,
        )

from django.db import models


class LogoOrder(models.Model):
    full_name = models.CharField("Фамилия Имя", max_length=200)
    contact = models.TextField("Контактный телефон или Телеграмм")
    description = models.TextField("Какой логотип желаете заказать?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ от {self.full_name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
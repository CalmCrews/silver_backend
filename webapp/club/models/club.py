import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config.models import BaseModel


class Club(BaseModel):
    class Meta:
        db_table = 'clubs'
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    name = models.CharField(
        verbose_name='모임명',
        max_length=40,
    )
    code = models.IntegerField(
        verbose_name='초대코드',
        unique=True,
        blank=True,
    )
    intro = models.CharField(
        verbose_name='모임 소개',
        max_length=60
    )
    level = models.IntegerField(
        verbose_name='모임 등급',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        default=0,
    )
    tag = models.CharField(
        verbose_name='모임 태그',
        blank=False,
    )

    achievement_count = models.IntegerField(
        verbose_name='총 달성률 횟수',
        default=0
    )

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super(Club, self).save(*args, **kwargs)

    def generate_code(self):
        while True:
            new_code = str(random.randint(0, 9999)).zfill(4)
            if not Club.objects.filter(code=new_code).exists():
                return new_code

    def __str__(self):
        return self.name

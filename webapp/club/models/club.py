from django.db import models
from config.models import BaseModel
import random

club_grade = [
    ('동산', 'First'),
    ('청계산', 'Second'),
    ('설악산', 'Third'),
    ('지리산', 'Fourth'),
    ('한라산', 'Fifth'),
]


# Create your models here.
class Club(BaseModel):
    class Meta:
        db_table = 'clubs'
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    name = models.CharField(
        verbose_name='모임명',
        unique=True,
        max_length=30,
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
    grade = models.CharField(
        verbose_name='모임 등급',
        choices=club_grade,
        default='동산',
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


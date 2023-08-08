from django.db import models

from club.models import Club
from config.models import BaseModel
from user.models import User


class UserClub(BaseModel):
    class Meta:
        db_table = 'user_club'
        verbose_name = 'UserClub'
        verbose_name_plural = 'UserClubs'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='참여자',
        related_name='club_user',
    )

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        verbose_name='참여중인 모임',
        related_name='user_club',
    )

    is_owner = models.BooleanField(
        verbose_name='모임장 여부',
        default=False,
    )


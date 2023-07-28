from django.db import models

from club.models import Club
from config.models import BaseModel


class ClubTag(BaseModel):
    class Meta:
        db_table = 'club_tag'
        verbose_name = 'ClubTag'
        verbose_name_plural = 'ClubTags'

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        unique=True,
        verbose_name='모임명',
        related_name='club_tags',
    )
    gathering = models.BooleanField(
        verbose_name='친목/또래모임',
        default=False,
    )
    daily = models.BooleanField(
        verbose_name='일상',
        default=False,
    )
    economic = models.BooleanField(
        verbose_name='경제',
        default=False,
    )
    biology = models.BooleanField(
        verbose_name='동식물',
        default=False,
    )
    culture = models.BooleanField(
        verbose_name='문화/예술',
        default=False,
    )
    study = models.BooleanField(
        verbose_name='교육/공부',
        default=False,
    )
    life = models.BooleanField(
        verbose_name='생활정보',
        default=False,
    )
    sports = models.BooleanField(
        verbose_name='스포츠',
        default=False,
    )
    religion = models.BooleanField(
        verbose_name='종교',
        default=False,
    )
    health = models.BooleanField(
        verbose_name='건강',
        default=False,
    )
    etc = models.BooleanField(
        verbose_name='기타',
        default=False,
    )

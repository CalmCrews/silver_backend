from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """ModelManager definition for User Model"""

    def _create_user(self, username, password, **kwargs):
        user = self.model(
            username=username,
            **kwargs,
        )
        user.set_password(password)
        user.save()

    def create_user(self, username, password, **kwargs):
        """일반 유저 생성 메소드"""
        self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        """슈퍼 유저(superuser) 생성 메소드"""
        kwargs.setdefault('is_superuser', True)
        self._create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'

    username = models.CharField(
        verbose_name='유저 아이디',
        unique=True,
        max_length=20,
        null=True,
        blank=True,
    )

    kakaoId = models.CharField(
        verbose_name='카카오 아이디',
        unique=True,
        max_length=255,
        null=True,
        blank=True,
    )

    naverId = models.CharField(
        verbose_name='네이버 아이디',
        unique=True,
        max_length=255,
        null=True,
        blank=True,
    )

    nickname = models.CharField(
        max_length=30,
        null=True,
    )

    profile_image = models.ImageField(
        verbose_name='프로필 이미지',
        upload_to='profile_image',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name='생성 일시',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='수정 일시',
        auto_now=True,
    )

    balance = models.PositiveIntegerField(
        verbose_name='잔액',
        default=0,
    )

    objects = UserManager()

    def __str__(self):
        if self.kakaoId:
            return f"(카카오) {self.username}"
        if self.naverId:
            return f"(네이버) {self.username}"
        return f"(일반) {self.username}"

    @property
    def is_staff(self):
        return self.is_superuser

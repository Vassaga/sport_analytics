
""" FOOTBALL MODELS """


from django.db import models

import os

class ActualManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Match.Status.NOW)


class Team(models.Model):
    """Team model"""
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded = models.PositiveIntegerField()
    coach = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    """Player model"""
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Match(models.Model):
    """Match model"""
    class Status(models.TextChoices):
        FUTURE = 'FT', 'Future'
        NOW = 'NW', 'Now'
        FINISHED = 'FN', 'Finished'

    date_time = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.FUTURE)

    objects = models.Manager()
    actual = ActualManager()

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.home_team.name} vs. {self.away_team.name}"


def rename_banner_file(instance, filename):
    base_path = 'main/'
    extension = filename.split('.')[-1]
    new_filename = f'{instance.name}.{extension}'
    return os.path.join(base_path, new_filename)


class Banner(models.Model):
    """banner for Reclama"""
    name = models.CharField(
        verbose_name='баннер',
        max_length=20,
    )
    banner_file = models.ImageField(
        verbose_name='файл баннера',
        upload_to=rename_banner_file,
        default='main/unknown.jpeg')
    
    is_active = models.BooleanField(
        verbose_name='активный',
        default=False,
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'баннер'
        verbose_name_plural = 'баннеры'

    def __str__(self) -> str:
        return self.name
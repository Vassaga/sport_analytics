from django.db import models




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
    date_time = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.home_team.name} vs. {self.away_team.name}"

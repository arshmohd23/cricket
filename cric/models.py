from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(unique=True, max_length=255)
    player_1_name = models.CharField(
        max_length=30, verbose_name='Name of Player 1')
    player_2_name = models.CharField(
        max_length=30, verbose_name='Name of Player 2')
    player_3_name = models.CharField(
        max_length=30, verbose_name='Name of Player 3')
    player_4_name = models.CharField(
        max_length=30, verbose_name='Name of Player 4')
    player_5_name = models.CharField(
        max_length=30, verbose_name='Name of Player 5')
    player_6_name = models.CharField(
        max_length=30, verbose_name='Name of Player 6')
    player_7_name = models.CharField(
        max_length=30, verbose_name='Name of Player 7')
    player_8_name = models.CharField(
        max_length=30, verbose_name='Name of Player 8')
    player_9_name = models.CharField(
        max_length=30, verbose_name='Name of Player 9')
    player_10_name = models.CharField(
        max_length=30, verbose_name='Name of Player 10')
    player_11_name = models.CharField(
        max_length=30, verbose_name='Name of Player 11')

    def __str__(self):
        return self.team_name


# class Player(models.Model):
#     name = models.CharField(max_length=30)
#     team_name = models.ForeignKey(Team, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name + ' ' + self.team_name.team_name

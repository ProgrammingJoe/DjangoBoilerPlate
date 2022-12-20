from django.db import models


class District(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name} {self.code}'


class School(models.Model):
    ELEMENTARY = 'ELEM'
    MIDDLESCHOOL = 'MIDD'
    HIGHSCHOOL = 'HIGH'
    HIGHSCHOOL_CATEGORY = [
        (ELEMENTARY, 'Elementary'),
        (MIDDLESCHOOL, 'MiddleSchool'),
        (HIGHSCHOOL, 'Highschool'),
    ]

    name = models.CharField(max_length=120)
    category = models.CharField(
        max_length=4,
        choices=HIGHSCHOOL_CATEGORY,
        default=ELEMENTARY,
    )

    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name="schools"
    )

    def __str__(self):
        return self.name

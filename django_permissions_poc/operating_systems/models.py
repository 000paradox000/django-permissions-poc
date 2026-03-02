from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        permissions = {
            (
                "viewall_operatingsystem",
                "Can view all operating systems",
            ),
        }


class Distribution(models.Model):
    name = models.CharField(max_length=100)
    operating_system = models.ForeignKey(
        OperatingSystem,
        on_delete=models.CASCADE,
        related_name="distributions",
        related_query_name="distribution",
    )

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        permissions = {
            (
                "viewall_distribution",
                "Can view all distributions",
            ),
        }

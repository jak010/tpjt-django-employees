from __future__ import annotations

from django.db import models

from django.db.models.query import QuerySet


class EmployeesExtraManager(models.Manager):

    def last_emp_no(self) -> int:
        return self.model.objects.last().emp_no


class Employees(models.Model):
    """ Employee 에 대한 Model  """

    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()

    objects: QuerySet = models.Manager()
    manager = EmployeesExtraManager()

    class Meta:
        db_table = 'employees'

    def to_dict(self):
        return {
            'emp_no': self.emp_no,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'birth_date': self.birth_date,
            'hire_date': self.hire_date
        }


class Titles(models.Model):
    """ Employee가 갖는  Titles에 대한 Model """
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'
        unique_together = (('emp_no', 'title', 'from_date'),)

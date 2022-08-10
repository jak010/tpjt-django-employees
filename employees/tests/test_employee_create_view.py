import pytest
import datetime
from django.shortcuts import reverse


@pytest.mark.django_db
def test_employee_create_view_with_success(client):
    """ employee 생성에 대한 성공 케이스 """
    # given
    url = reverse('employee:create')
    _today = datetime.date.today().strftime("%Y-%m-%d")

    # when
    response = client.post(url, data={
        'title': 'Engineer',
        'emp_no': 1,
        'last_name': 'ja',
        'first_name': 'ko',
        'hire_date': _today,
        'birth_date': _today
    })

    # then
    assert response.status_code == 200


@pytest.mark.django_db
def test_employee_create_view_with_failure_when_engineer_create(client):
    """ employee 생성에 대한 실패 케이스"""

    # given
    url = reverse('employee:create')
    _today = datetime.date.today().strftime("%Y-%m-%d")

    # when
    response = client.post(url, data={
        'title': 'engineer',
        'emp_no': 1,
        'last_name': 'ja',
        'first_name': 'ko',
        'hire_date': _today,
        'birth_date': _today
    })

    # then
    assert response.status_code == 400

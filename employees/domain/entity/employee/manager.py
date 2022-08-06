from employees.domain.entity.employee._base_employee import BaseEmployee
from employees.domain.value_object.name import EmployeeName


class Manager(BaseEmployee):
    EMPLOYEE_TITLE = 'Manager'

    def __init__(self, emp_no, emp_name: EmployeeName, birth_date, hire_date):
        super().__init__(emp_no, emp_name, birth_date, hire_date)

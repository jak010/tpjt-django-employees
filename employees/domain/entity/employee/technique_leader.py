from __future__ import annotations

from employees.domain.entity.employee._base_employee import IEmployee, EmployeeType, EmployeeProfile


class TechniqueLeader(IEmployee):
    EMPLOYEE_TITLE = EmployeeType.TECHNIQUE_LEADER.value

    def __init__(self, employee_profile: EmployeeProfile):
        super(TechniqueLeader, self).__init__(employee_profile=employee_profile)

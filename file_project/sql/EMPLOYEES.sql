-- Unlock the HR user if locked
ALTER USER hr IDENTIFIED BY hr ACCOUNT UNLOCK;

DROP TABLE hr.xx_employees;

CREATE TABLE hr.xx_employees
(
    employee_id            NUMBER( 6, 0 )
  , first_name             VARCHAR2( 20 )
  , last_name              VARCHAR2( 25 ) NOT NULL 
  , email                  VARCHAR2( 25 ) NOT NULL
  , hire_date              DATE NOT NULL
  , salary                 NUMBER( 8, 2 )
  , manager_id             NUMBER( 6, 0 )
  , department_id          NUMBER( 4, 0 )
);
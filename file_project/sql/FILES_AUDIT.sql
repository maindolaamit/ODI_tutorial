DROP TABLE hr.files_audit;

/*
category        -> Category of a file
sub Category    -> If any
path            -> File Path
name            -> File Name
status          -> Load Status of File - PICKED, PROCESSING, PROCESSED
lines_count     -> Number of lines in the file
creation_date   -> Date record got created 
processed_date  -> Date file was processed.
load_time       -> Time taken to load file data
session_id      -> ODI Session ID
*/
CREATE TABLE hr.files_audit
(
    category              VARCHAR2( 200 ) NOT NULL
  , sub_category          VARCHAR2( 200 )
  , path                  VARCHAR2( 200 ) NOT NULL
  , name                  VARCHAR2( 50 ) NOT NULL
  , status                VARCHAR2( 50 ) NOT NULL
  , lines_count           NUMBER
  , creation_date         DATE DEFAULT SYSDATE
  , pickup_date           DATE 
  , processed_date        DATE
  , load_time_seconds     NUMBER
  , session_id            NUMBER
);

INSERT INTO hr.files_audit VALUES ('EMP',NULL,'/home/oracle/odi_test/stage','Employees.csv','PICKED',26,SYSDATE,NULL,NULL,NULL,NULL);
INSERT INTO hr.files_audit VALUES ('EMP',NULL,'/home/oracle/odi_test/stage','employees_1.csv','PICKED',25,SYSDATE,NULL,NULL,NULL,NULL);
INSERT INTO hr.files_audit VALUES ('EMP',NULL,'/home/oracle/odi_test/stage','employees_2.csv','PICKED',26,SYSDATE,NULL,NULL,NULL,NULL);
INSERT INTO hr.files_audit VALUES ('EMP',NULL,'/home/oracle/odi_test/stage','employees_3.csv','PICKED',34,SYSDATE,NULL,NULL,NULL,NULL);

-- commit changes
COMMIT;

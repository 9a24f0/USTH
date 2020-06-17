-- Create database --
CREATE DATABASE Company;
USE Company;

-- Create tables --
CREATE TABLE Employee (
    Fname       VARCHAR(50),
    Minit       CHAR(1),
    Lname       VARCHAR(20),
    Ssn         INT(9),
    Bdate       DATE,
    Address     VARCHAR(50),
    Sex         TINYINT,
    Salary      FLOAT,
    Super_ssn   INT(9),
    Dno         SMALLINT,    /* Dept number */
    PRIMARY KEY (Ssn)
);

CREATE TABLE Department (
    Dname       VARCHAR(20) NOT NULL,
    Dnumber     SMALLINT,
    Mgr_ssn     INT(9),     /*  Manager SSN */
    Mgr_start_date DATE,     /* The date that the manager start working at dept*/
    PRIMARY KEY (Dnumber)
);


CREATE TABLE Dept_locations (
    Dnumber     SMALLINT,
    Dlocation   VARCHAR(50),
    PRIMARY KEY (Dnumber, Dlocation)
);

CREATE TABLE Project (
    Pname       VARCHAR(20),
    Pnumber     SMALLINT,
    Plocation   VARCHAR(20),
    Dnum        SMALLINT,
    PRIMARY KEY (Pnumber)
);

CREATE TABLE Works_on (
    Essn        INT(9),
    Pno         SMALLINT,
    Hours       TIME(0),
    PRIMARY KEY (Essn, Pno)
);

CREATE TABLE Dependent (
    Essn        INT(9),
    Dependent_name VARCHAR(20),
    Sex         TINYINT,
    Bdate       DATE,
    Relationship CHAR (20),
    PRIMARY KEY (Essn, Dependent_name)
);

-- Relations --
ALTER TABLE Employee
    ADD FOREIGN KEY (Super_ssn) REFERENCES Employee(Ssn);
ALTER TABLE Employee
    ADD FOREIGN KEY (Dno) REFERENCES Department(Dnumber);

ALTER TABLE Department
    ADD FOREIGN KEY (Mgr_ssn) REFERENCES Employee(SSn);

ALTER TABLE Dept_locations
    ADD FOREIGN KEY (Dnumber) REFERENCES Department(Dnumber);

ALTER TABLE Project
    ADD FOREIGN KEY (Dnum) REFERENCES Department(Dnumber);

ALTER TABLE Works_on
    ADD FOREIGN KEY (Pno) REFERENCES Project(Pnumber);
ALTER TABLE Works_on
    ADD FOREIGN KEY (Essn) REFERENCES Employee(Ssn);

ALTER TABLE Dependent
    ADD FOREIGN KEY (Essn) REFERENCES Employee(Ssn);
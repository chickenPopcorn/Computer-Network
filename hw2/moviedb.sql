
CREATE TABLE associations
    (  a_name VARCHAR(n),
       location VARCHAR(n),
       PRIMARY KEY (a_name) )

CREATE TABLE studios
    (  s_name VARCHAR(n),
       location VARCHAR(n),
       PRIMARY KEY (s_name) )

CREATE TABLE awards
    (  a_name VARCHAR(n),
       year integer NOT NULL,
       categ VARCHAR(n) NOT NULL,
       alias VARCHAR(n),
       PRIMARY KEY (a_name, categ, year),
       FOREIGN KEY (a_name) REFERENCES associations ON DELETE CASCADE )

CREATE TABLE crew
    (  crew_name VARCHAR(n) NOT NULL,
       pid integer,
       dob integer NOT NULL,
       PRIMARY KEY (pid) )


CREATE TABLE cast
    (  cast_name VARCHAR(n) NOT NULL,
       pid integer,
       dob integer NOT NULL
       picture bytea,
       PRIMARY KEY (pid) )

CREATE TABLE films
    (  fid integer,
       title VARCHAR(n) NOT NULL,
       genre VARCHAR(n),
       year integer NOT NULL,
       PRIMARY KEY (fid) )

CREATE TABLE act
    (  pid integer,
       fid integer,
       role VARCHAR(n),
       PRIMARY KEY (fid, pid, role),
       FOREIGN KEY (pid) REFERENCES cast on DELETE CASCADE,
       FOREIGN KEY (fid) REFERENCES films cast on DELETE CASCADE )

CREATE TABLE work_on
    (  pid integer NOT NULL,
       fid integer,
       job VARCHAR(n),
       PRIMARY KEY (fid, pid, job),
       FOREIGN KEY (pid) REFERENCES cast on DELETE CASCADE,
       FOREIGN KEY (fid) REFERENCES films on DELETE CASCADE )

CREATE TABLE prod
    (  name VARCHAR(n),
       fid integer,
       PRIMARY KEY (pid, fid),
       FOREIGN KEY (name) REFERENCES studios on DELETE CASCADE,
       FOREIGN KEY (fid) REFERENCES films on DELETE CASCADE )

CREATE TABLE win_cast
    (   a_name VARCHAR(n)
        categ VARCHAR(n),
        year integer,
        pid integer,
        fid integer,
        role VARCHAR(n),
        PRIMARY KEY (pid, a_name, categ, year, fid),
        FOREIGN KEY (a_name, categ, year) REFERENCES assocation on DELETE CASCADE,
        FOREIGN KEY (pid, fid, role) REFERENCES act on DELETE CASCADE )

CREATE TABLE win_crew
    (   a_name VARCHAR(n),
        categ VARCHAR(n),
        year integer,
        pid integer,
        fid integer,
        PRIMARY KEY (pid, a_name, categ, year, fid),
        FOREIGN KEY (a_name, categ, year) REFERENCES assocation on DELETE CASCADE,
        FOREIGN KEY (pid, fid, job) REFERENCES work_on on DELETE CASCADE )

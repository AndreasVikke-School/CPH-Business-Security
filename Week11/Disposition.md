# Week-11 A1 SQL injection
Group: Martin Frederiksen(cph-mf237), Andreas Vikke(cph-av).


### Give an example of a SQL inject which will give all users in a user table
- Input: "Hans' or 1 = 1;" --
- SQL: "SELECT * FROM USERS WHERE name = '" + input + "'"
-> SELECT * FROM USERS WHERE name = 'Hans' or 1 = 1; --'


### Explain how prepared statements prevent SQL injection


### Explain how to use placeholders in cases where prepared statements cannot do the job


### Explain how logging could be used to monitor injection attempts


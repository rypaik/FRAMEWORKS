[Securing Login Page Section From Sql Injection for Streamlit Apps](https://blog.jcharistech.com/2020/06/04/securing-login-page-section-from-sql-injections-for-streamlit-apps/)


``` sql
# regular SQL query
SELECT * FROM usertable WHERE userid = 5;

# Injection SQL query
SELECT * FROM userstable WHERE userid = 5 OR 1=1;

```

## SQL INJECTION CODE
``` sql
x'OR'1'='1
admin' --
admin'/*
' or 1=1--
' or 1=1/*

' or 1=1#
admin' #
') or '1'='1--
') or ('1'='1--

```
## DO'S
``` python
# ? and a tuple
'SELECT * FROM userstable WHERE username =? AND password = ?',(username,password)

# %s must b a tuple not a string
"SELECT * FROM userstable WHERE username= '%s' AND password='%s'",(username,password)

"SELECT * FROM userstable WHERE username= %s AND password= %s",(username,password)

```



## DONT'S!!!

### AVOID STRING CONCATENTATION WITH +

``` python
"SELECT * FROM userstable WHERE username = '" + username + "AND password= '" + password + "
"SELECT * FROM userstable WHERE username='" + username + "'AND password='" + password + "'";

```


### STRING FORMAT AND F-STRINGS
``` python

"SELECT * FROM userstable WHERE username='{}' AND password = '{}'".format(username,password)

f"SELECT * FROM userstable WHERE username= '{username}' AND password= '{password}'"

```


``` python
"SELECT * FROM userstable WHERE username='{}' AND password = '{}'".format(username,password)

# injection with admin 
“SELECT * FROM userstable WHERE username=‘admin ‘–‘ AND password = ‘admin ‘–‘”
```

# PythonApplicant

* [Introduction](Introduction)
* [Usage](#Usage)
* [Reference](#Limitations)


Introduction
-----------------
Applicant service with:
    - Kong API gateway
    - Python application
    - MySQL database

Usage
-----------------
We can use this in 2 ways:

From the main directory of PythonApplicant run:
- Use start script, but this just can use to test 1000 post requests and get all applicants because of some limitations:

```
./start.sh
```

- Use swagger docs to check and use full features :D
```
acccess http://127.0.0.1:9090/docs
```

Limitations
-----------------
- Kong API gateway can't add query string so you just can POST/GET /applicant to create and get applicants but can't filter by status
- Can't fetch swagger docs of FastAPI through Kong API gateway.
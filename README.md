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
From the main directory of PythonApplicant run:
```
./start.sh

```

You can access swagger docs for application through http://127.0.0.1:9090/docs or http://host.docker.internal:9090/docs

Limitations
-----------------
- Kong API gateway can't route "/process/{id}" to application
- Can't fetch swagger docs of FastAPI through Kong API gateway
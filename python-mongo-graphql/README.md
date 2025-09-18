Python 3.7+


##  REFERENCES
https://github.com/Shikha-code36/GraphQL_FastAPI/tree/main

NOT Helpful:
    https://strawberry.rocks/docs


FastAPI (pip install fastapi)
Strawberry (pip install strawberry)
PyMongo (pip install pymongo)
Uvicorn (pip install uvicorn)
requirements.txt
fastapi strawberry pymongo uvicorn
pip install -r requirements.txt --upgrade

## GraphQL Setup

```

pip install annotated-types anyio certifi charset-normalizer click colorama dnspython fastapi
pip install graphql-core h11 httpcore idna iniconfig packaging pluggy
pip install pydantic pydantic_core pymongo pytest python-dateutil python-multipart requests

pip install six sniffio starlette strawberry-graphql typing_extensions urllib3 uvicorn
python -m uvicorn main:app --reload

```

<!-- OPEN git bash
python -m venv pmg_env
source pmg_env/bin/activate

pip install 'strawberry-graphql[debug-server]'
pip install pymongo
pip install uvicorn -->

# CRUD Operation GraphQL FastAPI with MongoDB

# Examples
## Create Employee
To create a new employee, send a GraphQL mutation request:
``` mutation MyMutation {
createEmployee(name: "Bob", role: "Manager") {
    id
    name
    role
  }
}
```
## Insert multiple employees
To create multiple employees, send a GraphQL mutation request:
``` mutation MyMutation {
insertEmployeesArrayV1(
    employees: [{name: "Tanmay", role: "Software engineer"}, {name: "Prachi", role: "HR"}]
  ) {
    id
    name
    role
  }
}
```

## Get all employees
To get a list of all employees, send a GraphQL query request:
``` query MyQuery {
employees {
    id
    name
    role
  }
}
```

## Update employee
To update a employee, send a GraphQL mutation request:
``` mutation MyMutation {
updateEmployee(id: 4, name: "Harry", role: "Graphic designer") {
    id
    name
    role
  }
}
```

## Delete employee
To delete a employee, send a GraphQL mutation request:
``` mutation MyMutation {
deleteEmployee(id: 2) {
    id
    name
  }
}
```
## Get employee by role
To get a specific employee role, send a GraphQL query request:
```query MyQuery {
  getEmployeeByRole(role: "Developer") {
    id
    name
    role
  }
}
```

## Search employee by role
To search a specific employee role, send a GraphQL query request:
``` query MyQuery {
searchEmployeeByRole(keyword: "dev") {
    id
    name
    role
  }
}
```
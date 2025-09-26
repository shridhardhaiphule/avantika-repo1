# 1. String practice
- Work with strings in Node.js
- Convert strings to Date objects
- Split strings by comma
- Shuffle letters in a word

Run in terminal:
```bash
cd nodejs-practice
node string_practice.js
```
### Example output
```
Original String: Hello
Uppercase: HELLO
Lowercase: hello
Date object: 2025-09-23T00:00:00.000Z
Year: 2025
Month: 9
Day: 23
Split array: [ 'apple', 'banana', 'cherry' ]
Original word: practice
Jumbled word: accrtpie
```


# 2. Create a project using Next.js (Change basic template)
- Added a **welcome message** and **clickable button** on the page.

- Run in terminal:
```bash
cd next_app_example
npm install
npm run dev
```
**View page:** [http://localhost:3000](http://localhost:3000)



# 3. GraphQL API

### Run server
```bash
cd graphql_server
uvicorn main:app --reload
```

**GraphQL page:** [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)



# 4. Next.js setup
```bash
npx create-next-app@latest next_app_example
cd next_app_example
npm install
npm run dev
```

**GraphQL tester page:** [http://localhost:3000/graphql_tester](http://localhost:3000/graphql_tester)



# 5. Example Graphql
- Add a person
```
mutation MyMutation {
  addPerson(age: 24, email: "abhi@gmail.com", name: "Abhi") {
    age
    createdAt
    email
    id
    name
  }
}
```
- Get all people
```
query MyQuery {
  allPeople {
    age
    createdAt
    email
    id
    name
  }
}
```


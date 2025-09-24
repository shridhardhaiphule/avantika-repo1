# Node.js & Next.js

## 1. String practice
- Work with strings in Node.js
- Convert string to Date objects
- Split strings by comma
- Shuffle letters in a word

Run in terminal
```bash
cd nextjs-graphql-app
node string-jumble.js
```

Output
```
Original String: Hello
Uppercase: HELLO
Lowercase: hello
Date object: 2025-09-23T00:00:00.000Z
Year: 2025
Month: 9
Day: 23
Split array: [ 'apple', 'banana', 'cherry' ]
Original Word: practice
Jumbled Word: cpiretca
```

## 2. Create a project using Next.js(Change basic template)
- Added a welcome message and clickable button on the page
- Run in terminal
```bash
cd nextjs-graphql-app
npm run dev
```
**View page:** [http://localhost:3000/welcomepage](http://localhost:3000/welcomepage)


## 3. Next.js setup
```bash
npx create-next-app@latest nextjs-graphql-app
cd nextjs-graphql-app
npm install graphql express-graphql mongodb
npm run dev
```
**View page:** [http://localhost:3000](http://localhost:3000)

**View page:** [http://localhost:3000/api/graphql](http://localhost:3000/api/graphql)


## 4. Example
- Create a new user
```
mutation {
  createUser(name: "Alice", role: "Admin") {
    id
    name
    role
  }
}
```

- Get all users
```
query {
  getUsers {
    id
    name
    role
  }
}
```

- Get a user by ID
```
query {
  getUser(id: "68d3c0c80f4cba846f70407d") {
    id
    name
    role
  }
}
```

- Update a user
```
mutation {
  updateUser(id: "68d3c0c80f4cba846f70407d", name: "Jane Doe", role: "Editor") {
    id
    name
    role
  }
}
```

- Delete a user
```
mutation {
  deleteUser(id: "68d3c0c80f4cba846f70407d")
}
```




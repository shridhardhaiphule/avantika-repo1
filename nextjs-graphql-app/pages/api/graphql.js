import { graphqlHTTP } from "express-graphql";
import { buildSchema } from "graphql";
import { connectToDatabase } from "../../lib/mongodb";
import { ObjectId } from "mongodb";

// Define GraphQL schema
const schema = buildSchema(`
    type User {
        id: ID!
        name: String!
        role: String!
    }

    type Query {
        getUsers: [User!]!
        getUser(id: ID!): User
    }

    type Mutation {
        createUser(name: String!, role: String!): User
        updateUser(id: ID!, name: String, role: String): User
        deleteUser(id: ID!): String
    }
`);

export default async function handler(req, res) {
    const db = await connectToDatabase();

    const root = {
        getUsers: async () => {
        const users = await db.collection("users").find({}).toArray();
        return users.map(u => ({ id: u._id.toString(), name: u.name, role: u.role }));
    },
        getUser: async ({ id }) => {
        const user = await db.collection("users").findOne({ _id: new ObjectId(id) });
        return user ? { id: user._id.toString(), name: user.name, role: user.role } : null;
    },
        createUser: async ({ name, role }) => {
        const result = await db.collection("users").insertOne({ name, role });
        return { id: result.insertedId.toString(), name, role };
    },
        updateUser: async ({ id, name, role }) => {
        const updateData = {};
        if (name) updateData.name = name;
        if (role) updateData.role = role;

        await db.collection("users").updateOne(
        { _id: new ObjectId(id) },
        { $set: updateData }
        );

        const updatedUser = await db.collection("users").findOne({ _id: new ObjectId(id) });
        return { id: updatedUser._id.toString(), name: updatedUser.name, role: updatedUser.role };
    },
        deleteUser: async ({ id }) => {
        await db.collection("users").deleteOne({ _id: new ObjectId(id) });
        return "User deleted";
    }
    };

    await graphqlHTTP({
        schema,
        rootValue: root,
        graphiql: true,
    })(req, res);
}

import { MongoClient } from 'mongodb';

const url = "mongodb://127.0.0.1:27017";
const dbName = "nextjs-graphql-app";

let client;
let db;

export async function connectToDatabase() {
    if (db) return db;
    client = await MongoClient.connect(url);
    db = client.db(dbName);
    return db;
}
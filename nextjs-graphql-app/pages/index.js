import { useState } from 'react';

export default function Home() {
    const [query, setQuery] = useState(`{
        getUsers {
            id
            name
            role
        }
    }`);
    const [ output, setOutput ] = useState('');

    async function executeQuery() {
        const response = await fetch('/api/graphql', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });
        const result = await response.json();
        setOutput(JSON.stringify(result, null, 2));
    }

    return (
        <div style={{ padding: '20px' }}>
            <h1>GraphQL Tester</h1>
            <textarea
                rows={10}
                cols={80}
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            ></textarea>
            <br />
            <button onClick={executeQuery}>Execute Query</button>
            <h2>Output:</h2>
            <textarea rows={10} cols={80} value={output} readOnly></textarea>
        </div>
    );
}

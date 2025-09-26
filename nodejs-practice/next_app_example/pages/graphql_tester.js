import { useState } from 'react';

export default function GraphQLTester() {
    const [query, setQuery] = useState('');
    const [result, setResult] = useState('');

    const executeQuery = async () => {
        if (!query.trim()) {
            setResult('Please enter a GraphQL query or mutation.');
            return;
    }

    try {
        const res = await fetch('http://127.0.0.1:8000/graphql', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query }),
        });
        const data = await res.json();
        setResult(JSON.stringify(data, null, 2));
    } catch (err) {
        setResult(err.message);
    }
    };

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial' }}>
        <h1>GraphQL Tester</h1>

        <textarea
        rows={10}
        cols={50}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter GraphQL query or mutation"
        />
        <br />
        <button onClick={executeQuery} style={{ marginTop: '10px' }}>
        Execute
        </button>
        <br />
        <textarea
        rows={10}
        cols={50}
        value={result}
        readOnly
        style={{ marginTop: '10px' }}
        />
    </div>
    );
}

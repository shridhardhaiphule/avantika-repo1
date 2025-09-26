export default function Home() {
    return (
        <div style={{ padding: "20px", fontFamily: "Arial" }}>
        <h1>Welcome!</h1>
        <p>This is first custom Next.js page.</p>

        <button onClick={() => alert("Button clicked!")}>Click Me</button>
    </div>
    );
}

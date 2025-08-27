# Addition API (Flask)

This project provides a simple REST API for addition using Python 3 and the Flask framework.

## Features
- `/add` endpoint: Accepts two numbers (`a` and `b`) as query parameters and returns their sum as JSON.
- Unit tests for API functionality using Python's `unittest` and Flask's test client.

## Setup
1. Install Python 3.
2. Install Flask:
   ```powershell
   pip install flask
   ```

## Running the API
1. Navigate to the API directory:
   ```powershell
   cd python-practice\sum_flask_api
   ```
2. Start the Flask server:
   ```powershell
   python addition_api.py
   ```
3. Access the API in your browser or via curl:
   ```
   http://127.0.0.1:5000/add?a=5&b=7
   ```

## Running Unit Tests
1. Ensure the API code is present in `addition_api.py` and the test code in `test_addition_api.py`.
2. Run the tests:
   ```powershell
   python test_addition_api.py
   ```
   or, to discover all tests:
   ```powershell
   python -m unittest discover
   ```

## Example Response
```
GET /add?a=2&b=3
Response: { "result": 5.0 }
```

## Notes
- The API returns a 400 error if parameters are missing or invalid.
- The server runs in debug mode for development purposes.

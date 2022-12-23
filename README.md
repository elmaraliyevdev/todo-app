## Simple ToDo app with FastAPI

This is a simple ToDo app with FastAPI.

### How to run

1. Clone the repo

    ```bash
    git clone https://github.com/elmaraliyevdev/todo-app
    ```
2. Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
3. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run the app
    ```bash
    uvicorn main:app --reload
    ```
5. Go to http://localhost:8000/docs
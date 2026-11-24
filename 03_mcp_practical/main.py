
import sqlite3
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("todo-server")

# Database file will be created inside this project folder
DB_PATH = Path(__file__).with_name("todos.db")


def get_connection():
    """Create a connection to the SQLite database."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create the todos table if it does not exist."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                completed INTEGER DEFAULT 0
            )
            """
        )


# Initialize database when server starts
initialize_database()


@mcp.tool()
def add_todo(title: str, description: str = "") -> str:
    """Add a new task to the Todo List."""
    if not title.strip():
        return "Error: Todo title cannot be empty."

    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO todos (title, description) VALUES (?, ?)",
            (title.strip(), description.strip()),
        )
        todo_id = cursor.lastrowid

    return f"Todo created successfully. ID: {todo_id}, Title: {title}"


@mcp.tool()
def list_todos() -> str:
    """Get all tasks from the Todo List."""
    with get_connection() as connection:
        todos = connection.execute(
            "SELECT * FROM todos ORDER BY id"
        ).fetchall()

    if not todos:
        return "Your Todo List is empty."

    result = []
    for todo in todos:
        status = "Completed" if todo["completed"] else "Pending"
        result.append(
            f"ID: {todo['id']} | Title: {todo['title']} | "
            f"Description: {todo['description']} | Status: {status}"
        )

    return "\n".join(result)


@mcp.tool()
def complete_todo(todo_id: int) -> str:
    """Mark a Todo task as completed using its ID."""
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE todos SET completed = 1 WHERE id = ?",
            (todo_id,),
        )

    if cursor.rowcount == 0:
        return f"Todo with ID {todo_id} was not found."

    return f"Todo {todo_id} marked as completed."


@mcp.tool()
def delete_todo(todo_id: int) -> str:
    """Delete a Todo task using its ID."""
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM todos WHERE id = ?",
            (todo_id,),
        )

    if cursor.rowcount == 0:
        return f"Todo with ID {todo_id} was not found."

    return f"Todo {todo_id} deleted successfully."


@mcp.tool()
def get_todo(todo_id: int) -> str:
    """Get one Todo task using its ID."""
    with get_connection() as connection:
        todo = connection.execute(
            "SELECT * FROM todos WHERE id = ?",
            (todo_id,),
        ).fetchone()

    if todo is None:
        return f"Todo with ID {todo_id} was not found."

    status = "Completed" if todo["completed"] else "Pending"

    return (
        f"ID: {todo['id']}\n"
        f"Title: {todo['title']}\n"
        f"Description: {todo['description']}\n"
        f"Status: {status}"
    )


@mcp.resource("todos://all")
def todos_resource() -> str:
    """Provide all Todo tasks as an MCP resource."""
    return list_todos()


if __name__ == "__main__":
    mcp.run(transport="stdio")

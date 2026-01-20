# MCP Database Server

A **Model Context Protocol (MCP)** server that provides database user management functionality for AI assistants. This server exposes tools for adding and retrieving user information from a SQLite database.

## 🚀 What is MCP?

The **Model Context Protocol (MCP)** is an open standard that enables AI applications to securely connect to external data sources and tools. Think of it as a bridge between AI assistants (like Claude, ChatGPT, or custom agents) and your local or remote resources.

### Why Use MCP?

- **Standardized Integration**: Connect AI assistants to databases, APIs, and tools using a unified protocol
- **Tool Exposure**: Let AI assistants perform actions on your behalf (database operations, file management, etc.)
- **Secure Communication**: Controlled access to your resources with proper authentication
- **Extensibility**: Build custom servers to expose any functionality you need

## 📋 Features

This MCP server provides the following tools:

### 1. **add_user**
Add a new user to the database with username, email, and mobile number.

**Parameters:**
- `username` (string): User's name
- `email` (string): User's email address
- `mobileNumber` (string): User's mobile number

### 2. **get_user_by_email**
Retrieve user information by email address.

**Parameters:**
- `email` (string): Email address to search for

**Returns:**
- User object with id, username, email, created_at, and mobileNumber
- Error message if user not found

## 🛠️ Technology Stack

- **FastMCP**: Python framework for building MCP servers
- **SQLite**: Lightweight database for user storage
- **Python 3.13+**: Modern Python features
- **HTTP Transport**: RESTful API interface

## 📦 Installation

### Prerequisites

- Python 3.13 or higher
- pip or uv package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd mcp_server
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**
   
   Using pip:
   ```bash
   pip install -e .
   ```
   
   Or using uv:
   ```bash
   uv pip install -e .
   ```

## 🚦 Running the Server

### Standard Mode

```bash
python main.py
```

The server will start on `http://0.0.0.0:8001`

### Using FastMCP CLI

```bash
fastmcp run main.py
```

### Using uv

```bash
uv run python main.py
```

## 📡 Usage

### With MCP-Compatible Clients

Configure your MCP client (e.g., Claude Desktop, Continue, or custom client) to connect to:

```
http://localhost:8001
```

### Example Tool Calls

**Adding a user:**
```python
add_user(
    username="John Doe",
    email="john@example.com",
    mobileNumber="+1234567890"
)
```

**Retrieving a user:**
```python
get_user_by_email(email="john@example.com")
```

## 🗄️ Database Schema

The server automatically creates a SQLite database (`database.db`) with the following schema:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mobileNumber TEXT NOT NULL
)
```

## 🔧 Configuration

- **Host**: `0.0.0.0` (accessible from network)
- **Port**: `8001`
- **Transport**: HTTP
- **Database**: `database.db` (created in the same directory as main.py)

To change these settings, modify the values in [main.py](main.py#L68):

```python
mcp.run(transport="http", host="0.0.0.0", port=8001)
```

## 📁 Project Structure

```
mcp_server/
├── main.py           # MCP server implementation
├── pyproject.toml    # Project dependencies and metadata
├── README.md         # This file
├── database.db       # SQLite database (created at runtime)
└── .venv/           # Virtual environment (if created)
```

## 🔒 Security Notes

- This server is configured to listen on `0.0.0.0`, making it accessible from your network
- For production use, consider:
  - Adding authentication
  - Using HTTPS transport
  - Implementing input validation
  - Adding rate limiting
  - Restricting host to `127.0.0.1` for local-only access

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

[Add your license information here]

## 🆘 Troubleshooting

### Server won't start
- Ensure port 8001 is not already in use
- Check that Python 3.13+ is installed
- Verify all dependencies are installed

### Database errors
- The database file will be created automatically
- Ensure write permissions in the project directory

### Connection issues
- Verify the server is running with `netstat -an | findstr 8001`
- Check firewall settings if connecting from another machine

## 📚 Learn More

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

---

**Built with ❤️ using FastMCP and Python**
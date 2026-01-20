from fastmcp import FastMCP
import sqlite3
import os

mcp = FastMCP(name="Database")

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool
def sub(a: int, b: int) -> int:
    return a - b

@mcp.tool
def mul(a: int, b: int) -> int:
    return a * b


@mcp.tool
def mod(a: int, b: int) -> int:
    return a % b
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0" , port=6080)

# __init__.py
from src.chatppt.ppt import mcp


def main():
    """MCP Chatppt Server - HTTP call Chatppt API for MCP"""
    mcp.run()


if __name__ == "__main__":
    main()

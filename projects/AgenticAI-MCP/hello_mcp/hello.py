from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-MCP")

@mcp.tool()
def add(a:int|float , b:int| float):
    """
    Docstring for add
    
    :param a: Description
    :type a: int | float
    :param b: Description
    :type b: int | float
    """
    return a+b

if __name__ == "__main__":
    mcp.run(transport="stdio")
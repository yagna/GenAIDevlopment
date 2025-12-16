from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calc-MCP")

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
@mcp.tool()
def subtract(a:int|float , b:int| float):
    """_summary_

    Args:
        a (int | float): _description_
        b (int | float): _description_

    Returns:
        _type_: _description_
    """
    return a-b
@mcp.tool()
def multiply(a:int|float, b:int| float):
    """_summary_

    Args:
        a (int | float): _description_
        b (int | float): _description_

    Returns:
        _type_: _description_
    """
    return a*b
@mcp.tool()
def divide(a:int|float, b:int| float):
    """_summary_

    Args:
        a (int | float): _description_
        b (int | float): _description_

    Returns:
        _type_: _description_
    """
    return a/b



if __name__ == "__main__":
    mcp.run(transport="stdio")
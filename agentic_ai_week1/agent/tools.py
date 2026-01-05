"""
Tools module for defining agent tools and utilities.
"""


class Tool:
    """
    Base class for agent tools.
    """
    
    def __init__(self, name, description, func):
        """
        Initialize a tool.
        
        Args:
            name: Name of the tool
            description: Description of what the tool does
            func: Function to execute when tool is called
        """
        self.name = name
        self.description = description
        self.func = func
    
    def execute(self, *args, **kwargs):
        """
        Execute the tool's function.
        
        Args:
            *args: Positional arguments for the tool
            **kwargs: Keyword arguments for the tool
            
        Returns:
            Result of the tool execution
        """
        return self.func(*args, **kwargs)


def get_default_tools():
    """
    Get a list of default tools for the agent.
    
    Returns:
        List of Tool instances
    """
    tools = []
    
    # Example tool
    def search(query):
        return f"Search results for: {query}"
    
    tools.append(Tool(
        name="search",
        description="Search for information",
        func=search
    ))
    
    return tools

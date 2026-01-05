"""
Memory module for agent memory management.
"""


class Memory:
    """
    Memory system for the agent to store and retrieve information.
    """
    
    def __init__(self, max_size=100):
        """
        Initialize the memory system.
        
        Args:
            max_size: Maximum number of items to store in memory
        """
        self.max_size = max_size
        self.store = []
    
    def add(self, item):
        """
        Add an item to memory.
        
        Args:
            item: Item to store in memory
        """
        self.store.append(item)
        
        # Keep only the most recent items if max_size is exceeded
        if len(self.store) > self.max_size:
            self.store = self.store[-self.max_size:]
    
    def get_recent(self, n=10):
        """
        Get the n most recent items from memory.
        
        Args:
            n: Number of recent items to retrieve
            
        Returns:
            List of recent items
        """
        return self.store[-n:] if len(self.store) >= n else self.store
    
    def clear(self):
        """
        Clear all items from memory.
        """
        self.store = []
    
    def search(self, query):
        """
        Search for items in memory matching the query.
        
        Args:
            query: Search query
            
        Returns:
            List of matching items
        """
        # Simple implementation - can be enhanced with semantic search
        results = [item for item in self.store if query.lower() in str(item).lower()]
        return results

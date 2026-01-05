"""
Main entry point for the agentic AI application.
"""

from agent.agent import Agent
from agent.tools import get_default_tools
from agent.llm import LLM
from agent.memory import Memory
from agent.logger import Logger


def main():
    """
    Main function to initialize and run the agent.
    """
    # Initialize components
    logger = Logger(name="AgenticAI")
    logger.info("Initializing Agentic AI System...")
    
    # Create LLM instance
    llm = LLM(model_name="gpt-3.5-turbo")
    logger.info(f"LLM initialized: {llm.model_name}")
    
    # Create memory system
    memory = Memory(max_size=100)
    logger.info("Memory system initialized")
    
    # Get default tools
    tools = get_default_tools()
    logger.info(f"Loaded {len(tools)} tools")
    
    # Create agent
    agent = Agent(llm=llm, tools=tools, memory=memory, logger=logger)
    logger.info("Agent created successfully")
    
    # Example task
    task = "Analyze the latest AI trends"
    result = agent.run(task)
    print(f"\nResult: {result}")
    
    logger.info("Agentic AI System completed")


if __name__ == "__main__":
    main()

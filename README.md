# Azurite Cognitive Architecture v0 for Generative Agents
 Prototype Psudeocode Repo for project developments based on standfords Generative agents paper and lilianwengs article on LLM Powered Autonomous Agents

https://lilianweng.github.io/posts/2023-06-23-agent/#agent-system-overview

This codebase draft represents a cognitive architecture for an agent. It consists of several classes that handle different aspects of the agent's functionality. Here's an overview of the main components:

1. PerceptionSystem:
   - Responsible for processing sensory input and converting it into an internal representation.
   - Uses a deque to store sensory inputs and limit the maximum number of inputs stored.

2. MemorySystem:
   - Handles different types of memory: sensory memory, short-term memory, and long-term memory.
   - Uses deques to store sensory and short-term memories with a maximum size.
   - Utilizes an SQLite database for long-term memory storage.
   - Provides methods for storing, retrieving, and pruning memory.

3. EmotionalSystem:
   - Represents the emotional system of the agent.
   - Maintains the current emotion and its intensity.
   - Provides methods for updating and retrieving the emotional state.

4. ReasoningSystem:
   - Represents the reasoning system of the agent.
   - Includes methods for making decisions, planning actions, and reacting to observations.

5. ResourceSystem:
   - Handles the management of resources available to the agent.
   - Stores resources in a dictionary and provides methods for adding, using, and checking resource availability.

6. AgentMessage:
   - Represents a message that can be sent or received by an agent.
   - Contains information about the sender, recipient, and content of the message.

7. Agent:
   - Represents an agent and combines the functionalities of the above components.
   - Includes methods for interacting with users, generating code, managing goals and constraints, executing commands, and more.
   - Maintains an inbox for receiving messages and provides methods for sending and receiving messages.

8. AgentManager:
   - Manages a collection of agents.
   - Provides methods for creating, removing, and retrieving agents.
   - Supports processing messages for all agents.

The codebase draft provides a foundation for implementing cognitive architectures and agents with various functionalities. However, many methods are currently empty or marked as "TODO" and require implementation based on the specific requirements of the cognitive model or application.

To use this codebase draft, you can create instances of the `Agent` class using the `AgentManager`. The `Agent` instances can then be customized by adding goals, constraints, commands, and resources. The agents can interact with users, process messages, execute commands, and perform other actions based on the implemented methods.

Note that some parts of the codebase, such as database interactions and pattern matching in memory retrieval, are placeholders marked with "TODO" comments. These areas need to be implemented according to the specific requirements of the cognitive model or application.

Please refer to the comments in the codebase draft for detailed explanations of each class, method, and their respective parameters and return values. You can also extend and customize the codebase according to your specific needs and requirements.

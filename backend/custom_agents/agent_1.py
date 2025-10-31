from agents import Agent, Runner, SQLiteSession
from langfuse import observe


DB_PATH="data/assistant_sessions.db"

def get_agent_session(session_id: str) -> SQLiteSession:
    # Pass the session_id to isolate conversations for each user/thread.
    # Pass the DB_PATH to make the session persistent (it saves to a file).
    return SQLiteSession(session_id, DB_PATH)

class Agent1:
    def __init__(self):
        self.name = "Agent 1"
        self.model = "gpt-4.1-nano"
        self.instructions = f"You are a super funny joke teller."

        self.agent = Agent(
            name=self.name,
            model=self.model,
            instructions=self.instructions
        )

    @observe(name="Agent 1 - run")
    async def run(self, user_id: str, user_input: str) -> str:
        print(f"Agent received input: {user_input}")
        session = get_agent_session(user_id)

        response = await Runner.run(self.agent, user_input, session=session)
        return response.final_output
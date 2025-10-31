# AI Chatbot Starter Template

A full-stack AI chatbot starter template built with modern technologies and best practices. This template provides a robust foundation for building conversational AI applications with observability, persistent sessions, and a polished user interface.

## 🚀 Features

- **Modern Frontend**: Built with Next.js 16, React 19, and TailwindCSS
- **Interactive UI**: Powered by [`@assistant-ui/react`](https://github.com/Yonom/assistant-ui) for rich chat experiences
- **AI Agents**: OpenAI Agents SDK integration for intelligent conversation handling
- **Observability**: Complete monitoring and tracing with [Langfuse](https://langfuse.com/)
- **Persistent Sessions**: SQLite-based conversation history and session management
- **Streaming Responses**: Real-time message streaming for smooth user experience
- **Type Safety**: Full TypeScript support across the frontend stack

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │
│   (Next.js)     │◄───┤   (FastAPI)     │
│                 │    │                 │
│ • Assistant UI  │    │ • OpenAI Agents │
│ • Real-time     │    │ • Langfuse      │
│   Streaming     │    │ • SQLite        │
└─────────────────┘    └─────────────────┘
```

### Tech Stack

**Frontend:**
- Next.js 16 (App Router)
- React 19
- TypeScript
- TailwindCSS + Radix UI
- Assistant UI React Components
- Zustand for state management

**Backend:**
- FastAPI (Python)
- OpenAI Agents SDK
- Langfuse (LLM observability)
- SQLite (session persistence)
- UV for dependency management

## 🛠️ Quick Start

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm
- Python 3.12+
- [UV package manager](https://github.com/astral-sh/uv)
- OpenAI API key
- Langfuse account (optional but recommended). You can also selfhost langfuse or [run it locally](https://langfuse.com/self-hosting/deployment/docker-compose) 

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd AI-Chatbot-Starter
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies with UV
uv sync

# Create environment file
cp .env.example .env
```

Configure your `.env` file:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Langfuse Configuration (optional)
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_HOST=https://cloud.langfuse.com  # or your self-hosted instance
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
# or
yarn install
# or
pnpm install
```

### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
uv run fastapi dev main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Open [http://localhost:4000](http://localhost:4000) in your browser.

## 📁 Project Structure

```
AI-Chatbot-Starter/
├── backend/
│   ├── main.py                # FastAPI application entry point
│   ├── pyproject.toml         # Python dependencies and config
│   ├── custom_agents/         # AI agent implementations
│   │   ├── __init__.py
│   │   └── agent_1.py        # Example joke-telling agent
│   └── data/                 # SQLite database storage
│       └── assistant_sessions.db
├── frontend/
│   ├── app/
│   │   ├── layout.tsx       # Root layout
│   │   ├── page.tsx         # Chat interface
│   │   └── components/      # React components
│   ├── components/
│   │   ├── assistant-ui/    # Chat UI components
│   │   └── ui/             # Reusable UI components
│   ├── package.json
│   └── next.config.ts
└── README.md
```

## 🤖 Creating Custom Agents

The template includes an example agent (`Agent1`) that demonstrates the basic structure. To create your own agent:

1. **Create a new agent file** in `backend/custom_agents/`:

```python
from agents import Agent, Runner, SQLiteSession
from langfuse import observe

class MyCustomAgent:
    def __init__(self):
        self.name = "My Custom Agent"
        self.model = "gpt-4"  # or "gpt-3.5-turbo"
        self.instructions = "Your custom instructions here"
        
        self.agent = Agent(
            name=self.name,
            model=self.model,
            instructions=self.instructions
        )
    
    @observe(name="My Custom Agent - run")
    async def run(self, user_id: str, user_input: str) -> str:
        session = get_agent_session(user_id)
        response = await Runner.run(self.agent, user_input, session=session)
        return response.final_output
```

2. **Update `main.py`** to use your new agent:

```python
from custom_agents.my_custom_agent import MyCustomAgent

# Initialize your agent
my_agent = MyCustomAgent()

# Use in the chat endpoint
@app.post("/chat")
async def chat_endpoint(request: dict):
    # ... existing code ...
    response = await my_agent.run(request['user_id'], user_message)
    # ... rest of the function ...
```

## 📊 Observability with Langfuse

This template includes Langfuse integration for comprehensive LLM observability:

- **Conversation Tracking**: Monitor all chat interactions
- **Performance Metrics**: Track response times and token usage
- **Cost Analysis**: Monitor OpenAI API costs
- **Debugging**: Detailed trace information for troubleshooting

The `@observe` decorator automatically captures:
- Input and output data
- Execution time
- Token consumption
- Error traces

## 💾 Session Management

Conversations are automatically persisted using SQLite:

- Placeholder userid -> needs to be replaced with your actual userId
- Message history is maintained across browser sessions
- Conversations are isolated per user
- Database files are stored in `backend/data/`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `LANGFUSE_SECRET_KEY` | Langfuse secret key | No |
| `LANGFUSE_PUBLIC_KEY` | Langfuse public key | No |
| `LANGFUSE_HOST` | Langfuse host URL | No |

### Frontend Configuration

The frontend runs on port 4000 by default. You can modify this in:
- `frontend/package.json` scripts
- `backend/main.py` CORS origins


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request


## 🙏 Acknowledgments

- [Assistant UI](https://github.com/Yonom/assistant-ui) - For the excellent React chat components
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - For the AI agent framework
- [Langfuse](https://langfuse.com/) - For LLM observability and monitoring
- [FastAPI](https://fastapi.tiangolo.com/) - For the high-performance API framework
- [Next.js](https://nextjs.org/) - For the React framework

## 📚 Additional Resources

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
- [Assistant UI Documentation](https://docs.assistant-ui.com/)
- [Langfuse Documentation](https://langfuse.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)

---

**Happy coding! 🎉** If you build something cool with this template, I'd love to hear about it!

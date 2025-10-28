import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

# Create the FastAPI application instance
app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, etc.
    allow_headers=["*"],
)


# Define a path operation (route)
@app.get("/")
async def read_root():
    return {"message": "Hello World with UV and FastAPI!"}


@app.post("/chat")
async def chat_endpoint(request: dict):
    def event_generator():
        print("Received request:", request)
        # Placeholder: Your agent logic generates and yields events
        yield f"data: {json.dumps({'id': '1', 'role': 'assistant', 'content': 'Hello. I am the Research Agent.'})}\n\n"
        yield f"data: {json.dumps({'id': '2', 'role': 'assistant', 'content': 'I will now begin research...'})}\n\n"   # ... more events
        
    # Set media_type to 'text/event-stream' for SSE
    return StreamingResponse(event_generator(), media_type='text/event-stream')

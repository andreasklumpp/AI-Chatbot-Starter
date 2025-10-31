"use client";

import type { ReactNode } from "react";
import {
  AssistantRuntimeProvider,
  ChatModelRunResult,
  useLocalRuntime,
  type ChatModelAdapter,
} from "@assistant-ui/react";

const FastAPIAdapter: ChatModelAdapter = {
  async *run({ messages, abortSignal }) {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // USER ID Should come from authenticated user context
      body: JSON.stringify({ messages, user_id: "user-123" }), 
      signal: abortSignal,
    });


    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reader = response.body!.getReader();
    const decoder = new TextDecoder();
    let accumulatedContent = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      const events = chunk.split("\n\n").filter(Boolean);

      for (const event of events) {
        try {
          const jsonStr = event.replace(/^data: /, "").trim();
          const data = JSON.parse(jsonStr);
          accumulatedContent += data.content + " "; // Accumulate content
          const result: ChatModelRunResult = {
            content: [{ type: "text", text: accumulatedContent.trim() }],
          };
          yield result;
        } catch (error) {
        }
      }
    }
  },
};

export function MyRuntimeProvider({
  children,
}: Readonly<{
  children: ReactNode;
}>) {
  const runtime = useLocalRuntime(FastAPIAdapter);

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      {children}
    </AssistantRuntimeProvider>
  );
}

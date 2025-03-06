import React, { useState } from "react";
import axios from "axios";
import './App.css';

const Chat = () => {
  const API_URL = process.env.REACT_APP_API_URI;
  const [prompt, setPrompt] = useState("");
  const [resText, setResText] = useState("");

  const sendPrompt = async () => {
    if (!prompt.trim()) return;
    const response = await axios.post(`${API_URL}/api/llm/`, { prompt: prompt });
    if (response.statusText==="OK") {
      const text = response.data.response;
      setResText(text);
    }
  }

  return (
    <>
    <input type="textarea" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
    <button onClick={sendPrompt}>▶️</button>
    <p>{resText}</p>
    </>
  );
}

export default Chat;

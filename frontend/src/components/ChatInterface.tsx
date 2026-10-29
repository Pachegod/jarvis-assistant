import { useState } from 'react'
import VoiceControl from './VoiceControl'

export default function ChatInterface() {
  const [messages, setMessages] = useState<any[]>([])
  const [input, setInput] = useState('')

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { role: 'user', content: input }])
      setInput('')
    }
  }

  return (
    <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
      <div style={{ flex: 1, overflowY: 'auto', padding: '20px' }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ marginBottom: '10px' }}>
            <strong>{msg.role}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <div style={{ padding: '20px', borderTop: '1px solid #ccc' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type a message..."
          style={{ width: '100%', padding: '10px' }}
        />
        <button onClick={handleSend} style={{ marginTop: '10px', padding: '10px' }}>
          Send
        </button>
        <VoiceControl />
      </div>
    </div>
  )
}

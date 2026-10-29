import { useState } from 'react'
import ChatInterface from '../components/ChatInterface'
import Sidebar from '../components/Sidebar'

export default function Chat() {
  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <Sidebar />
      <ChatInterface />
    </div>
  )
}

import { Link } from 'react-router-dom'

export default function Sidebar() {
  return (
    <div style={{ width: '250px', backgroundColor: '#f0f0f0', padding: '20px' }}>
      <h2>Jarvis</h2>
      <nav style={{ marginTop: '20px' }}>
        <div style={{ marginBottom: '10px' }}>
          <Link to="/">Dashboard</Link>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <Link to="/chat">Chat</Link>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <Link to="/settings">Settings</Link>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <Link to="/integrations">Integrations</Link>
        </div>
      </nav>
    </div>
  )
}

import { useEffect, useState } from 'react'
import TaskDashboard from '../components/TaskDashboard'

export default function Dashboard() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Jarvis Assistant Dashboard</h1>
      <TaskDashboard />
    </div>
  )
}

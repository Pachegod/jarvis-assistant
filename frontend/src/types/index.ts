export interface Message {
  id: number
  role: 'user' | 'assistant'
  content: string
  createdAt: string
}

export interface Conversation {
  id: number
  title: string
  createdAt: string
}

export interface User {
  id: number
  email: string
  username: string
}

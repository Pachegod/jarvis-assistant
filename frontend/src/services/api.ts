import axios from 'axios'
import { Message, Conversation } from '../types'

const API_BASE_URL = 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
})

export const chatAPI = {
  sendMessage: async (content: string, conversationId?: number): Promise<Message> => {
    const response = await api.post('/chat', { content, conversation_id: conversationId })
    return response.data
  },

  getConversations: async (): Promise<Conversation[]> => {
    const response = await api.get('/conversations')
    return response.data
  },

  createConversation: async (title: string): Promise<Conversation> => {
    const response = await api.post('/conversations', { title })
    return response.data
  },
}

export default api

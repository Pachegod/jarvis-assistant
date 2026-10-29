export class WebSocketService {
  private ws: WebSocket | null = null
  private url: string

  constructor(url: string = 'ws://localhost:8000/ws') {
    this.url = url
  }

  connect(): Promise<void> {
    return new Promise((resolve, reject) => {
      try {
        this.ws = new WebSocket(this.url)
        this.ws.onopen = () => resolve()
        this.ws.onerror = (error) => reject(error)
      } catch (error) {
        reject(error)
      }
    })
  }

  send(message: string): void {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(message)
    }
  }

  disconnect(): void {
    if (this.ws) {
      this.ws.close()
      this.ws = null
    }
  }

  onMessage(callback: (data: string) => void): void {
    if (this.ws) {
      this.ws.onmessage = (event) => callback(event.data)
    }
  }
}

export const wsService = new WebSocketService()

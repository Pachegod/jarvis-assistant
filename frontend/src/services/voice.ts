export class VoiceService {
  private mediaRecorder: MediaRecorder | null = null
  private audioStream: MediaStream | null = null
  private chunks: Blob[] = []

  async startRecording(): Promise<void> {
    try {
      this.audioStream = await navigator.mediaDevices.getUserMedia({ audio: true })
      this.mediaRecorder = new MediaRecorder(this.audioStream)
      this.chunks = []

      this.mediaRecorder.ondataavailable = (event) => {
        this.chunks.push(event.data)
      }

      this.mediaRecorder.start()
    } catch (error) {
      console.error('Error accessing microphone:', error)
      throw error
    }
  }

  stopRecording(): Blob | null {
    if (!this.mediaRecorder) return null

    this.mediaRecorder.stop()

    if (this.audioStream) {
      this.audioStream.getTracks().forEach(track => track.stop())
    }

    return new Blob(this.chunks, { type: 'audio/webm' })
  }
}

export const voiceService = new VoiceService()

import { useState } from 'react'
import { voiceService } from '../services/voice'

export default function VoiceControl() {
  const [isRecording, setIsRecording] = useState(false)

  const handleStartRecording = async () => {
    try {
      await voiceService.startRecording()
      setIsRecording(true)
    } catch (error) {
      console.error('Error starting recording:', error)
    }
  }

  const handleStopRecording = () => {
    const audioBlob = voiceService.stopRecording()
    setIsRecording(false)
    // Handle audio blob
  }

  return (
    <button
      onClick={isRecording ? handleStopRecording : handleStartRecording}
      style={{ marginTop: '10px', padding: '10px', marginLeft: '10px' }}
    >
      {isRecording ? 'Stop Recording' : 'Start Recording'}
    </button>
  )
}

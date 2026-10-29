"""
Speech-to-Text module using Google Cloud Speech API.
"""

from typing import Optional


class SpeechToText:
    """Converts audio to text."""
    
    def __init__(self, language: str = "pt-BR"):
        """
        Initialize STT service.
        
        Args:
            language: Language code (default: Portuguese-Brazil)
        """
        self.language = language
    
    def transcribe(self, audio_path: str) -> Optional[str]:
        """
        Transcribe audio file to text.
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Transcribed text
        """
        # Implementation placeholder
        pass
    
    def transcribe_stream(self, audio_stream):
        """Transcribe from audio stream in real-time."""
        # Implementation placeholder
        pass


# Global instance
stt = SpeechToText()

import random

class IntentExtractor:
    """
    Stage 1: Intent Extraction
    Decodes sentiment, tone, and core message from the source text.
    """

    def extract(self, text: str) -> dict:
        """
        Mock implementation of intent extraction.
        In a real scenario, this would use an LLM to analyze the text.
        """
        # Simulated analysis based on keywords or random assignment for the demo
        
        # Simple keyword-based mock logic
        emotional_tone = "Neutral"
        if "happy" in text.lower() or "great" in text.lower():
            emotional_tone = "Joyful"
        elif "sad" in text.lower() or "sorry" in text.lower():
            emotional_tone = "Melancholy"
        elif "urgent" in text.lower() or "now" in text.lower():
            emotional_tone = "Urgent"

        return {
            "source_text": text,
            "emotional_tone": emotional_tone,
            "core_intent": "Convey information" if len(text) > 20 else "Greeting/Phatic",
            "detected_nuances": ["Sincerity", "Politeness"] if "please" in text.lower() else ["Directness"]
        }

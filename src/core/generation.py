class ConstrainedGenerator:
    """
    Stage 3: Constrained Generation
    Reconstructs the message in the target language while preserving specific stylistic elements.
    """

    def generate(self, intent_data: dict, cultural_data: dict) -> str:
        """
        Mock implementation of constrained generation.
        Combines intent and cultural context to produce the final output.
        """
        target_lang = cultural_data.get("target_lang", "English")
        tone = intent_data.get("emotional_tone", "Neutral")
        idioms = cultural_data.get("suggested_idioms", [])

        # If we found an idiom, return it as the primary result
        if idioms and idioms[0]:
            return idioms[0]

        # Otherwise, return a simulated translation based on tone
        start_phrases = {
            "French": {
                "Joyful": "Avec grand plaisir, ",
                "Urgent": "Attention! ",
                "Neutral": "Voici: "
            },
            "Spanish": {
                "Joyful": "¡Con alegría! ",
                "Urgent": "¡Urgente! ",
                "Neutral": "Aquí tienes: "
            }
        }

        prefix = start_phrases.get(target_lang, {}).get(tone, f"[{target_lang} Translation]: ")
        original_text = intent_data.get("source_text", "")
        
        return f"{prefix}{original_text} (Transcreated for {tone} impact)"

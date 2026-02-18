from src.core.intent import IntentExtractor
from src.core.culture import CulturalRetriever
from src.core.generation import ConstrainedGenerator

class TranscreationPipeline:
    """
    Orchestrates the 3-stage Resonance Engine pipeline.
    """
    def __init__(self):
        self.intent_extractor = IntentExtractor()
        self.cultural_retriever = CulturalRetriever()
        self.constrained_generator = ConstrainedGenerator()

    def process(self, text: str, target_lang: str) -> dict:
        # Stage 1: Intent Extraction
        intent_result = self.intent_extractor.extract(text)

        # Stage 2: Cultural Retrieval
        culture_result = self.cultural_retriever.retrieve(intent_result, target_lang)

        # Stage 3: Constrained Generation
        final_output = self.constrained_generator.generate(intent_result, culture_result)

        return {
            "original_text": text,
            "target_language": target_lang,
            "transcreated_text": final_output,
            "pipeline_trace": {
                "intent": intent_result,
                "culture": culture_result
            }
        }

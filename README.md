# ResonanceEngine

**ResonanceEngine** is a generative AI backend designed for high-fidelity "Transcreation," prioritizing semantic impact over literal translation. It ensures that creative content—from marketing copy to poetry—retains its original "soul" and resonance across different languages.

## Vision

Startups and enterprises often struggle to scale their brand voice globally because standard translation tools (like Google Translate or even raw GPT-4) focus on *lexical fidelity* (word-for-word accuracy). **ResonanceEngine** focuses on *impact fidelity* (emotional and stylistic accuracy).

## Architecture

The engine employs a three-stage pipeline:

1.  **Intent Extraction**: Decodes sentiment, tone, and core message from the source text.
2.  **Cultural Retrieval**: Finds target-language equivalents for idioms, metaphors, and cultural references.
3.  **Constrained Generation**: Reconstructs the message in the target language while preserving specific stylistic elements (rhyme, meter, brevity).

## Key Features

1.  **Generative AI Backend**: Built on **FastAPI**, this engine orchestrates **ML models** to perform deep "Transcreation," favoring semantic and emotional impact over simple literal translation.
2.  **Modular Pipeline Architecture**: Features a robust **Python-based** three-stage design (Intent Extraction, Cultural Retrieval, Constrained Generation) that decouples meaning from form to preserve stylistic constraints like rhyme and tone.
3.  **Cloud-Native Deployment**: Fully containerized with **Docker** and ready for orchestration on **AWS EKS** or **ECS**, enabling scalable, high-availability inference pipelines.

## Project Structure

```
resonance-engine/
├── src/
│   ├── main.py                 # FastAPI Application entry point
│   ├── core/
│   │   ├── pipeline.py         # Orchestrates the 3-stage process
│   │   ├── intent.py           # Stage 1: Intent Extraction
│   │   ├── culture.py          # Stage 2: Cultural Retrieval
│   │   └── generation.py       # Stage 3: Constrained Generation
│   └── api/                    # API routes and models
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/resonance-engine.git
    cd resonance-engine
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the server:
    ```bash
    uvicorn src.main:app --reload
    ```

4.  Open your browser to `http://127.0.0.1:8000/docs` to test the API.

## Usage

Send a POST request to `/transcreate`:

```json
{
  "text": "It's raining cats and dogs",
  "target_language": "French",
  "context": "Casual conversation"
}
```

Response:

```json
{
  "original": "It's raining cats and dogs",
  "transcreated": "Il pleut des cordes",
  "meta": {
    "intent": "Emphasize heavy rain",
    "cultural_adaptation": "Idiom replacement",
    "tone": "Casual"
  }
}
```

## License

MIT

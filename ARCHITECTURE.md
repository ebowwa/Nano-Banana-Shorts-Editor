# Nano-Banana-Shorts-Editor Architecture Documentation

## Project Overview

Nano-Banana-Shorts-Editor is the **integration project** that orchestrates AI-powered video editing for marketing materials. This repository serves as the main application layer that combines two foundational libraries to create an automated video editing pipeline.

## System Architecture

### Repository Dependencies

```
Nano-Banana-Shorts-Editor (Main Application)
├── ai-proxy-core (AI Processing Layer)
│   ├── Gemini for video analysis
│   ├── Model management & routing
│   └── Unified AI interface
└── media-processor (Media Operations Layer)
    ├── Video frame extraction
    ├── Image processing & upscaling
    └── Format conversions
```

## Core Dependencies

### 1. ai-proxy-core (v0.4.40+)
**Repository**: `ebowwa/ai-proxy-core`
**Role**: AI abstraction and processing layer

**Key Features Used**:
- **Gemini Integration**: Video content analysis and decision making
- **Unified AI Interface**: Single client for multiple AI providers
- **Model Management**: Intelligent model selection and routing
- **Image Generation**: DALL-E integration for enhanced content creation
- **WebSocket Support**: Real-time AI interactions via Gemini Live

**Integration Points**:
```python
from ai_proxy_core import CompletionClient, GeminiLiveSession

# Video analysis
client = CompletionClient()
analysis = await client.create_completion(
    messages=[{"role": "user", "content": "Analyze this video for enhancement opportunities"}],
    model="gemini-1.5-flash"
)

# Real-time processing
session = GeminiLiveSession(api_key="...", enable_code_execution=True)
```

### 2. media-processor
**Repository**: `ebowwa/media-processor`
**Role**: Media processing and manipulation engine

**Key Features Used**:
- **Frame Extraction**: Extract frames from videos at specified intervals
- **AI Upscaling**: Enhance image quality using ONNX models
- **Format Conversion**: Handle various media format transformations
- **Batch Processing**: Process multiple files efficiently

**Integration Points**:
```python
from media_processor import VideoFrameExtractor, ImageUpscaler

# Extract frames for AI analysis
extractor = VideoFrameExtractor(frame_interval_seconds=1)
frames = extractor.extract_frames("input.mp4", "frames/")

# Enhance extracted frames
upscaler = ImageUpscaler(model_name="modelx4")
upscaler.process("frames/", "enhanced_frames/")
```

## Planned Workflow

### Phase 1: Video Upload & Preprocessing
1. User uploads source video
2. **media-processor** extracts frames at optimal intervals
3. Frames prepared for AI analysis

### Phase 2: AI Analysis & Decision Making
1. **ai-proxy-core** sends frames to Gemini for analysis
2. AI identifies:
   - Objects requiring effects/enhancements
   - Optimal moments for text overlays
   - Vector points for augmentation
   - Scene transitions and key moments

### Phase 3: Content Enhancement
1. **ai-proxy-core** generates overlay content, translations, effects
2. **media-processor** applies enhancements to identified frames
3. Upscaling and quality improvements applied

### Phase 4: Video Reconstruction
1. Enhanced frames reassembled into final video
2. Effects, text overlays, and enhancements applied
3. Output optimized for target platform (social media, marketing)

## Use Cases

### 1. Overlay Commentator Content
- AI identifies key moments for commentary
- Generates contextual text overlays
- Positions overlays optimally in frame

### 2. Multi-language Translations
- Extracts text from video frames
- Translates content using AI
- Replaces original text with translations

### 3. General Editor Functionality
- Automated scene detection
- Smart cropping and framing
- Color correction and enhancement

### 4. AR/MR Functionality
- Object detection and tracking
- 3D effect placement
- Augmented reality overlays

## Technical Implementation Strategy

### Data Flow
```
Video Input → Frame Extraction → AI Analysis → Enhancement Generation → Frame Processing → Video Output
     ↓              ↓                ↓                    ↓                   ↓              ↓
media-processor → media-processor → ai-proxy-core → ai-proxy-core → media-processor → Final Product
```

### Key Integration Patterns

1. **Async Processing Pipeline**: Leverage ai-proxy-core's async capabilities
2. **Batch Operations**: Use media-processor's batch processing for efficiency
3. **Model Selection**: Utilize ai-proxy-core's intelligent model routing
4. **Error Handling**: Implement robust error handling across both libraries

## Development Roadmap

### Phase 1: Foundation (Current)
- [x] ai-proxy-core: Production ready (v0.4.40)
- [x] media-processor: Complete CLI tool
- [ ] Integration layer architecture design

### Phase 2: Core Integration
- [ ] Implement video upload and preprocessing
- [ ] Integrate AI analysis pipeline
- [ ] Basic frame enhancement workflow

### Phase 3: Advanced Features
- [ ] Real-time processing with Gemini Live
- [ ] Multi-language support
- [ ] AR/MR functionality

### Phase 4: Production
- [ ] Performance optimization
- [ ] User interface development
- [ ] Deployment and scaling

## Benefits of This Architecture

### Separation of Concerns
- **ai-proxy-core**: Handles all AI operations and model management
- **media-processor**: Manages all media manipulation tasks
- **Nano-Banana-Shorts-Editor**: Orchestrates workflow and user experience

### Reusability
- Both dependency libraries can be used independently
- Modular design allows for easy testing and maintenance
- Clear interfaces between components

### Scalability
- AI processing can be scaled independently
- Media processing can be optimized separately
- Easy to add new AI providers or media formats

### Maintainability
- Each repository has focused responsibility
- Updates to AI capabilities don't affect media processing
- Clear dependency management and versioning

## Getting Started (Future)

Once implementation begins, the setup will involve:

```bash
# Install dependencies
pip install ai-proxy-core>=0.4.40
pip install media-processor

# Clone integration project
git clone https://github.com/ebowwa/Nano-Banana-Shorts-Editor.git
cd Nano-Banana-Shorts-Editor

# Install integration layer
pip install -e .
```

## Contributing

This project integrates two mature libraries:
- Contribute AI improvements to `ebowwa/ai-proxy-core`
- Contribute media processing features to `ebowwa/media-processor`
- Contribute integration and workflow improvements to this repository

---

*This architecture documentation will be updated as the integration project develops.*

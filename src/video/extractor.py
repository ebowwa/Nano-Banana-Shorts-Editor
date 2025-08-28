"""Mock VideoFrameExtractor for testing when media-processor is not available"""

import logging
import os
from pathlib import Path
from typing import List, Optional
import shutil

logger = logging.getLogger(__name__)

class VideoFrameExtractor:
    """Mock frame extractor that simulates video processing"""
    
    def __init__(self, frame_interval_seconds: int = 1, max_frames: int = 5000):
        self.frame_interval_seconds = frame_interval_seconds
        self.max_frames = max_frames
        logger.info(f"Initialized mock VideoFrameExtractor (interval: {frame_interval_seconds}s, max: {max_frames})")
    
    def extract_frames(self, video_path: str, output_dir: str, start_time: float = 0, end_time: Optional[float] = None) -> List[str]:
        """
        Mock frame extraction that creates placeholder frame files
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Simulate frame extraction
        num_frames = min(10, self.max_frames)  # Mock: extract 10 frames
        frame_paths = []
        
        video_name = Path(video_path).stem
        
        for i in range(1, num_frames + 1):
            frame_filename = f"{video_name}_frame{i}.jpg"
            frame_path = output_path / frame_filename
            
            # Create a placeholder frame (copy test image if exists, otherwise create empty file)
            test_frame = Path("output/frames/test_video/segment_0_text_overlay/test_video_frame1.jpg")
            if test_frame.exists():
                shutil.copy(test_frame, frame_path)
            else:
                frame_path.touch()
            
            frame_paths.append(str(frame_path))
        
        logger.info(f"Mock extracted {len(frame_paths)} frames to {output_dir}")
        return frame_paths
    
    def get_video_duration(self, video_path: str) -> float:
        """Mock: Return a fixed duration"""
        return 30.0  # 30 seconds mock duration
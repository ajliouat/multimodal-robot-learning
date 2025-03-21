import time
from src.core.vision_language.segmenter import Segmenter

def benchmark_segmentation():
    segmenter = Segmenter()
    start_time = time.time()
    segmenter.segment("sample_image.jpg")
    end_time = time.time()
    print(f"Inference time: {(end_time - start_time) * 1000:.2f} ms")

if __name__ == "__main__":
    benchmark_segmentation()
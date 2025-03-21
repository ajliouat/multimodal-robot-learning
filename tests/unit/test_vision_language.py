import torch
from src.core.vision_language.model import VisionLanguageModel

def test_vision_language_model():
    model = VisionLanguageModel()
    output = model.forward(torch.randint(0, 100, (32, 512)))
    assert output is not None

if __name__ == "__main__":
    test_vision_language_model()
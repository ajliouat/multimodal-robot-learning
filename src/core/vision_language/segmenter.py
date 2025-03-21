import torch
from segment_anything import SamPredictor, sam_model_registry

class Segmenter:
    def __init__(self, model_type="vit_h", checkpoint_path="models/sam/sam_vit_h_4b8939.pth"):
        self.model = sam_model_registry[model_type](checkpoint=checkpoint_path)
        self.predictor = SamPredictor(self.model)

    def segment(self, image):
        self.predictor.set_image(image)
        masks, _, _ = self.predictor.predict()
        return masks
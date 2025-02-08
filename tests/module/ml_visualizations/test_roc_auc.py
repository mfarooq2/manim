from manim import *
from manim.ml_visualizations.roc_auc import ROCAUCVisualization

class TestROCAUCVisualization(Scene):
    def construct(self):
        # Create an instance of the visualization
        visualization = ROCAUCVisualization()
        visualization.construct()

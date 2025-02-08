from manim import *
from manim.ml_visualizations.precision_recall import PrecisionRecallVisualization

class TestPrecisionRecallVisualization(Scene):
    def construct(self):
        # Create an instance of the visualization
        visualization = PrecisionRecallVisualization()
        visualization.construct()

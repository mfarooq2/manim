from manim import *
from manim.ml_visualizations.svm import SVMVisualization

class TestSVMVisualization(Scene):
    def construct(self):
        # Create an instance of the visualization
        visualization = SVMVisualization()
        visualization.construct()

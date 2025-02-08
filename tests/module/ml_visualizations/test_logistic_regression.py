from manim import *
from manim.ml_visualizations.logistic_regression import LogisticRegressionVisualization

class TestLogisticRegressionVisualization(Scene):
    def construct(self):
        # Create an instance of the visualization
        visualization = LogisticRegressionVisualization()
        visualization.construct()

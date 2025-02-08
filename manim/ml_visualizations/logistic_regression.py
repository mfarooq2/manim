from manim import *

class LogisticRegressionVisualization(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(x_range=[-3, 3], y_range=[-3, 3], axis_config={"include_numbers": True})
        self.add(axes)

        # Create data points
        data_points = [
            Dot(point=[x, y, 0], color=BLUE) for x, y in zip([1, 2, 3], [1, 2, 3])
        ]
        self.add(*data_points)
        self.play(
            *[
                Create(obj)
                for obj in data_points
            ]
        )
        # Calculate the decision boundary
        decision_boundary_func = lambda x: 1 / (1 + np.exp(-(x) ** 2))
        decision_boundary = axes.plot(decision_boundary_func, color=RED)
        self.play(Create(decision_boundary))
        # Create the logistic regression line
        regression_line = axes.plot(lambda x: 1 / (1 + np.exp(-(x) ** 2)), color=GREEN)
        self.play(Create(regression_line))

        # Create text labels
        text_labels = VGroup(
            Text("Class 1", color=BLUE).scale(0.5),
            Text("Class 2", color=GREEN).scale(0.5),
        ).arrange(DOWN)
        self.play(Write(text_labels))
        for label in text_labels:
            self.play(Create(label))

        # Create the regression line
        axes.plot(lambda x: 1 / (1 + np.exp(-(x) ** 2)), color=BLUE, stroke_width=0, fill_in_x_axis=True, is_line_graph=True)
        self.play(Create(axes.plot(lambda x: 1 / (1 + np.exp(-(x) ** 2)), color=BLUE, stroke_width=0, fill_in_x_axis=True, is_line_graph=True))
        
        self.wait()

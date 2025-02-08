from manim import *

class SVMVisualization(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(x_range=[-3, 3], y_range=[-3, 3], axis_config={"include_numbers": True})
        self.add(axes)

        # Create data points for the example
        data_points = [
            Dot(point=[x, y, 0], color=BLUE) for x, y in zip([1, 2, 3], [1, 2, 3])
        ]
        self.add(*data_points)
        self.play(*[Create(obj) for obj in data_points])

        # Create the decision boundary with a more complex function
        decision_boundary_func = lambda x: 0.5 * (np.sin(x) + 1)
        decision_boundary = axes.plot(decision_boundary_func, color=RED)
        self.play(Create(decision_boundary))

        # Create the SVM support vectors
        support_vector = Arrow(color=GREEN)
        self.play(Create(support_vector))
        support_vector_2 = Arrow(color=GREEN)
        self.play(Create(support_vector_2))

        # Add the title of the model
        title = Text("SVM Model", color=BLUE).scale(0.7)
        self.play(Write(title))
        self.add(title)
        
        # Create a text label
        label = Text("Decision Boundary", color=YELLOW).scale(0.7)
        self.play(Write(label))
        self.add(label)

        # Create the text label
        text_labels = VGroup(
            Text("Class 1", color=BLUE).scale(0.5),
            Text("Class 2", color=GREEN).scale(0.5),
        ).arrange(DOWN)
        self.play(Write(text_labels))
        for label in text_labels:
            self.play(Create(label))

        # Create the regression line
        regression_line_func = lambda x: 1 / (1 + np.exp(-(x) ** 2))
        axes.plot(regression_line_func, color=BLUE, stroke_width=0, fill_in_x_axis=True, is_line_graph=True)
        self.play(Create(axes.plot(regression_line_func, color=BLUE, stroke_width=0, fill_in_x_axis=True, is_line_graph=True))

        # Create the svm line
        svm_line = axes.plot(lambda x: 0.5 * (np.sin(x) + 1), color=GREEN)
        self.play(Create(svm_line))
        
        self.wait()

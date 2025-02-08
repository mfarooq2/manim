from manim import *

class PrecisionRecallVisualization(Scene):
    def construct(self):
        # Create a table to show the values
        table = Table(
            [["TP", "FP", "Precision", "Recall", "FN"], ["1", "0", "0.8", "0.5", "1"]],
            row_labels=[Text("True Positive"), Text("False Positive"), Text("False Negative")],
            col_labels=[Text("Precision"), Text("Recall"), Text("FN")],
            include_outer_lines=True,
        ).scale(0.7)
        self.play(Create(table))

        # Calculate the precision
        precision_formula = MathTex(r"\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}")
        self.play(Write(precision_formula))

        # Calculate the recall
        recall_formula = MathTex(r"\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}")
        self.play(Write(recall_formula))

        # Create data points
        data_points = [
            Dot(point=[x, y, 0], color=BLUE) for x, y in zip([1, 0, 0, 1], [0, 1, 1, 0])
        ]
        self.add(*data_points)
        self.play(
            *[
                Create(obj)
                for obj in data_points
            ]
        )
        # Create text labels
        text_labels = VGroup(
            Text("True Positive", color=BLUE).scale(0.5),
            Text("False Positive", color=RED).scale(0.5),
            Text("False Negative", color=YELLOW).scale(0.5),
        ).arrange(DOWN)
        self.play(Write(text_labels))
        for label in text_labels:
            self.play(Create(label))

        # Create the data set to show the precision and recall
        axes = Axes(x_range=[-3, 3], y_range=[-3, 3], axis_config={"include_numbers": True})
        self.add(axes)
        
        self.wait()

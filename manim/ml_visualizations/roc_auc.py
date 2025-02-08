from manim import *

class ROCAUCVisualization(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(x_range=[0, 1], y_range=[0, 1], axis_config={"include_numbers": True})
        self.add(axes)
        
        # Create the ROC curve
        roc_curve = axes.plot(lambda x: x**2, color=BLUE)
        self.play(Create(roc_curve))

        # Add the title to the curve
        title = Text("ROC Curve", color=BLUE).scale(0.7)
        self.add(title)
        self.play(Write(title))
        
        # Create text labels
        text_labels = VGroup(
            Text("True Positive", color=BLUE).scale(0.5),
            Text("False Positive", color=RED).scale(0.5),
            Text("False Negative", color=YELLOW).scale(0.5),
        ).arrange(DOWN)
        self.play(Write(text_labels))
        for label in text_labels:
            self.play(Create(label))

        # Create the AUC area
        auc_area = axes.get_area(x_range=[0, 1], y_range=[0, 1], color=GREEN)
        self.play(Create(auc_area))

        # Add the title to the AUC area
        auc_title = Text("AUC", color=GREEN).scale(0.7)
        self.add(auc_title)
        self.play(Create(auc_title))

        # Add the formula
        formula = MathTex(r"AUC = \int_0^1 ROC Curve")
        self.add(formula)
        self.play(Write(formula))

        self.wait()

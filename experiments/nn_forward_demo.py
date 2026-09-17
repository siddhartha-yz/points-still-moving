"""A single, continuous Manim visualization of one neural-network forward pass.

The numerical constants in this file are deliberately the sole source of truth
for the grid, point cloud, node values, and output probabilities.
"""

from __future__ import annotations

import numpy as np
from manim import (
    AnimationGroup,
    BLACK,
    BLUE,
    BLUE_A,
    BLUE_D,
    BLUE_E,
    Circle,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    Flash,
    GrowFromCenter,
    LaggedStart,
    Line,
    MovingCameraScene,
    ORIGIN,
    RIGHT,
    LEFT,
    Succession,
    Transform,
    UP,
    DOWN,
    SurroundingRectangle,
    Text,
    VGroup,
    VMobject,
    ValueTracker,
    Wait,
    WHITE,
    YELLOW,
    YELLOW_A,
    YELLOW_D,
    YELLOW_E,
    config,
    interpolate_color,
    linear,
    smooth,
)


# Delivery settings.  The render command may still choose the quality preset,
# but these retain the requested dimensions and frame rate in all presets.
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60
config.background_color = BLACK


# One shared forward-pass definition for every visual component.
W1 = np.array([[1.15, 0.75], [-0.35, 1.10]], dtype=float)
B1 = np.array([0.15, -0.10], dtype=float)
W2 = np.array([[1.10, -0.65], [-0.75, 1.20]], dtype=float)
B2 = np.array([-0.15, 0.10], dtype=float)
SAMPLE_X = np.array([1.25, 0.60], dtype=float)


def softmax(values: np.ndarray) -> np.ndarray:
    shifted = values - np.max(values)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials)


def forward(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    z = W1 @ x + B1
    h = np.tanh(z)
    p = softmax(W2 @ h + B2)
    return z, h, p


SAMPLE_Z, SAMPLE_H, SAMPLE_P = forward(SAMPLE_X)


class NeuralNetworkForwardDemo(MovingCameraScene):
    """Approximately ten seconds of continuous 2D-to-network visualization."""

    grid_color = BLUE_E
    positive_color = BLUE_A
    negative_color = YELLOW_A
    node_radius = 0.31

    def construct(self) -> None:
        affine_progress = ValueTracker(0.0)
        nonlinear_progress = ValueTracker(0.0)
        field_scale = ValueTracker(1.0)
        field_shift = ValueTracker(0.0)
        tanh_camera_view = self.camera.frame.copy().scale(0.64)
        network_camera_view = self.camera.frame.copy().scale(1.035).shift(RIGHT * 0.22)

        def map_point(point: np.ndarray) -> np.ndarray:
            """Map a source coordinate through the same staged math as the scene."""
            x = np.asarray(point, dtype=float)
            z = W1 @ x + B1
            affine = (1 - affine_progress.get_value()) * x + affine_progress.get_value() * z
            h = np.tanh(affine)
            mapped = (1 - nonlinear_progress.get_value()) * affine + nonlinear_progress.get_value() * h
            return np.array(
                [
                    field_scale.get_value() * mapped[0] + field_shift.get_value(),
                    field_scale.get_value() * mapped[1],
                    0.0,
                ]
            )

        def make_curve(source_points: list[np.ndarray], accent: bool = False) -> VMobject:
            curve = VMobject()

            def redraw(mobject: VMobject) -> None:
                # Corner paths remain open paths (first point is not repeated);
                # force transparent fill after every point rebuild so warped
                # tanh curves can never fill their enclosed interiors.
                mobject.set_points_as_corners([map_point(point) for point in source_points])
                mobject.set_fill(opacity=0)

            redraw(curve)
            curve.add_updater(redraw)
            curve.set_fill(opacity=0)
            curve.set_stroke(
                YELLOW_D if accent else self.grid_color,
                width=1.8 if accent else 1.05,
                opacity=0.68 if accent else 0.42,
            )
            return curve

        # A coordinate grid is made from source-coordinate curves.  Therefore
        # both the affine stage and tanh stage act on every grid location.
        domain = np.linspace(-2.85, 2.85, 27)
        verticals = VGroup(
            *[
                make_curve([np.array([constant, y]) for y in domain], accent=abs(constant) < 0.01)
                for constant in np.arange(-2.8, 2.81, 0.4)
            ]
        )
        horizontals = VGroup(
            *[
                make_curve([np.array([x, constant]) for x in domain], accent=abs(constant) < 0.01)
                for constant in np.arange(-2.8, 2.81, 0.4)
            ]
        )
        grid = VGroup(verticals, horizontals)

        # Two source groups retain their original colors throughout. SAMPLE_X
        # belongs to the blue group and is also the highlighted sample later.
        blue_points = np.array(
            [
                SAMPLE_X,
                [0.94, 0.88],
                [1.48, 0.28],
                [0.75, 0.12],
                [1.68, 0.78],
                [0.52, 0.67],
                [1.07, 1.20],
                [1.75, 0.45],
                [0.83, 0.42],
                [1.36, 0.98],
                [0.42, 0.34],
                [1.50, 1.08],
            ],
            dtype=float,
        )
        yellow_points = np.array(
            [
                [-1.38, -0.90],
                [-0.92, -1.34],
                [-1.76, -0.42],
                [-0.55, -0.74],
                [-1.18, -0.24],
                [-2.03, -1.08],
                [-0.74, -0.28],
                [-1.62, -1.46],
                [-1.09, -0.54],
                [-2.20, -0.64],
                [-0.42, -1.08],
                [-1.83, -0.10],
            ],
            dtype=float,
        )

        def make_dot(point: np.ndarray, color) -> Dot:
            dot = Dot(map_point(point), radius=0.075, color=color)
            dot.set_fill(color, opacity=0.96)
            dot.add_updater(lambda mobject, p=point: mobject.move_to(map_point(p)))
            return dot

        blue_dots = VGroup(*[make_dot(point, BLUE) for point in blue_points])
        yellow_dots = VGroup(*[make_dot(point, YELLOW) for point in yellow_points])
        sample_dot = blue_dots[0]
        point_clouds = VGroup(blue_dots, yellow_dots)

        # Network geometry: a clean 2 -> 2 -> 2 fully connected graph.
        layer_positions = {
            # The final output labels extend to the right of this layer, so
            # the entire graph is deliberately left of the composition edge.
            "input": [np.array([1.55, 1.05, 0]), np.array([1.55, -1.05, 0])],
            "hidden": [np.array([3.55, 1.05, 0]), np.array([3.55, -1.05, 0])],
            "output": [np.array([5.40, 1.05, 0]), np.array([5.40, -1.05, 0])],
        }
        nodes = {
            layer: VGroup(
                *[
                    Circle(radius=self.node_radius)
                    .move_to(position)
                    .set_stroke(BLUE_D, width=2.2, opacity=0.85)
                    .set_fill(BLACK, opacity=0.95)
                    for position in positions
                ]
            )
            for layer, positions in layer_positions.items()
        }
        input_symbols = VGroup(
            *[
                Text(symbol, font_size=27, color=WHITE).move_to(node.get_center())
                for symbol, node in zip(("x₁", "x₂"), nodes["input"])
            ]
        )
        hidden_symbols = VGroup(
            *[
                Text(symbol, font_size=27, color=WHITE).move_to(node.get_center())
                for symbol, node in zip(("h₁", "h₂"), nodes["hidden"])
            ]
        )
        output_symbols = VGroup(
            *[
                Text(symbol, font_size=27, color=WHITE).move_to(node.get_center())
                for symbol, node in zip(("p₁", "p₂"), nodes["output"])
            ]
        )
        symbols_by_layer = {
            "input": input_symbols,
            "hidden": hidden_symbols,
            "output": output_symbols,
        }

        def edge_color(weight: float):
            return BLUE_D if weight >= 0 else YELLOW_D

        input_hidden_edges = []
        hidden_output_edges = []
        for out_idx, hidden_node in enumerate(nodes["hidden"]):
            for in_idx, input_node in enumerate(nodes["input"]):
                input_hidden_edges.append(
                    (
                        Line(
                            input_node.get_center(),
                            hidden_node.get_center(),
                            buff=self.node_radius,
                        ).set_stroke(edge_color(W1[out_idx, in_idx]), width=2.4, opacity=0.52),
                        W1[out_idx, in_idx],
                    )
                )
        for out_idx, output_node in enumerate(nodes["output"]):
            for hidden_idx, hidden_node in enumerate(nodes["hidden"]):
                hidden_output_edges.append(
                    (
                        Line(
                            hidden_node.get_center(),
                            output_node.get_center(),
                            buff=self.node_radius,
                        ).set_stroke(edge_color(W2[out_idx, hidden_idx]), width=2.4, opacity=0.52),
                        W2[out_idx, hidden_idx],
                    )
                )
        network_edges = VGroup(
            *[edge for edge, _ in input_hidden_edges],
            *[edge for edge, _ in hidden_output_edges],
        )
        network = VGroup(
            network_edges,
            nodes["input"],
            nodes["hidden"],
            nodes["output"],
            input_symbols,
            hidden_symbols,
            output_symbols,
        )

        def value_label(text: str, target, direction, color) -> Text:
            return Text(text, font_size=22, color=color).next_to(target, direction, buff=0.20)

        sample_label = Text("x = [1.25, 0.60]", font_size=22, color=WHITE)
        input_values = VGroup(
            value_label(f"x₁ = {SAMPLE_X[0]:+.2f}", nodes["input"][0], LEFT, BLUE_A),
            value_label(f"x₂ = {SAMPLE_X[1]:+.2f}", nodes["input"][1], LEFT, BLUE_A),
        )
        hidden_values = VGroup(
            # This value sits above and left of h₁, clear of its descending
            # outgoing edge and the softmax equation over the output layer.
            Text(f"h₁ = {SAMPLE_H[0]:+.2f}", font_size=22, color=BLUE_A).move_to(
                nodes["hidden"][0].get_center() + UP * 0.64 + LEFT * 0.42
            ),
            value_label(f"h₂ = {SAMPLE_H[1]:+.2f}", nodes["hidden"][1], DOWN, YELLOW_A),
        )
        output_values = VGroup(
            value_label(f"p₁ = {SAMPLE_P[0]:.2f}", nodes["output"][0], RIGHT, BLUE_A),
            value_label(f"p₂ = {SAMPLE_P[1]:.2f}", nodes["output"][1], RIGHT, BLUE_A),
        )
        affine_label = Text("z = W₁x + b₁", font_size=29, color=WHITE).to_edge(UP, buff=0.42)
        tanh_label = Text("h = tanh(z)", font_size=29, color=WHITE).to_edge(UP, buff=0.42)
        softmax_label = Text("p = softmax(W₂h + b₂)", font_size=22, color=WHITE)
        # Keep the output equation in its own high-right visual lane, away
        # from the h₁ activation label above the hidden layer.
        softmax_label.move_to(nodes["output"].get_center() + UP * 2.25 + RIGHT * 0.25)

        def activation_intensity(value: float) -> float:
            return 0.32 + 0.68 * min(abs(value), 1.0)

        def activation_fill(value: float, output: bool = False):
            base = BLUE_A if output or value >= 0 else YELLOW_A
            return interpolate_color(BLACK, base, activation_intensity(value))

        def activation_symbol_color(value: float, output: bool = False):
            # A white glyph vanishes on a bright fill.  Flip only bright nodes
            # to black, retaining white symbols on the deliberately dim ones.
            return BLACK if activation_intensity(value) >= 0.48 else WHITE

        def light_nodes(layer: str, values: np.ndarray, output: bool = False):
            return AnimationGroup(
                *[
                    AnimationGroup(
                        node.animate.set_fill(activation_fill(value, output), opacity=0.98).set_stroke(
                            activation_fill(value, output), width=3.7, opacity=1.0
                        ),
                        symbol.animate.set_color(activation_symbol_color(value, output)),
                    )
                    for node, symbol, value in zip(nodes[layer], symbols_by_layer[layer], values)
                ],
                lag_ratio=0.16,
            )

        def send_pulses(edge_data: list[tuple[Line, float]], run_time: float) -> None:
            pulses = VGroup(
                *[
                    Dot(edge.get_start(), radius=0.075, color=edge_color(weight)).set_fill(
                        edge_color(weight), opacity=min(1.0, 0.50 + abs(weight) * 0.32)
                    )
                    for edge, weight in edge_data
                ]
            )
            self.add(pulses)
            self.play(
                LaggedStart(
                    *[
                        pulse.animate.move_to(edge.get_end())
                        for pulse, (edge, _) in zip(pulses, edge_data)
                    ],
                    lag_ratio=0.13,
                ),
                run_time=run_time,
                rate_func=linear,
            )
            self.remove(pulses)

        # 0.0–1.0s — the full, stroke-only grid is visible in frame zero.
        self.add(grid)
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in point_clouds], lag_ratio=0.10),
            run_time=1.00,
            rate_func=smooth,
        )

        # 1.0–2.6s — one affine map acts on every source point and curve.
        self.play(
            affine_progress.animate.set_value(1.0),
            FadeIn(affine_label),
            run_time=1.60,
            rate_func=smooth,
        )

        # 2.6–4.2s — tanh bends and compresses the affine geometry continuously.
        # The camera zoom begins only after tanh has mostly compressed the
        # initially wide affine map, keeping the whole warped wireframe visible.
        self.play(
            nonlinear_progress.animate.set_value(1.0),
            # Sequential fades prevent two equations or intermediate glyph
            # morphs from occupying the title lane at the same time.
            Succession(
                FadeOut(affine_label, run_time=0.20),
                FadeIn(tanh_label, run_time=0.20),
                Wait(1.20),
            ),
            Succession(
                Wait(0.94),
                Transform(self.camera.frame, tanh_camera_view, run_time=0.66),
            ),
            run_time=1.60,
            rate_func=smooth,
        )

        # 4.2–5.4s — recompose to make room for the revealed network.
        self.play(
            field_scale.animate.set_value(1.10),
            field_shift.animate.set_value(-2.65),
            FadeOut(tanh_label),
            FadeIn(network),
            Transform(self.camera.frame, network_camera_view),
            run_time=1.20,
            rate_func=smooth,
        )

        # 5.4–10.0s — a single sample propagates through the fixed, untrained network.
        highlight = SurroundingRectangle(sample_dot, color=YELLOW, buff=0.13, corner_radius=0.08)
        highlight.set_stroke(width=2.7)
        # Place the sample value below-left of the enlarged field: it clears
        # both point clouds and the x₂ value that starts the network pass.
        sample_label.next_to(highlight, DOWN, buff=1.35).shift(LEFT * 0.35)
        self.play(
            Create(highlight),
            Flash(sample_dot.get_center(), color=YELLOW, flash_radius=0.37, line_length=0.11),
            FadeIn(sample_label),
            FadeIn(input_values),
            light_nodes("input", SAMPLE_X),
            run_time=0.50,
            rate_func=smooth,
        )

        send_pulses(input_hidden_edges, run_time=0.65)
        self.play(
            light_nodes("hidden", SAMPLE_H),
            FadeIn(hidden_values),
            run_time=0.65,
            rate_func=smooth,
        )

        send_pulses(hidden_output_edges, run_time=0.75)
        self.play(
            light_nodes("output", SAMPLE_P, output=True),
            FadeIn(output_values),
            FadeIn(softmax_label),
            run_time=0.65,
            rate_func=smooth,
        )

        winning_index = int(np.argmax(SAMPLE_P))
        winning_node = nodes["output"][winning_index]
        winner_box = SurroundingRectangle(winning_node, color=YELLOW, buff=0.13, corner_radius=0.08)
        winner_box.set_stroke(width=3.1)
        self.play(
            Create(winner_box),
            winning_node.animate.set_fill(YELLOW, opacity=0.98).set_stroke(YELLOW, width=4.2),
            self.camera.frame.animate.scale(0.965).shift(RIGHT * 0.18),
            run_time=0.70,
            rate_func=smooth,
        )
        self.wait(0.70)

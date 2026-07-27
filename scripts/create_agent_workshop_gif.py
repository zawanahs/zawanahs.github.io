from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def ease(value: float) -> float:
    value = clamp(value)
    return value * value * (3.0 - 2.0 * value)


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: create_agent_workshop_gif.py INPUT OUTPUT")

    source_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    source = Image.open(source_path).convert("RGBA")
    target_width = 960
    target_height = round(source.height * target_width / source.width)
    base = source.resize((target_width, target_height), Image.Resampling.LANCZOS)

    sx = target_width / source.width
    sy = target_height / source.height

    def point(x: float, y: float) -> tuple[int, int]:
        return round(x * sx), round(y * sy)

    def box(x1: float, y1: float, x2: float, y2: float) -> tuple[int, int, int, int]:
        left, top = point(x1, y1)
        right, bottom = point(x2, y2)
        return left, top, right, bottom

    frame_count = 48
    duration_ms = 100
    frames: list[Image.Image] = []

    for index in range(frame_count):
        t = index / frame_count
        slow_pulse = (1.0 + math.sin(2.0 * math.pi * t)) / 2.0
        monitor_pulse = (1.0 + math.sin(4.0 * math.pi * t + 0.7)) / 2.0
        fact_pulse = (1.0 + math.sin(2.0 * math.pi * t + 1.4)) / 2.0

        frame = base.copy()

        glow = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow, "RGBA")

        lamp_x, lamp_y = point(148, 320)
        lamp_radius = round(84 * sx)
        glow_draw.ellipse(
            (lamp_x - lamp_radius, lamp_y - lamp_radius, lamp_x + lamp_radius, lamp_y + lamp_radius),
            fill=(255, 207, 126, round(12 + 18 * slow_pulse)),
        )

        fact_x, fact_y = point(576, 255)
        fact_radius = round((46 + 5 * fact_pulse) * sx)
        glow_draw.ellipse(
            (fact_x - fact_radius, fact_y - fact_radius, fact_x + fact_radius, fact_y + fact_radius),
            fill=(255, 197, 77, round(10 + 28 * fact_pulse)),
        )

        monitor_alpha = round(10 + 20 * monitor_pulse)
        glow_draw.rounded_rectangle(box(1221, 292, 1372, 389), radius=round(7 * sx), fill=(124, 179, 150, monitor_alpha))
        glow_draw.rounded_rectangle(box(1495, 291, 1640, 389), radius=round(7 * sx), fill=(116, 171, 142, round(10 + 18 * (1.0 - monitor_pulse))))

        glow = glow.filter(ImageFilter.GaussianBlur(radius=max(2, round(10 * sx))))
        frame = Image.alpha_composite(frame, glow)

        detail = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(detail, "RGBA")

        board_cells = [
            (977, 326, 997, 344),
            (1008, 326, 1028, 344),
            (1039, 326, 1059, 344),
            (977, 354, 997, 372),
            (1008, 354, 1028, 372),
            (1039, 354, 1059, 372),
        ]
        active_cell = int(t * len(board_cells)) % len(board_cells)
        draw.rounded_rectangle(box(*board_cells[active_cell]), radius=max(1, round(3 * sx)), fill=(77, 140, 113, 90))

        poker_dot_x = 1264 + 52 * ((math.sin(2.0 * math.pi * t) + 1.0) / 2.0)
        poker_dot_y = 370
        dot_x, dot_y = point(poker_dot_x, poker_dot_y)
        dot_radius = max(2, round(4 * sx))
        draw.ellipse((dot_x - dot_radius, dot_y - dot_radius, dot_x + dot_radius, dot_y + dot_radius), fill=(239, 203, 137, 180))

        chess_positions = [(1531, 336), (1550, 336), (1568, 352), (1586, 352)]
        chess_x, chess_y = point(*chess_positions[int(t * len(chess_positions)) % len(chess_positions)])
        square = max(3, round(7 * sx))
        draw.rectangle((chess_x - square, chess_y - square, chess_x + square, chess_y + square), fill=(185, 106, 82, 80))

        sparkle_alpha = round(70 + 150 * fact_pulse)
        for dx, dy in [(-34, -10), (31, -18), (26, 28)]:
            cx, cy = point(576 + dx, 255 + dy)
            arm = max(2, round(6 * sx))
            draw.line((cx - arm, cy, cx + arm, cy), fill=(232, 166, 65, sparkle_alpha), width=max(1, round(2 * sx)))
            draw.line((cx, cy - arm, cx, cy + arm), fill=(232, 166, 65, sparkle_alpha), width=max(1, round(2 * sx)))

        completion = ease((t - 0.58) / 0.16) * (1.0 - ease((t - 0.88) / 0.1))
        check_alpha = round(220 * completion)
        if check_alpha:
            p1 = point(861, 414)
            p2 = point(870, 423)
            p3 = point(887, 400)
            draw.line((p1, p2, p3), fill=(55, 122, 91, check_alpha), width=max(2, round(4 * sx)), joint="curve")

        frame = Image.alpha_composite(frame, detail).convert("RGB")
        frames.append(frame)

    palette = frames[0].quantize(colors=160, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    gif_frames = [
        frame.quantize(palette=palette, dither=Image.Dither.NONE)
        for frame in frames
    ]

    gif_frames[0].save(
        output_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
        disposal=1,
    )


if __name__ == "__main__":
    main()

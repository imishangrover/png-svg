import svgwrite

def save_svg(paths, output_path, width=1000, height=1000):
    dwg = svgwrite.Drawing(
        filename=str(output_path),
        size=(f"{width}px", f"{height}px"),
        viewBox=f"0 0 {width} {height}"
    )

    for curve in paths:
        start = curve.start_point
        d = f"M {start.x} {start.y} "

        for segment in curve:
            if segment.is_corner:
                d += f"L {segment.c.x} {segment.c.y} "
            else:
                d += (
                    f"C {segment.c1.x} {segment.c1.y} "
                    f"{segment.c2.x} {segment.c2.y} "
                    f"{segment.end_point.x} {segment.end_point.y} "
                )

        d += "Z"

        dwg.add(
            dwg.path(
                d=d,
                fill="black",
                stroke="none"
            )
        )

    dwg.save()

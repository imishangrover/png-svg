import potrace

def vectorize_bitmap(bw_image):
    bitmap = potrace.Bitmap(bw_image)

    path = bitmap.trace(
        turdsize=10,     # remove small specks
        alphamax=1.0,    # curve smoothness
        opticurve=True  # optimize Bezier curves
    )

    return path

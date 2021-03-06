def make_grid(width, height):
    """
    Create a grid that will hold all of the titles
    for a boggle game
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)}
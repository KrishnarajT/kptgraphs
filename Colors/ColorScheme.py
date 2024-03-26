class ColorScheme:
    """Contains color scheme data."""

    def __init__(self, name, primary, secondary, accent, background, text) -> None:
        self.primary = primary
        self.secondary = secondary
        self.accent = accent
        self.background = background
        self.text = text
        self.name = name
        

    def __str__(self) -> str:
        return f"{self.name} color scheme"

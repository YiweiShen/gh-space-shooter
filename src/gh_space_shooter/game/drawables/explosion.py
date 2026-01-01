"""Explosion effects for bullet hits and enemy destruction."""

import math
import random
from typing import TYPE_CHECKING, Literal

from PIL import ImageDraw

from .drawable import Drawable

if TYPE_CHECKING:
    from ..game_state import GameState
    from ..render_context import RenderContext


class Explosion(Drawable):
    """Particle explosion effect that expands and fades out."""

    def __init__(self, x: float, y: float, size: Literal["small", "large"], game_state: "GameState"):
        """
        Initialize an explosion.

        Args:
            x: X position (week, 0-51)
            y: Y position (day, 0-6)
            size: "small" for bullet hits, "large" for enemy destruction
            game_state: Reference to game state for self-removal
        """
        self.x = x
        self.y = y
        self.game_state = game_state
        self.frame = 0
        self.max_frames = 6 if size == "small" else 20
        self.max_radius = 10 if size == "small" else 20
        self.particle_count = 4 if size == "small" else 8
        # Generate random angles for each particle
        self.particle_angles = [random.uniform(0, 2 * math.pi) for _ in range(self.particle_count)]

    def animate(self) -> None:
        """Progress the explosion animation and remove when complete."""
        self.frame += 1
        if self.frame >= self.max_frames:
            self.game_state.explosions.remove(self)

    def draw(self, draw: ImageDraw.ImageDraw, context: "RenderContext") -> None:
        """Draw expanding particle explosion with fade effect."""
        # Calculate animation progress (0 to 1)
        progress = self.frame / self.max_frames
        fade = 1 - progress  # Fade out as animation progresses

        # Get center position
        center_x, center_y = context.get_cell_position(self.x, self.y)
        center_x += context.cell_size // 2
        center_y += context.cell_size // 2

        # Draw expanding particles in random directions
        for i in range(self.particle_count):
            distance = progress * self.max_radius
            angle = self.particle_angles[i]

            # Particle position using random angle
            px = int(center_x + distance * math.cos(angle))
            py = int(center_y + distance * math.sin(angle))

            # Particle size decreases as it expands
            particle_size = int((1 - progress * 0.5) * 3) + 1

            draw.rectangle(
                [px - particle_size, py - particle_size,
                 px + particle_size, py + particle_size],
                fill=(*context.bullet_color, int(255 * fade))
            )

"""
Configuration file for paths and constants used across the project.

Defines:
- Data directory location relative to the project root
- Paths to specific text files for analysis
- Any shared constants like plot styles

All paths are resolved using pathlib for cross-platform compatibility.
"""

from pathlib import Path

# Get the project root by going up two levels from src/config.py
DATA_DIR = Path(__file__).parent.parent / "data"

# Paths to text files
BASKERVILES_PATH = DATA_DIR / "doyle_baskervilles.txt"
WAR_WORLDS_PATH = DATA_DIR / "wells_war_worlds.txt"
LOST_WORLD_PATH = DATA_DIR / "lost_world.txt"

# Constants for plot visualization
LINE_STYLES = ["-", ":", "--"]

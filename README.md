# 15 Puzzle

A minimal implementation of the classic 15 Puzzle built with Python and raylib via `pyray`.  
The project focuses on clarity, deterministic layout, and straightforward rendering logic.

<img width="488" height="520" alt="image" src="https://github.com/user-attachments/assets/8b4296a7-e054-4c21-8e27-a9fba1c9a2e4" />

## Overview

This project implements:

- 4×4 sliding puzzle grid  
- Mouse interaction  
- Shuffle logic  
- Win state detection  
- Simple rendering loop  
- Optional FPS display  

Architecture is intentionally simple:  
- `Card` — UI + state  
- Stateless helper functions for puzzle logic  
- Single render loop  

---

## Requirements

- Python 3.9+  
- `pyray`  
- System installation of `raylib`  

Install dependency:  
pip install pyray  

If required (macOS):  
brew install raylib  

---

## Run

python main.py  

---

## Controls

- Move tile — Left mouse click  
- Shuffle — S  
- Restart after victory — Mouse click  

---

## Rendering Model

The game uses a standard game loop: input → state mutation → draw → repeat  

FPS locking can be enabled via `set_target_fps(60)` or disabled with `set_target_fps(0)`  

## Game Logic

- The empty tile is represented by ""  
- Movement is allowed only for adjacent tiles  
- Victory condition: tiles 1–15 are ordered and the empty tile is last  

## Design Notes

- No global mutation outside the main loop  
- Rectangle-based layout  
- No physics, no animation  
- Deterministic board generation  
- Lightweight dependency surface  

## Possible Improvements

- Solvability validation for shuffle  
- Move counter  
- Timer  
- Animation transitions  
- Adaptive layout  
- State isolation (MVC-like separation)  

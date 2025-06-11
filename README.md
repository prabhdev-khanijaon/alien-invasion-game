# 🚀 Alien Invasion: A Pygame-Based Project

**Alien Invasion** is a 2D arcade-style shooter built with Python’s `pygame` library. Control a rocket ship, shoot down waves of alien fleets, and survive as the difficulty increases with each level. The game demonstrates core concepts in object-oriented programming, game loop design, real-time data tracking, and basic data persistence.

---

## 🎮 Game Overview

* Move your ship left and right to dodge and destroy incoming alien fleets.
* Shoot down aliens before they reach the bottom of the screen or collide with your ship.
* Track your score, levels, and remaining ships in real time.
* High scores are saved across sessions using a JSON file.
* Bonus: Includes a **Sideways Shooter** variation with a horizontal layout and altered gameplay.

---

## 🧠 Skills Demonstrated

* **Object-Oriented Design**: Cleanly structured classes for ships, bullets, aliens, and game logic.
* **Data Handling**: Tracks high scores using JSON for persistence.
* **Real-Time UI**: Live score, level, and ship count displayed with in-game HUD.
* **Problem Solving**: Game mechanics designed and debugged through hands-on development.

---

## ✨ Key Features

* 🛸 **Alien Fleet Behavior**: Fleet movement, descent upon edge collision, and level progression.
* 🚀 **Ship Control & Firing**: Smooth player movement and bullet firing mechanics.
* 📊 **Live Scoreboard**: Real-time display of scores, levels, and ships remaining.
* 💾 **High Score System**: Persistent high score tracking between sessions.
* 🔄 **Bonus Version**: “Sideways Shooter” with alternative screen orientation and mechanics.

---

## 🧪 Future Improvements

* 👾 Add new alien types with varied behaviors or boss levels.
* 🔋 Introduce power-ups (shields, rapid-fire, invincibility).
* 🤝 Implement multiplayer mode for co-op or PvP gameplay.

---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alien-invasion.git
cd alien-invasion
```

### 2. Install Dependencies

```bash
pip install pygame
```

### 3. Run the Game

```bash
python alien_invasion.py
```

---

## 🎮 Controls

| Key      | Action               |
| -------- | -------------------- |
| ⬅️ / ➡️  | Move ship left/right |
| Spacebar | Fire bullet          |
| P        | Start/resume game    |
| Q        | Quit game            |

---

## 📁 Project Structure (Optional Section)

```
alien-invasion/
│
├── alien_invasion.py         # Main game file
├── settings.py               # Game settings
├── ship.py                   # Player ship class
├── alien.py                  # Alien class
├── bullet.py                 # Bullet logic
├── game_stats.py             # Score & state tracking
├── scoreboard.py             # Displaying HUD
├── button.py                 # Start/Play Again button
├── sideways_shooter.py       # Bonus sideways version
└── high_score.json           # Saved high scores
```

---

## 📌 Notes

* Built with Python 3.x and Pygame
* Great starter project for learning game loops, event handling, and class structure in Python.

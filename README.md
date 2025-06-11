# 🚀 Alien Invasion: A Pygame-Based Project

**Alien Invasion** is a 2D arcade-style shooter built with Python’s `pygame` library.  
Control a rocket ship, shoot down waves of alien fleets, and survive as the difficulty increases with each level.  
This project demonstrates core concepts in object-oriented programming, game loop design, real-time data tracking, and data persistence.

---

## 🎮 Game Overview

- Move your ship left and right to dodge and destroy incoming alien fleets.
- Shoot down aliens before they reach the bottom of the screen or collide with your ship.
- Track your score, levels, and remaining ships in real time.
- High scores are saved across sessions using a JSON file.
- Bonus: Includes a **Sideways Shooter** variation with horizontal gameplay and different difficulty logic.

---

## 🧠 Skills Demonstrated

- **Object-Oriented Design**: Modular classes for ship, alien, bullet, scoreboard, and more.
- **Data Handling**: High score saved using `JSON` for persistence across sessions.
- **Real-Time Tracking**: Dynamic scoreboard displaying live score, level, and remaining lives.
- **Problem Solving**: Game mechanics designed and debugged through hands-on development.

---

## ✨ Key Features

- 🛸 **Alien Fleet Behavior**: Fleets move horizontally and descend when hitting screen edges.
- 🚀 **Ship Control & Firing**: Smooth horizontal movement and projectile-based shooting.
- 📊 **Live Scoreboard**: Real-time display of score, level, and remaining ships.
- 💾 **High Score System**: Persistent high score saved between runs.
- 🔄 **Bonus Game Mode**: *Sideways Shooter* offers a horizontal layout with altered dynamics.

---

## 🧪 Future Improvements

- 👾 Add varied alien types and boss battles
- 🔋 Introduce power-ups (e.g., shields, rapid fire, invincibility)
- 🤝 Implement a multiplayer mode (co-op or competitive)

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alien-invasion.git
cd alien-invasion
````

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
| Spacebar | Fire bullets         |
| `P`      | Start or resume game |
| `Q`      | Quit the game        |

---

## 📁 Project Structure

```
alien-invasion/
│
├── alien_invasion.py         # Main game loop
├── settings.py               # Game configuration
├── ship.py                   # Ship logic
├── alien.py                  # Alien behavior
├── bullet.py                 # Bullet logic
├── game_stats.py             # Game state and stats
├── scoreboard.py             # Scoreboard display
├── button.py                 # Play/Restart button
├── sideways_shooter.py       # Bonus version
└── high_score.json           # Persistent high score data
```

---

## 📝 Notes

* Built with **Python 3.x** and **Pygame**
* Designed as a hands-on way to learn **game development**, **Python OOP**, and **real-time logic**
* Also demonstrates fundamental concepts useful for data analysts (tracking, persistence, UI feedback)

---

Feel free to fork, star ⭐, or contribute!

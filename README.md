# Slot-Machine
# 🎰 Slot Machine Simulator with RTP Analysis

This project implements a slot machine in Python and evaluates its long-term behavior using Monte Carlo simulation.
The primary goal of the project is not gameplay, but to study how payout rules, penalties, and outcome frequencies affect **Return to Player (RTP)** in a probabilistic system.

The project consists of:
- a playable slot machine game
- a simulation mode that runs thousands of spins automatically
- RTP calculation and tuning based on real outcomes

---

## 🚀 Features

- 🎰 Slot machine with multiple symbols (🍒 🫐 🔔 ⭐ 7️⃣ 💣)
- 💥 Bomb mechanics with penalties
- 🏆 Multiple win types:
  - Double Slash (two matching symbols)
  - Triple normal symbols
  - Triple ⭐
  - Triple 7️⃣
- 🤖 Simulation mode to calculate RTP over large numbers of spins
- 📊 RTP tuning through experimentation

---

## 🧠 What is RTP?

**RTP (Return to Player)** is the percentage of total money bet that is returned to the player over a long period of time.

Example:
- RTP = 94%
- For every 100 units bet, the player gets back ~94 units
- The remaining ~6 units is the house edge

RTP is a *long-term statistical measure*, not a guarantee for individual sessions.

---

## 🔬 Simulation & Analysis

The simulation mode:
- runs up to hundreds of thousands of spins automatically
- uses the same game logic as the real game
- tracks total money bet vs total money returned
- calculates RTP using empirical data

This allows safe tuning of:
- payout multipliers
- penalty strength
- overall game balance

---

## ⚙️ Current Game Configuration

- Double Slash payout: **×2.5**
- Triple normal payout: **×16**
- Triple ⭐ payout: **×20**
- Triple 7️⃣ payout: **×25**
- Double bomb penalty: **−2× bet**
- Triple bomb penalty: **−10× bet**

With this configuration, RTP stabilizes around:

> **91% – 94% over 200,000 spins**

This range is consistent with real-world slot machines.

---

## 📚 Key Learnings

- Frequent small wins affect RTP more than rare jackpots
- RTP is driven by **frequency**, not just payout size
- Simulation is essential for validating probabilistic systems
- Small parameter changes can drastically affect long-term outcomes
- Separating gameplay and analysis leads to cleaner design

---

## ▶️ How to Run

### Play the game
```bash
python slot.py

###Run the simulation:
python slots_simulation.py

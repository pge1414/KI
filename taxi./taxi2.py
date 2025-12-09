import gymnasium as gym
import numpy as np
import random
import pygame
import time

# --- Parameter / Farben für GUI ---
CELL_SIZE = 80
GRID_ROWS = 5
GRID_COLS = 5
WIDTH = CELL_SIZE * GRID_COLS
HEIGHT = CELL_SIZE * GRID_ROWS

COLOR_BG = (220, 220, 220)
COLOR_GRID = (200, 200, 200)
COLOR_TAXI = (255, 215, 0)       # gold/yellow
COLOR_PASSENGER = (0, 0, 255)   # blue
COLOR_DEST = (255, 0, 255)      # magenta

# --- Q‑Learning Training ---
def train_q_learning(env, episodes=20000, alpha=0.7, gamma=0.95,
                     epsilon_start=1.0, epsilon_min=0.05, epsilon_decay=0.0005):
    n_states = env.observation_space.n
    n_actions = env.action_space.n
    Q = np.zeros((n_states, n_actions))
    epsilon = epsilon_start

    for ep in range(episodes):
        state, _ = env.reset()
        done = False

        while not done:
            if random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state])

            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            old = Q[state, action]
            Q[state, action] = old + alpha * (reward + gamma * np.max(Q[next_state]) - old)
            state = next_state

        if epsilon > epsilon_min:
            epsilon -= epsilon_decay

    return Q

def decode_state(state, env):
    # Gymnasium internal encode: we can use env.unwrapped.decode or similar, but
    # easiest: use env.env.decode (if available)
    try:
        return env.env.decode(state)
    except:
        # fallback: same as older gym versions
        return env.unwrapped.decode(state)

# --- GUI + Simulation mit gelernter Q‑Tabelle ---
def visualize_with_pygame(env, Q, delay=0.5):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Taxi-v3 with Q‑Learning GUI")

    state, _ = env.reset()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

        # get action from Q‑table (greedy)
        action = np.argmax(Q[state])

        # decode state: (taxi_row, taxi_col, pass_loc, dest_loc)
        taxi_row, taxi_col, pass_loc, dest = decode_state(state, env)

        # clear screen
        screen.fill(COLOR_BG)

        # draw grid
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, COLOR_GRID, rect, 1)

        # draw passenger (wenn nicht im Taxi)
        if pass_loc < 4:
            px, py = env.unwrapped.locs[pass_loc]  # locs enthält coords der special points
            # locs liefert (row, col)
            rect = pygame.Rect(py * CELL_SIZE, px * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, COLOR_PASSENGER, rect)

        # draw destination
        dx, dy = env.unwrapped.locs[dest]
        rect = pygame.Rect(dy * CELL_SIZE, dx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, COLOR_DEST, rect)

        # draw taxi
        rect = pygame.Rect(taxi_col * CELL_SIZE, taxi_row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, COLOR_TAXI, rect)

        pygame.display.flip()
        time.sleep(delay)

        # Schritt ausführen
        state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

    pygame.quit()

if __name__ == "__main__":
    env = gym.make("Taxi-v3", render_mode="rgb_array")
    Q = train_q_learning(env, episodes=20000, alpha=0.7, gamma=0.95,
                         epsilon_start=1.0, epsilon_min=0.05, epsilon_decay=0.0005)
    visualize_with_pygame(env, Q, delay=0.3)

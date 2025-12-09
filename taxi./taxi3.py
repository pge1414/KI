import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def train_q_learning(env, episodes=20000, alpha=0.7, gamma=0.95, 
                     epsilon_start=1.0, epsilon_min=0.05, epsilon_decay=0.0005):
    n_states = env.observation_space.n
    n_actions = env.action_space.n
    Q = np.zeros((n_states, n_actions))
    epsilon = epsilon_start

    rewards_per_episode = []

    for ep in tqdm(range(episodes), desc="Training Q‑Learning"):
        state, _ = env.reset()
        done = False
        total_reward = 0

        while not done:
            # Epsilon‑greedy
            if random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state])

            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            # Q‑Update
            old = Q[state, action]
            Q[state, action] = old + alpha * (reward + gamma * np.max(Q[next_state]) - old)

            state = next_state
            total_reward += reward

        # Epsilon decay
        if epsilon > epsilon_min:
            epsilon -= epsilon_decay

        rewards_per_episode.append(total_reward)

    return Q, rewards_per_episode

def run_episode(env, Q, render=True):
    state, _ = env.reset()
    done = False
    total_reward = 0
    steps = 0

    if render:
        print(env.render())

    while not done:
        action = np.argmax(Q[state])
        state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        steps += 1
        if render:
            print(env.render())
    return total_reward, steps

if __name__ == "__main__":
    env = gym.make("Taxi-v3", render_mode="ansi")
    Q, rewards = train_q_learning(env,
                                  episodes=25000,
                                  alpha=0.7,
                                  gamma=0.95,
                                  epsilon_start=1.0,
                                  epsilon_min=0.05,
                                  epsilon_decay=0.0005)

    # Plot Reward‑Progress über Episoden
    plt.plot(rewards)
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Q‑Learning: Reward über Episoden")
    plt.show()

    # Test: eine Episode mit „Greedy“-Policy
    total_reward, steps = run_episode(env, Q, render=True)
    print(f"Test‑Episode beendet: Reward = {total_reward}, Schritte = {steps}")

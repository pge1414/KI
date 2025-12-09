import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def q_lernen(umgeb, nr=20000, alpha=0.7, gamma=0.95, 
                     start=1.0, min=0.05, verfall=0.0005):
    n_states = umgeb.observation_space.n
    n_actions = umgeb.action_space.n
    Q = np.zeros((n_states, n_actions))
    y = start

    bel_pro = []

    for ep in tqdm(range(nr), desc="Training Q‑Learning"):
        status, _ = umgeb.reset()
        fertig = False
        bel_insg = 0

        while not fertig:
            if random.random() < y:
                akt = umgeb.action_space.sample()
            else:
                akt = np.argmax(Q[status])

            n_status, bel, terminiert, gekürzt, _ = umgeb.step(akt)
            fertig = terminiert or gekürzt

            alt = Q[status, akt]
            Q[status, akt] = alt + alpha * (bel + gamma * np.max(Q[n_status]) - alt)

            status = n_status
            bel_insg += bel
        if y > min:
            y -= verfall

        bel_pro.append(bel_insg)

    return Q, bel_pro

def run_episode(umgeb, Q, g=True):
    a, _ = umgeb.reset()
    fertig = False
    bel_insg = 0
    schritte = 0

    if g:
        print(umgeb.render())

    while not fertig:
        action = np.argmax(Q[a])
        a, belohnung, terminiert, gekürzt, _ = umgeb.step(action)
        fertig = terminiert or gekürzt
        bel_insg += belohnung
        schritte += 1
        if g:
            print(umgeb.render())
    return bel_insg, schritte

if __name__ == "__main__":
    env = gym.make("Taxi-v3", render_mode="ansi")
    Q, rewards = q_lernen(env,nr=25000,alpha=0.7,gamma=0.95,start=1.0,min=0.05,verfall=0.0005)

    
    plt.plot(rewards)
    plt.xlabel("VersuchNr")
    plt.ylabel("Belohnung")
    plt.title("Q‑Learning: Belohnung pro Nr")
    plt.show()

  
    bel_insg, steps = run_episode(env, Q, g=True)
    print(f"Test‑Episode beendet: Belohnung = {bel_insg}, Schritte = {steps}")

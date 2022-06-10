import numpy as np
import random

class Selected_Reward():#Env

    def __init__(self, real_arms):
        self.real_arms = real_arms
        pass
    
    def judge(self,p):
        if random.random() < self.real_arms[p]:
            return 1.0
        else:
            return 0.0

class Greedy():#argent

    def __init__(self,e,act):
        self.e = e
        self.count = np.zeros(len(act))
        self.act_value = np.zeros(len(act))
        pass

    def select_arm(self):
        if np.random.random() > self.e:
            selected_act = np.argmax(self.act_value)
        else:
            selected_act = random.randint(0, 2)
        return selected_act

    def Update(self, selected_act, rwd):
        self.count[selected_act] += 1
        N = self.count[selected_act]
        self.act_value[selected_act] = ((N-1)/N) * self.act_value[selected_act] + rwd/N
    
def simulatar(real_arms,e):
    arms = real_arms
    opt = np.argmax(arms)
    world = 1000
    money = 500
    player_arm_answer = [0]*world
    player_log,earned_rwd = [[0 for _ in range(money)] for _ in range(world)] ,[[0 for _ in range(money)] for _ in range(world)] 
    Env = Selected_Reward(arms)
    for i in range(world):
        Player = Greedy(e,arms)
        for l in range(money):
            arm = Player.select_arm()
            rwd = Env.judge(arm)
            Player.Update(arm,rwd)
            player_log[i][l] = arm
            earned_rwd[i][l] = rwd
        player_arm_answer[i] = arm

    return np.argmax(np.bincount(player_arm_answer))#toUI


def start(n_1,n_2,n_3,e):
    np.random.seed(2022)
    random.seed(7)
    real_arms = [n_1, n_2, n_3]
    e = e
    return simulatar(real_arms,e)
#print(start(0.8,0.9,0.8,0.1))

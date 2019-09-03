# import gym

# env = gym.make('CartPole-v0') # select game
# observation = env.reset() # initialize

# for i in range(100):
#   env.render()
#   observation, reward, done, info = env.step(1) # go right
# env.env.close()

import gym

env = gym.make('SpaceInvaders-v0') # sellect game
env.reset() # initialize
for _ in range(1000):
    env.step(env.action_space.sample())
    env.render('human')
env.close()  # https://github.com/openai/gym/issues/893

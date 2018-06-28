import gym

import torchrl.registry as registry
import torchrl.registry.hparams as hparams
from torchrl.registry.problems import A2CProblem
from torchrl.learners import BaseA2CLearner


@registry.register_problem('a2c-cartpole-v0')
class CartPoleA2CProblem(A2CProblem):
  def make_env(self):
    return gym.make('CartPole-v0')

  def init_agent(self):
    params = self.params

    observation_space, action_space = self.get_gym_spaces()

    agent = BaseA2CLearner(
        observation_space,
        action_space,
        lr=params.actor_lr,
        gamma=params.gamma,
        lmbda=params.lmbda,
        alpha=params.alpha,
        beta=params.beta)

    return agent


@registry.register_hparam('a2c-cartpole')
def hparam_a2c_cartpole():
  params = hparams.base_pg()

  params.num_processes = 16

  params.rollout_steps = 5
  params.max_episode_steps = 500
  params.num_total_steps = int(1e6)

  params.alpha = 0.5
  params.gamma = 0.99
  params.beta = 1e-3
  params.lmbda = 1.0

  params.batch_size = 128
  params.tau = 1e-2
  params.actor_lr = 3e-4

  return params

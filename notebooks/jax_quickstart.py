import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random, device_put
import numpy as onp

key = random.PRNGKey(0)
x = random.normal(key, (10,))
print(x)
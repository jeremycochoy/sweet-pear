# Sweet Pear library

Sweet pear is a python package wich add
basic functional methods to the core types
of python.

This is really usefull for fast prototyping / debugging.

Usage example:
```
(1, 2, 3, 4).map(lambda x: x**2)
["hello", "world"].map('capitalize')
```

You can also is this property to access member of objects:
```
import numpy as np
import torch

infos = (np.array([1,2,3]), np.zeros((2,5)), torch.ones((3,4)))
infos.map('shape')
```

# How does it works

It rely on ForbiddenFruit to patch the built in types in order to add the `map` method.
The implementation is pretty straight forward and simply rely on python's map implementation.


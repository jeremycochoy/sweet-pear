# Sweet Pear library

Sweet pear is a python package which add
basic functional member methods to the build in
python types (`str`, `tuple`, `list`, `range`).

## I don't find my loved `awsmstff` function!

If you think that a commonly used function is missing,
don't worry. Just open a issue for feature request
describing its usage. If your request is accepted,
it will be implemented in few days and a new version of
this package will be released.

## Examples
Usage example:
```python
import sweetpear

(1, 2, 3, 4).map(lambda x: x**2)
["hello", "world"].map('capitalize')
```

You can also is this property to access member of objects:
```python
import numpy as np
import torch

infos = (np.array([1,2,3]), np.zeros((2,5)), torch.ones((3,4)))
infos.map('shape')
```

Advanced features like groupby are now easily accessible :)
```
>>> "Abrakadabra!".groupby(lambda x: x== 'a' or x== "A")
{True: ['A', 'a', 'a', 'a', 'a'], False: ['b', 'r', 'k', 'd', 'b', 'r', '!']}
```

## API
Here is the list of the available functions:
```
[].map
[].tail
[].drop
[].take
[].firt
[].second
[].concat
[].flatten
[].count
[].groupby
[].filter
[].reject
```

For more information on a specific method, just type
```python
import sweetpear

help([].groupby)
```
in your python console.

## How does it works

The implementation rely on the python library `ForbiddenFruit` to patch the built in types
and add custom methods.
Most of the methods are binding around the awesome `cytoolz` package.

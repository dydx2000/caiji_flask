from __future__ import print_function

import torch

x = torch.empty(5, 3)
# print(x)

x = torch.rand(5, 3)
# print(x)
# print(x.shape)

x = torch.zeros(5,3, dtype=torch.long)
print(x)

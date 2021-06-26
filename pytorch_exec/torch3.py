import torch

x1 = torch.ones(3, 3)
print(x1)

x = torch.ones(2, 2, requires_grad=True)
print(x)
y = x + 2
# print(y)
#
# print(x.grad_fn)
# print(y.grad_fn)

a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a * a).sum()
print(b)
print(b.requires_grad)

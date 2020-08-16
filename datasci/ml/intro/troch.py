'''
https://jovian.ml/aakashns/01-pytorch-basics
https://blog.exxactcorp.com/the-most-important-fundamentals-of-pytorch-you-should-know/
'''

import torch
'''t1 = torch.tensor(4.)
print("t1:", t1, t1.dtype)
t2 = torch.tensor([1., 2, 3, 4])
print("t2:",t2)
# Matrix
t3 = torch.tensor([[5., 6],
                   [7, 8],
                   [9, 10]])
print("t3:", t3, t3.dtype)
'''
# Create tensors.
x = torch.tensor(3.)
w = torch.tensor(4., requires_grad=True)
b = torch.tensor(5., requires_grad=True)

y = w * x + w * w* b
y.backward()
print('dy/dx:', x.grad)
print('dy/dw:', w.grad) # dev of y when w=4  dy/dw(3*w+5*w**2)=3+10*w=3+10*4= 43
print('dy/db:', b.grad)
print(' x :', x, ' w :', w, ' b :', b)
print(' y :', y , y.dtype)



def func(x):
    return x**3 - 7*x**2 + 11 * x


x = torch.tensor(2.0, requires_grad=True)
y = func(x)
y.backward()
print('dy/dx:', x.grad)#  derivative of y for x =2
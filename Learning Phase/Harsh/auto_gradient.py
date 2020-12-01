# -*- coding: utf-8 -*-
"""auto_gradient.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L_ibndmUiaIcLubhg-Ks0Lk0idF8cjz4
"""

import torch
import pdb

#training set 
x_train = [1.0, 2.0, 3.0]
y_train = [3.0, 8.0, 15.0]

#starting values
w1 = torch.tensor([1.0], requires_grad=True)
w2 = torch.tensor([2.0], requires_grad=True)

#forward pass
def forward(x):
    return (x*x*w2 + x*w1)

# calculating loss
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

# Before training 
print("Prediction (before training) for x=",4, "is:", forward(4).item())
# correct value is 24.0

# Training 
for epoch in range(500):
    for x_val, y_val in zip(x_train, y_train):
    
        l = loss(x_val, y_val) 
        l.backward() 
        #g1=w1.grad.data[0];
        #g1=w2.grad.data[0];
        print("\tgrad: ", x_val, y_val, w1.grad.item(), w2.grad.item())
        w1.data = w1.data - 0.01 * w1.grad.item()
        w2.data = w2.data - 0.01 * w2.grad.item()
        
        #print("w1=",w1.item(), "w2=", w2.item())
        # making gradients zero after updating weights
        w1.grad.data.zero_()
        w2.grad.data.zero_()
    print("epoch:", epoch, "loss=", l.item())

# After training
print("Prediction (after training) for x=",4, "is:", forward(4).item())
print("w1=",w1.item(), "w2=", w2.item())
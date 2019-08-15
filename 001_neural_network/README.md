# First Neural network

This program is simply to train a neural network with simplest of input and make it do simple output.

0, 0, 1 => 0
1, 1, 1 => 1
1, 0, 1 => 1
0, 1, 1 => 0

We train the neural network 10,000 times. each time we calculate the error.
We are using the sigmoid function to calculate the adjustment. So if the network is not confident, the adjustment will be more.
if the network is more confident, the adjustment will be less.

Once the error is calculated, we calculate the adjustment using sigmoid and error .

We apply adjustment to the weights, and try it again.

Finally we see that the values are conversing.


### TODO

We can try using Keras library to do the same function: just to learn Keras library.

### References

[Reference](https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1)
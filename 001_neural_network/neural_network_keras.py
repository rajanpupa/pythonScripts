from keras.models import Sequential;
from keras.layers import Dense;
import numpy;

# Create a sequential model
model = Sequential()

# create a layer
layer1 = Dense(
          1,
          activation = 'sigmoid', 
          # activation = 'relu',
          input_shape=(3,)
        )

print("Weights ", layer1.get_weights() )

w = numpy.random.rand(4, 1);
print(w)
b = numpy.random.rand(1)
print(b)

# Add a input layer
model.add(
  layer1
)
# Can add multiple layers specifying the output vector and activation('relu', 'sigmoid', 'softmax' ) etc

# Set the weight
weights = numpy.array( [
  [.5],
  [.5],
  [.5]
])
# print(weights)
biases = numpy.array([0])
# print(biases)
# setting weights
layer1.set_weights(
  [weights, biases]
)

# Compile the model with optimizer, loss function and other metrics
model.compile(optimizer='rmsprop',
              loss = 'binary_crossentropy',
              metrics=['accuracy']
)

# fit the training data
input = numpy.array([
    [0,0,1],
    [1,1,1],
    [1,0,1],
    [0,1,1]
])

labels = numpy.array([
    0,1,1,0
]).T

model.fit(input, 
          labels,
          batch_size=1,
          epochs=500, verbose=0,
          callbacks=None,
          validation_split=0,
          validation_data=None,
          shuffle=False,
          class_weight=None,
          sample_weight=None,
          initial_epoch=0
)

model.summary()

# print the layer weights
print('printing Trained weights: ')
for layer in model.layers:
    weights = layer.get_weights()
    print(weights);

# evaluate the test data
print(
  model.predict_classes(
    numpy.array([
                  [1,0,0],
                  [1,1,0],
                  [0,1,0]
                ]),
    verbose=1
  )
)



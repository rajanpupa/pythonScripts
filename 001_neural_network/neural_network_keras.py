from keras.models import Sequential;
from keras.layers import Dense;
import numpy;

model = Sequential()

# Add a input layer
model.add(Dense(1, activation = 'sigmoid', input_shape=(3,)))
# Can add multiple layers specifying the output vector and activation('relu', 'sigmoid', 'softmax' )

# Compile the model with optimizer, loss function and 
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
          epochs=1000, verbose=0,
          callbacks=None,
          validation_split=0,
          validation_data=None,
          shuffle=False,
          class_weight=None,
          sample_weight=None,
          initial_epoch=0
)

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



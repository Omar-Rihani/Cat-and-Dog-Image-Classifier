# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=10,  # You can increase this if needed
    validation_data=validation_generator,
    validation_steps=len(validation_generator)
)

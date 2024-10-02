# Make predictions on the test images
test_images = test_generator.next()
predictions = model.predict(test_images)
probabilities = [1 if pred[0] > 0.5 else 0 for pred in predictions]

# Plot test images with predictions
plotImages(test_images, probabilities)

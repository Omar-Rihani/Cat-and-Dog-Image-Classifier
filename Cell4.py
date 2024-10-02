# Function to plot images
def plotImages(images_arr, probabilities=None):
    plt.figure(figsize=(10, 10))
    for i in range(5):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images_arr[i])
        if probabilities is not None:
            plt.title(f"Probability: {probabilities[i]:.2f}")
        plt.axis("off")

# Plot five random training images
sample_images, _ = next(train_generator)
plotImages(sample_images)

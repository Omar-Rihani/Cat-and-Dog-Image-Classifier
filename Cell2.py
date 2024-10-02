# Download the dataset
!wget --no-check-certificate \
    https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
    -O /tmp/cats_and_dogs.zip

# Unzip the dataset
import zipfile
with zipfile.ZipFile('/tmp/cats_and_dogs.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/')

# Set directory paths
base_dir = '/tmp/cats_and_dogs_filtered/'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

# Set image dimensions
IMG_HEIGHT = 150
IMG_WIDTH = 150
BATCH_SIZE = 32

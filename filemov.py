import os
import shutil

# specify your source and destination directories
source_dir = '/path/to/source/directory'
dest_dir = '/path/to/destination/directory'

# iterate over all files in the source directory
for filename in os.listdir(source_dir):
    # check if the file is a .txt file
    if filename.endswith('.txt'):
        # construct full file path
        source = os.path.join(source_dir, filename)
        destination = os.path.join(dest_dir, filename)
        # move the file to the destination directory
        shutil.move(source, destination)

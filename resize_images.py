from PIL import Image
import os

# Function to resize images
def resize_images(input_dir, output_dir, new_width, new_height):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Open and resize the image
                with Image.open(file_path) as img:
                    resized_img = img.resize((new_width, new_height))
                    
                    # Save the resized image to the output directory
                    output_path = os.path.join(output_dir, filename)
                    resized_img.save(output_path)
                    print(f"Resized and saved: {filename}")
            except Exception as e:
                print(f"Failed to resize {filename}: {e}")

# Define input and output directories and target size
input_directory = "Original image"   # Replace with your input directory
output_directory = "resized_images"  # Replace with your output directory
width, height = 200, 200  # Replace with desired dimensions

# Call the function
resize_images(input_directory, output_directory, width, height)

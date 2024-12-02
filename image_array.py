import os
import json

def generate_nextjs_image_array(folder_path: str, base_path: str = '/images') -> str:
    """
    Generates a Next.js image array for all image files in the specified folder.

    Args:
        folder_path (str): The path to the folder containing image files.
        base_path (str): The base path for `src` in the output (default is '/images').

    Returns:
        str: A formatted string containing the Next.js image array.
    """
    # Supported image extensions
    supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
    images = []

    # Traverse through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Check if the file is an image
        if os.path.isfile(file_path) and os.path.splitext(file_name)[1].lower() in supported_extensions:
            # Generate `src` and `alt` attributes
            src = f"{base_path}/{file_name}"
            alt = f"{os.path.splitext(file_name)[0].replace('-', ' ').title()}"
            images.append({"src": src, "alt": alt})

    # Format the images array as a string
    images_array = json.dumps(images, indent=4)
    return f"const images = {images_array};"

# Example usage
if __name__ == "__main__":
    # Specify the folder containing images
    folder = "./epam/press-conferece-investors-presentation"
    base_path = "/images/press-conferece-investors-presentation"

    # Generate the Next.js image array
    result = generate_nextjs_image_array(folder, base_path)

    # Print the result
    print(result)

    # Optionally, save output to a file
    with open("images.js", "w", encoding="utf-8") as file:
        file.write(result)
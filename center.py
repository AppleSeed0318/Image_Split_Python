from PIL import Image

def split_image_uniform(image_path, frame_data, uniform_size):
    # Open the original image
    original_image = Image.open(image_path)

    frames = []
    for i, (start_x, start_y, width, height, center_x, center_y) in enumerate(frame_data):
        # Calculate the top-left corner of the frame centered around provided center
        x = center_x - uniform_size[0] // 2
        y = center_y - uniform_size[1] // 2

        # Ensure the frame does not go out of image boundaries
        x = max(0, min(x, original_image.width - uniform_size[0]))
        y = max(0, min(y, original_image.height - uniform_size[1]))

        # Crop the frame based on the calculated coordinates
        frame = original_image.crop((x, y, x + uniform_size[0], y + uniform_size[1]))

        frames.append(frame)

        # Save the frame as a separate image
        frame.save(f'frame_{i}.png')

    return frames

# Example frame data using (start_x, start_y, width, height, center_x, center_y)
frame_data = [
    (1, 1, 389, 512, 170, 519), # Frame starting at (120, 10) with center at (170, 60)
    (392, 1, 387, 512, 168, 519), # Frame starting at (230, 10) with center at (280, 60)
    (781, 1, 398, 512, 179, 519), # Frame starting at (230, 10) with center at (280, 60)
    (1181, 1, 422, 512, 203, 519), # Frame starting at (230, 10) with center at (280, 60)
    (1605, 1, 429, 505, 210, 513), # Frame starting at (230, 10) with center at (280, 60)
    (1, 515, 439, 500, 220, 508), # Frame starting at (230, 10) with center at (280, 60)
    (442, 515, 439, 507, 220, 515), # Frame starting at (230, 10) with center at (280, 60)
    (883, 515, 439, 510, 220, 518), # Frame starting at (230, 10) with center at (280, 60)
    (1324, 515, 438, 521, 220, 529), # Frame starting at (230, 10) with center at (280, 60)
    (1, 1038, 457, 510, 233, 518), # Frame starting at (230, 10) with center at (280, 60)
    # Add more frames as needed
]

# Define a uniform size for all frames
uniform_size = (600, 600)  # Width, Height

# Path to the big image
image_path = 'avatar-12.png'

# Split the image into uniform size frames centered at provided coordinates
split_image_uniform(image_path, frame_data, uniform_size)
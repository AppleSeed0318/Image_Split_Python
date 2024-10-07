from PIL import Image

def resize_images_based_on_center(image_path, centers, index):
    resized_images = []
    # Define uniform size for all images
    uniform_size = (400, 750)  # Width, Height

    print("===>>>>>>>>>>>>", image_path)
    # Open the original image
    original_image = Image.open(image_path)
    
    # Get center position (center_x, center_y) for the current image
    center_x, center_y = centers

    # Calculate the top-left corner of the crop area
    # crop_x = center_x - uniform_size[0] // 2
    # crop_y = center_y - uniform_size[1] // 2
    # Calculate the paste position
     # Create a new image with the target size and white background
    new_image = Image.new("RGBA", uniform_size, (255, 255, 255, 0))

    left = 0 - center_x
    top = 0 - center_y

    # crop_x = uniform_size[0]/2 - center_x
    # crop_y = uniform_size[1]/2 - center_y

    # last_x = uniform_size[0]/2 + center_x
    # last_y = uniform_size[0]/2 + center_y

    # print(crop_x, crop_y, last_x, last_y)

    

    # # Ensure the crop area is within the image boundaries
    # if crop_x < 0:
    #     crop_x = 0
    # elif crop_x + uniform_size[0] > original_image.width:
    #     crop_x = original_image.width - uniform_size[0]

    # if crop_y < 0:
    #     crop_y = 0
    # elif crop_y + uniform_size[1] > original_image.height:
    #     crop_y = original_image.height - uniform_size[1]

    # Crop the image based on the calculated coordinates
    # frame = original_image.crop((crop_x, crop_y, crop_x + uniform_size[0], crop_y + uniform_size[1]))
    # frame = original_image.crop((crop_x, crop_y, last_x, last_y))

    new_image.paste(original_image, (left, top))
    resized_images.append(new_image)

    # resized_images.append(frame)

    # Save the resized image
    new_image.save(f'./suspance/result/resized/suspance_fire_{index}.png')

    return resized_images

# Example list of image paths
image_paths = [
    'frame_0.png',
    'frame_1.png',
    'frame_2.png',
    'frame_3.png',
    'frame_4.png',
    'frame_5.png',
    'frame_6.png',
    'frame_7.png',
    'frame_8.png',
    'frame_9.png',
    'frame_10.png',
    'frame_11.png',
    'frame_12.png',
    'frame_13.png',
    'frame_14.png',
    # Add more image paths as needed
]


coordinates = [[1, 1, 364, 719, 0, -27, -23], [367, 1, 382, 714, 0, -18, -23], [751, 1, 392, 711, 0, -13, -22], [1145, 1, 393, 712, 0, -13, -21], [1540, 1, 396, 712, 0, -11, -21], [1, 722, 394, 712, 0, -12, -21], [397, 722, 387, 714, 0, -15, -20], [786, 722, 376, 723, 0, -21, -20], [1164, 722, 369, 734, 0, -25, -20], [1535, 722, 360,
                731, 0, -28, -19], [1, 1, 353, 735, 1, -31, -19], [356, 1, 365, 730, 1, -26, -19], [723, 1, 365, 728, 1, -26, -18], [1090, 1, 358, 718, 1, -29, -18], [1450, 1, 357, 718, 1, -30, -18], [1, 738, 357, 720, 1, -30, -17], [360, 738, 362, 728, 1, -28, -17], [724, 738, 364, 730, 1, -27, -17], [1090, 738, 362, 722, 1, -28, -16], [1454, 738, 360, 722, 1, -29, -16], [1, 1, 400, 724, 2, -9, -15], [403, 1, 389, 724, 2, -12, -15], [794, 1, 366, 724, 2, -29, -15], [1162, 1, 341, 725, 2, -39, -14], [1505, 1, 338, 733, 2, -40, -7], [1, 736, 332, 734, 2, -42, -6], [335, 736, 327, 726, 2, -47, -14], [664, 736, 346, 737, 2, -31, -13], [1012, 736,
                360, 729, 2, -29, -13], [1374, 736, 360, 729, 2, -29, -13], [1, 1, 363, 728, 3, -28, -13], [366, 1, 365, 728, 3, -26, -13], [733, 1, 364, 726, 3, -27, -14], [1099, 1, 375, 726, 3, -22, -14], [1476, 1, 376, 726, 3, -21, -14], [1, 731, 376, 724, 3, -21, -15], [379, 731, 373, 725, 3, -22, -14], [754, 731, 372, 736, 3, -23, -15], [1128, 731, 375, 738, 3, -21, -16], [1505, 731, 380, 731, 3, -19, -16], [1, 1, 380, 738, 4, -19, -16], [383, 1, 372, 735, 4, -23, -17], [757, 1, 372, 741, 4, -23, -10], [1131, 1, 367, 720, 4, -26, -17], [1500, 1, 363, 719, 4, -27, -17], [1, 744, 358, 719, 4, -30, -17], [361, 744, 360, 716, 4, -30, -19],
            [723, 744, 362, 716, 4, -28, -19], [1087, 744, 360, 724, 4, -29, -19], [1449, 744, 355, 728, 4, -31, -20], [1, 1, 363, 738, 5, -27, -16], [366, 1, 364, 741, 5, -27, -13], [732, 1, 358, 743, 5, -29, -11], [1092, 1, 362, 744, 5, -28, -10], [1456, 1, 366, 741, 5, -26, -10], [1, 747, 365, 733, 5, -26, -9], [368, 747, 364, 724, 5, -27, -23]]

inc = 0

# ------------------------------------------------For Single File-------------------------------------------------------------

# index = 0
# for data in coordinates:
#     image_path = "./enemyhit/frame_fire_"+ str(index) + ".png"

#     resize_images_based_on_center(image_path, (data[5], data[6]), inc)
#     index = index + 1
#     inc = inc + 1
# -------------------------------------------------------------------------------------------------------------


# ----------------------------------------------For Multi File-----------------------------------------------
for x in range(6):
    
    filtered_array = [arr for arr in coordinates if arr[4] == x]
    index = 0
    for data in filtered_array:
        image_path = "./suspance/result/frame_" + str(x*10 + index) + ".png"

        resize_images_based_on_center(image_path, (data[5], data[6]), inc)
        index = index + 1
        inc = inc + 1
# ---------------------------------------------------------------------------------------------

# frame_16_5.png
# Resize images based on center positions

from PIL import Image

def resize_images_based_on_center(image_path, centers, index, i):
    resized_images = []
    # Define uniform size for all images
    uniform_size = (600, 600)  # Width, Height

    print("===>>>>>>>>>>>>", image_path)
    # Open the original image
    original_image = Image.open(image_path)
    
    # Get center position (center_x, center_y) for the current image
    center_x, center_y = centers

    # Calculate the top-left corner of the crop area
    # crop_x = center_x - uniform_size[0] // 2
    # crop_y = center_y - uniform_size[1] // 2

    crop_x = uniform_size[0]/2 - center_x
    crop_y = uniform_size[1]/2 - center_y

    last_x = uniform_size[0]/2 + center_x
    last_y = uniform_size[0]/2 + center_y

    print(crop_x, crop_y, last_x, last_y)

    # Ensure the crop area is within the image boundaries
    if crop_x < 0:
        crop_x = 0
    elif crop_x + uniform_size[0] > original_image.width:
        crop_x = original_image.width - uniform_size[0]

    if crop_y < 0:
        crop_y = 0
    elif crop_y + uniform_size[1] > original_image.height:
        crop_y = original_image.height - uniform_size[1]

    # Crop the image based on the calculated coordinates
    # frame = original_image.crop((crop_x, crop_y, crop_x + uniform_size[0], crop_y + uniform_size[1]))
    frame = original_image.crop((crop_x, crop_y, last_x, last_y))

    resized_images.append(frame)

    # Save the resized image
    frame.save(f'./resized_frames/frame_{index}_{i}.png')

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

# Example centers for each image (center_x, center_y)
centers = [
    (170, 519),
    (168, 519),
    (179, 519),
    (203, 519),
    (210, 513),
    (220, 508),
    (220, 515),
    (220, 518),
    (220, 529),
    (233, 518),
    (233, 519),
    (233, 519),
    (233, 519),
    (233, 483),
    (233, 483),
]

coordinates = [[1, 1, 374, 491, 0, 167, 492], [377, 1, 374, 491, 0, 167, 492], [753, 1, 374, 491, 0, 167, 492], [1129, 1, 374, 491, 0, 167, 492], [1505, 1, 374, 491, 0, 167, 492], [1, 494, 374, 491, 0, 167, 492], [377, 494, 374, 491, 0, 167, 492],
            [753, 494, 374, 491, 0, 167, 492], [1129, 494, 374, 491, 0, 167, 492], [1505, 494, 374, 491, 0, 167, 492], [1, 987, 374, 491, 0, 167, 492], [377, 987, 374, 491, 0, 167, 492], [753, 987, 374, 491, 0, 167, 492], [1129, 987, 374, 491, 0, 167, 492], [1505, 987, 374, 491, 0, 167, 492], [1, 1480, 374, 491, 0, 167, 492], [377, 1480, 374, 491, 0, 167, 492], [753, 1480, 374, 491, 0, 167, 492], [1129, 1480, 374, 491, 0, 167, 492], [1505, 1480, 374, 491, 0, 167, 492], [1, 1, 374, 491, 1, 167, 492], [377, 1, 374, 491, 1, 167, 492], [753, 1, 374, 491, 1, 167, 492], [1129, 1, 374, 491, 1, 167, 492], [1505, 1, 374, 491, 1, 167, 492],
            [1, 494, 374, 491, 1, 167, 492], [377, 494, 374, 491, 1, 167, 492], [753, 494, 374, 491, 1, 167, 492], [1129, 494, 374, 491, 1, 167, 492], [1505, 494, 374, 491, 1, 167, 492], [1, 987, 374, 491, 1, 167, 492], [377, 987, 374, 491, 1, 167, 492], [753, 987, 374, 491, 1, 167, 492], [1129, 987, 374, 491, 1, 167, 492], [1505, 987, 374, 491, 1, 167, 492], [1, 1480, 374, 491, 1, 167, 492], [377, 1480, 374, 490, 1, 167, 491], [753, 1480, 374, 490, 1, 167, 491], [1129, 1480, 374, 490, 1, 167, 491], [1505, 1480, 374, 490, 1, 167, 491], [1, 1, 374, 490, 2, 167, 491], [377, 1, 374, 490, 2, 167, 491], [753, 1, 374, 490, 2, 167, 491],
            [1129, 1, 374, 490, 2, 167, 491], [1505, 1, 374, 490, 2, 167, 491], [1, 493, 374, 490, 2, 167, 491], [377, 493, 374, 490, 2, 167, 491], [753, 493, 374, 490, 2, 167, 491], [1129, 493, 374, 490, 2, 167, 491], [1505, 493, 374, 490, 2, 167, 491], [1, 985, 374, 490, 2, 167, 491], [377, 985, 374, 490, 2, 167, 491], [753, 985, 374, 490, 2, 167, 491], [1129, 985, 374, 490, 2, 167, 491], [1505, 985, 374, 490, 2, 167, 491], [1, 1477, 374, 490, 2, 167, 491], [377, 1477, 374, 490, 2, 167, 491], [753, 1477, 374, 490, 2, 167, 491], [1129, 1477, 374, 490, 2, 167, 491], [1505, 1477, 374, 490, 2, 167, 491], [1, 1, 374, 490, 3, 167, 491],
            [377, 1, 391, 492, 3, 178, 492], [770, 1, 391, 492, 3, 178, 492], [1163, 1, 390, 487, 3, 177, 487], [1555, 1, 391, 473, 3, 177, 473], [1, 495, 393, 456, 3, 177, 456], [396, 495, 393, 442, 3, 177, 442], [791, 495, 392, 435, 3, 178, 435], [1185, 495, 388, 433, 3, 178, 433], [1575, 495, 391, 434, 3, 179, 434], [1, 953, 391, 434, 3, 179, 434], [394, 953, 392, 434, 3, 179, 434], [788, 953, 391, 436, 3, 181, 436], [1181, 953, 399, 438, 3, 187, 438], [1582, 953, 389, 441, 3, 180, 441], [1, 1396, 388, 445, 3, 179, 445], [391, 1396, 396, 448, 3, 187, 448], [789, 1396, 388, 451, 3, 178, 451], [1179, 1396, 389, 452, 3, 177, 452],
            [1570, 1396, 391, 450, 3, 177, 450], [1, 1, 393, 446, 4, 176, 446], [396, 1, 395, 441, 4, 176, 441], [793, 1, 396, 436, 4, 177, 436], [1191, 1, 407, 429, 4, 176, 429], [1, 449, 489, 422, 4, 177, 422], [492, 449, 491, 414, 4, 177, 414], [985, 449, 483, 406, 4, 177, 406], [1470, 449, 458, 401, 4, 178, 401], [1, 873, 392, 398, 4, 178, 398], [395, 873, 426, 394, 4, 212, 394], [823, 873, 464, 391, 4, 250, 391], [1289, 873, 480, 387, 4, 267, 387], [1, 1273, 484, 386, 4, 272, 386], [487, 1273, 494, 385, 4, 280, 385], [983, 1273, 522, 383, 4, 305, 383], [1507, 1273, 537, 382, 4, 318, 382], [1, 1661, 539, 380, 4, 318, 380], [542,
                1661, 537, 380, 4, 312, 380], [1081, 1661, 517, 382, 4, 296, 382], [1, 1, 496, 385, 5, 275, 385], [499, 1, 472, 389, 5, 251, 389], [973, 1, 461, 394, 5, 242, 394], [1436, 1, 456, 401, 5, 237, 401], [1, 404, 449, 407, 5, 231, 407], [452, 404, 443, 414, 5, 226, 414], [897, 404, 434, 422, 5, 217, 422], [1333, 404, 422, 428, 5, 204, 428], [1, 834, 411, 434, 5, 192, 434], [414, 834, 398, 439, 5, 179, 439], [814, 834, 397, 444, 5, 178, 444], [1213, 834, 397, 449, 5, 178, 449], [1612, 834, 396, 454, 5, 178, 454], [1, 1290, 395, 459, 5, 178, 459], [398, 1290, 394, 464, 5, 178, 464], [794, 1290, 392, 469, 5, 178, 469], [1188, 1290,
                391, 473, 5, 178, 473], [1581, 1290, 390, 478, 5, 178, 478], [1, 1, 389, 481, 6, 177, 481], [392, 1, 387, 485, 6, 177, 485], [781, 1, 387, 487, 6, 177, 487], [1170, 1, 386, 490, 6, 177, 490], [1558, 1, 386, 491, 6, 177, 491], [1, 494, 384, 492, 6, 177, 492], [387, 494, 382, 493, 6, 176, 493], [771, 494, 384, 493, 6, 177, 493], [1157, 494, 384, 492, 6, 177, 492], [1543, 494, 384, 492, 6, 177, 492], [1, 989, 384, 492, 6, 177, 492], [387, 989, 384, 492, 6, 177, 492], [773, 989, 384, 492, 6, 177, 492], [1159, 989, 384, 492, 6, 177, 492], [1545, 989, 384, 493, 6, 177, 493], [1, 1484, 385, 493, 6, 178, 493], [388, 1484, 385, 493,
                6, 178, 493], [775, 1484, 385, 493, 6, 178, 493], [1162, 1484, 385, 494, 6, 178, 494], [1549, 1484, 385, 494, 6, 178, 494], [1, 1, 385, 494, 7, 178, 494], [388, 1, 385, 494, 7, 178, 494], [775, 1, 385, 494, 7, 178, 494], [1162, 1, 385, 493, 7, 178, 493], [1549, 1, 385, 493, 7, 178, 493], [1, 497, 388, 493, 7, 178, 493], [391, 497, 390, 493, 7, 178, 493], [783, 497, 392, 492, 7, 178, 492], [1177, 497, 392, 492, 7, 178, 492], [1571, 497, 392, 492, 7, 178, 492], [1, 992, 392, 492, 7, 178, 492], [395, 992, 392, 492, 7, 178, 492], [789, 992, 392, 492, 7, 178, 492], [1183, 992, 392, 492, 7, 178, 492], [1577, 992, 392, 492, 7,
                178, 492], [1, 1486, 392, 492, 7, 178, 492], [395, 1486, 392, 492, 7, 178, 492], [789, 1486, 392, 492, 7, 178, 492], [1183, 1486, 392, 491, 7, 178, 491], [1577, 1486, 392, 490, 7, 178, 490], [1, 1, 392, 490, 8, 178, 490], [395, 1, 391, 490, 8, 178, 490], [788, 1, 391, 489, 8, 178, 489], [1181, 1, 391, 488, 8, 178, 488], [1574, 1, 391, 487, 8, 178, 487], [1, 493, 391, 487, 8, 178, 487], [394, 493, 391, 487, 8, 178, 487], [787, 493, 391, 487, 8, 178, 487], [1180, 493, 391, 487, 8, 178, 487], [1573, 493, 391, 487, 8, 178, 487], [1, 982, 391, 487, 8, 178, 487], [394, 982, 391, 487, 8, 178, 487], [787, 982, 391, 487, 8, 178,
                487], [1180, 982, 391, 487, 8, 178, 487], [1573, 982, 391, 487, 8, 178, 487], [1, 1471, 391, 487, 8, 178, 487], [394, 1471, 391, 487, 8, 178, 487], [787, 1471, 391, 487, 8, 178, 487], [1180, 1471, 391, 487, 8, 178, 487], [1573, 1471, 391, 487, 8, 178, 487], [1, 1, 391, 487, 9, 178, 487], [394, 1, 391, 487, 9, 178, 487], [787, 1, 391, 487, 9, 178, 487], [1180, 1, 391, 486, 9, 178, 486], [1573, 1, 391, 487, 9, 178, 487], [1, 490, 391, 487, 9, 178, 487], [394, 490, 391, 487, 9, 178, 487], [787, 490, 391, 487, 9, 178, 487], [1180, 490, 391, 487, 9, 178, 487], [1573, 490, 391, 488, 9, 178, 488], [1, 980, 391, 488, 9, 178, 488],
            [394, 980, 391, 488, 9, 178, 488], [787, 980, 391, 488, 9, 178, 488], [1180, 980, 391, 488, 9, 178, 488], [1573, 980, 391, 488, 9, 178, 488], [1, 1470, 391, 487, 9, 178, 487], [394, 1470, 391, 487, 9, 178, 487], [787, 1470, 391, 487, 9, 178, 487], [1180, 1470, 391, 487, 9, 178, 487], [1573, 1470, 391, 487, 9, 178, 487], [1, 1, 391, 486, 10, 178, 486], [394, 1, 391, 486, 10, 178, 486], [787, 1, 391, 486, 10, 178, 486], [1180, 1, 391, 486, 10, 178, 486], [1573, 1, 391, 486, 10, 178, 486], [1, 489, 391, 486, 10, 178, 486], [394, 489, 391, 487, 10, 178, 487], [787, 489, 391, 487, 10, 178, 487], [1180, 489, 391, 488, 10, 178,
                488], [1573, 489, 391, 489, 10, 178, 489], [1, 980, 391, 490, 10, 178, 490], [394, 980, 391, 490, 10, 178, 490], [787, 980, 391, 491, 10, 178, 491], [1180, 980, 391, 491, 10, 178, 491], [1573, 980, 392, 491, 10, 178, 491], [1, 1473, 392, 492, 10, 178, 492], [395, 1473, 392, 492, 10, 178, 492], [789, 1473, 392, 492, 10, 178, 492], [1183, 1473, 390, 493, 10, 176, 493], [1575, 1473, 391, 493, 10, 176, 493], [1, 1, 394, 491, 11, 177, 492], [397, 1, 394, 490, 11, 177, 491], [793, 1, 394, 488, 11, 177, 490], [1189, 1, 394, 482, 11, 177, 485], [1585, 1, 394, 514, 11, 177, 519], [1, 517, 395, 514, 11, 176, 519], [398, 517,
                394, 513, 11, 175, 519], [794, 517, 396, 513, 11, 175, 519], [1192, 517, 395, 513, 11, 174, 519], [1589, 517, 393, 457, 11, 172, 463], [1, 1033, 393, 455, 11, 172, 461], [396, 1033, 393, 513, 11, 172, 519], [791, 1033, 391, 513, 11, 170, 519], [1184, 1033, 391, 513, 11, 170, 519], [1577, 1033, 391, 513, 11, 170, 519], [1, 1, 389, 512, 12, 170, 519], [392, 1, 387, 512, 12, 168, 519], [781, 1, 398, 512, 12, 179, 519], [1181, 1, 422, 512, 12, 203, 519], [1605, 1, 429, 505, 12, 210, 513], [1, 515, 439, 500, 12, 220, 508], [442, 515, 439, 507, 12, 220, 515], [883, 515, 439, 510, 12, 220, 518], [1324, 515, 438, 521, 12, 220,
                529], [1, 1038, 457, 510, 12, 233, 518], [460, 1038, 457, 513, 12, 233, 519], [919, 1038, 457, 515, 12, 233, 519], [1378, 1038, 457, 518, 12, 233, 519], [1, 1558, 457, 483, 12, 233, 483], [460, 1558, 457, 483, 12, 233, 483], [1, 1, 457, 519, 13, 233, 519], [460, 1, 457, 519, 13, 233, 519], [919, 1, 457, 494, 13, 233, 494], [1378, 1, 457, 503, 13, 233, 503], [1, 522, 457, 507, 13, 233, 507], [460, 522, 457, 519, 13, 233, 519], [919, 522, 457, 519, 13, 233, 519], [1378, 522, 457, 519, 13, 233, 519], [1, 1043, 457, 519, 13, 233, 519], [460, 1043, 457, 519, 13, 233, 519], [919, 1043, 457, 501, 13, 233, 501], [1378, 1043,
                457, 504, 13, 233, 504], [1, 1, 457, 505, 14, 233, 505], [460, 1, 457, 519, 14, 233, 519], [919, 1, 457, 519, 14, 233, 519], [1378, 1, 457, 519, 14, 233, 519], [1, 522, 457, 510, 14, 233, 510], [460, 522, 457, 506, 14, 233, 506], [919, 522, 437, 505, 14, 220, 505], [1358, 522, 457, 506, 14, 233, 506], [1, 1034, 457, 510, 14, 233, 510], [460, 1034, 457, 508, 14, 233, 508], [919, 1034, 457, 509, 14, 233, 509], [1378, 1034, 457, 510, 14, 233, 510], [1, 1, 457, 511, 15, 233, 511], [460, 1, 457, 519, 15, 233, 519], [919, 1, 457, 519, 15, 233, 519], [1378, 1, 457, 503, 15, 233, 503], [1, 522, 457, 506, 15, 233, 506], [460, 522,
                457, 508, 15, 233, 508], [919, 522, 457, 508, 15, 233, 508], [1378, 522, 457, 519, 15, 233, 519], [1, 1043, 457, 519, 15, 233, 519], [460, 1043, 457, 519, 15, 233, 519], [919, 1043, 457, 517, 15, 233, 517], [1378, 1043, 457, 520, 15, 233, 521], [1, 1, 457, 524, 16, 233, 525], [460, 1, 457, 520, 16, 233, 524], [919, 1, 437, 518, 16, 220, 524], [1358, 1, 437, 519, 16, 220, 527], [1, 527, 437, 519, 16, 220, 529], [440, 527, 437, 519, 16, 220, 529], [879, 527, 427, 515, 16, 210, 525], [1308, 527, 420, 471, 16, 203, 481], [1, 1048, 396, 468, 16, 179, 478], [399, 1048, 377, 458, 16, 160, 468], [778, 1048, 376, 459, 16, 160,
                469], [1156, 1048, 376, 509, 16, 160, 519], [1534, 1048, 373, 509, 16, 160, 519], [1, 1, 372, 509, 17, 160, 519], [375, 1, 372, 461, 17, 160, 471], [749, 1, 371, 461, 17, 160, 471], [1122, 1, 370, 462, 17, 160, 472], [1494, 1, 370, 509, 17, 160, 519], [1, 512, 370, 509, 17, 160, 519], [373, 512, 370, 509, 17, 160, 519], [745, 512, 369, 465, 17, 160, 475], [1116, 512, 372, 467, 17, 163, 477], [1490, 512, 372, 472, 17, 163, 478], [1, 1023, 374, 473, 17, 165, 479], [377, 1023, 373, 475, 17, 163, 481], [752, 1023, 375, 517, 17, 165, 519], [1129, 1023, 375, 517, 17, 165, 519], [1506, 1023, 381, 517, 17, 168, 519], [1, 1,
                385, 518, 18, 169, 519], [388, 1, 386, 518, 18, 170, 519], [776, 1, 385, 518, 18, 170, 519], [1163, 1, 384, 489, 18, 170, 489], [1549, 1, 383, 519, 18, 170, 519], [1, 522, 383, 519, 18, 170, 519], [386, 522, 384, 519, 18, 172, 519], [772, 522, 384, 519, 18, 172, 519], [1158, 522, 385, 519, 18, 172, 519], [1545, 522, 384, 519, 18, 172, 519], [1, 1043, 384, 499, 18, 172, 499], [387, 1043, 387, 519, 18, 174, 519], [776, 1043, 387, 519, 18, 174, 519], [1165, 1043, 387, 519, 18, 174, 519], [1554, 1043, 386, 501, 18, 174, 501], [1, 1, 387, 501, 19, 175, 501], [390, 1, 388, 501, 19, 175, 501], [780, 1, 388, 501, 19, 175, 501],
            [1170, 1, 388, 502, 19, 175, 502], [1560, 1, 389, 502, 19, 176, 502], [1, 505, 389, 502, 19, 176, 502], [392, 505, 389, 519, 19, 176, 519], [783, 505, 389, 519, 19, 176, 519], [1174, 505, 389, 519, 19, 177, 519], [1565, 505, 389, 492, 19, 177, 492], [1, 1026, 390, 492, 19, 177, 492], [393, 1026, 390, 492, 19, 177, 492], [785, 1026, 390, 492, 19, 177, 492], [1177, 1026, 390, 492, 19, 177, 492], [1569, 1026, 391, 492, 19, 178, 492]]


for x in range(20):
    
    filtered_array = [arr for arr in coordinates if arr[4] == x]
    index = 0
    for data in filtered_array:
        image_path = "./frames/frame_" + str(x) + "_" + str(index) + ".png"

        resize_images_based_on_center(image_path, (data[5], data[6]), x, index)
        index = index + 1


# frame_16_5.png
# Resize images based on center positions

import os #os For system-level tasks
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #To hide tensorflow warning in terminal

import cv2
import numpy as np
import mediapipe as mp #face landmark
import webcolors  #convert RGB val to colorname
from skimage import color #convert RGB to LAB color

#dictionary of lipcolor and RGB val,we compare lipcolor with these and find closest match
custom_colors = {
    'Cherry Red': (222, 49, 99),
    'Rose Pink': (255, 102, 204),
    'Nude': (205, 133, 63),
    'Plum': (142, 69, 133),
    'Coral': (255, 127, 80),
    'Peach': (255, 218, 185),
    'Wine': (114, 47, 55),
    'Dusty Rose': (201, 115, 115),
    'Berry': (135, 38, 87),
    'Mahogany': (192, 64, 0),
    'Deep Red': (139, 0, 0),
    'Soft Pink': (255, 182, 193),
    'Crimson': (220, 20, 60),
    'Mauve': (224, 176, 255),
    'Brick': (178, 34, 34)
}

#function finds closest match
def get_closest_custom_color(rgb):
    min_dist = float('inf')
    closest_color = None
    input_lab = color.rgb2lab(np.uint8([[list(rgb)]]))[0][0]

    for name, ref_rgb in custom_colors.items():
        ref_lab = color.rgb2lab(np.uint8([[list(ref_rgb)]]))[0][0]
        dist = np.linalg.norm(input_lab - ref_lab)
        if dist < min_dist:
            min_dist = dist
            closest_color = name

    return closest_color

# Average color from region
def get_average_color(img, points):
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [np.array(points, dtype=np.int32)], 255)
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    mean_val = cv2.mean(blurred, mask=mask)
    return mean_val[:3]  # BGR

#webcam
def detect_lip_color():
    mp_face = mp.solutions.face_mesh
    cap = cv2.VideoCapture(0)

    upper_lip_indices = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
    lower_lip_indices = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291]

    with mp_face.FaceMesh(static_image_mode=False, refine_landmarks=True, max_num_faces=1) as face_mesh:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(frame_rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    h, w, _ = frame.shape
                    upper_points = [(int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in upper_lip_indices]
                    lower_points = [(int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)) for i in lower_lip_indices]

                    upper_color = get_average_color(frame, upper_points)
                    lower_color = get_average_color(frame, lower_points)

                    r_u, g_u, b_u = [int(c) for c in upper_color[::-1]]
                    r_l, g_l, b_l = [int(c) for c in lower_color[::-1]]

                    name_u = get_closest_custom_color((r_u, g_u, b_u))
                    name_l = get_closest_custom_color((r_l, g_l, b_l))

                    cv2.polylines(frame, [np.array(upper_points)], isClosed=True, color=(255, 0, 0), thickness=1)
                    cv2.polylines(frame, [np.array(lower_points)], isClosed=True, color=(0, 0, 255), thickness=1)

                    cv2.putText(frame, f'Upper: {name_u}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (r_u, g_u, b_u), 2)
                    cv2.putText(frame, f'Lower: {name_l}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (r_l, g_l, b_l), 2)

            cv2.imshow("Lipstick Shade Detector", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

detect_lip_color()

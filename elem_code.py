import os
import cv2
from ultralytics import YOLO

images_dir = os.path.join('.', 'test_images')
image_name = '98.png'
image_path = os.path.join(images_dir, image_name)

model_path = os.path.join('.', 'runs', 'detect',
                          'train6', 'weights', 'best.pt')
model = YOLO(model_path)

class_elements_mapping = {
    0: "Collapsed Accordion Code",
    1: "Expanded Accordion Code"
}


def detect_component(image_path):
    img = cv2.imread(image_path)
    results = model(img)[0]

    detected_components = set()
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > 0.5:
            detected_components.add(class_elements_mapping.get(
                int(class_id), "Unknown Component"))

            cv2.rectangle(img, (int(x1), int(y1)),
                          (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(img, class_elements_mapping.get(int(class_id), "Unknown"),
                        (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    output_path = os.path.join(images_dir, 'output_'+image_name)
    cv2.imwrite(output_path, img)

    return detected_components, output_path


components, output_image = detect_component(image_path)
print("Detected Components:", components)
print("Output Image with Detections Saved at:", output_image)

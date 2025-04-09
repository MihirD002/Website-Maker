from getComponent import get_component_code
from htmlDoc import create_html_document


def build_website_from_detections(detection_results, viewport_width, viewport_height):
    page_layout = []

    processed_detections = []

    class_map = {
        0: "Accordion Default",
        1: "Accordion Expanded"
    }
    total_comp = 0
    for result in detection_results.boxes.data.tolist():
        x_center, y_center, x2, y2, score, class_id = result
        if score > 0.5:

            x_min = min(x_center, x2)
            y_min = min(y_center, y2)
            width = abs(x2 - x_center)
            height = abs(y2 - y_center)

            if x_min > 1 or y_min > 1 or width > 1 or height > 1:
                x_min = x_min / viewport_width
                y_min = y_min / viewport_height
                width = width / viewport_width
                height = height / viewport_height

            processed_detections.append({
                'top': y_min,
                'left': x_min,
                'width': width,
                'height': height,
                'confidence': score,
                'class_id': int(class_id)
            })

    sorted_components = sorted(
        processed_detections, key=lambda det: det['top'])

    for detection in sorted_components:
        component_type = class_map.get(detection['class_id'], "Unknown")

        position_css = {
            'position': 'absolute',
            'left': f"{detection['left']*100}%",
            'top': f"{detection['top']*100}%",
            'width': f"{detection['width']*100}%",
            'height': f"{detection['height']*100}%"
        }

        component_html = get_component_code(
            component_type, position_css)
        page_layout.append(component_html)

    final_html = create_html_document(page_layout)
    return final_html

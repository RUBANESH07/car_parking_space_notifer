from django.shortcuts import render, HttpResponse 
import cv2
import base64
from ultralytics import YOLO

def page(request):
    message = '<h1>Hi Rubi</h1>'
    return HttpResponse(message)

def page1(request):
    message1 = '<h1>Hello Rubi</h1>'
    return HttpResponse(message1)

def page2(request):
    message2 = '<h1>Hi shobi</h1>'
    return HttpResponse(message2)

def img_07(request):
    context = {'message': '<h1>This is img</h1>'}
    return render(request, 'secondapp_img/home.html', context)

def map_page(request):
    context = {'message': '<h1>This is img</h1>'}
    return render(request, 'secondapp_img/map.html', context)

def detect_objects(request):
    img_path = r"C:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\firstproject\static\images\32.png"
    model_path = r"c:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\models\Mini project\shobi\data1\trained_model\train1\weights\best.pt"

  
    colors = {0: (0, 0, 255), 1: (0, 255, 0)}  # Red for 'car', Green for 'free'

    model = YOLO(model_path)

 
    results = model(img_path)

  
    car_count = 0
    free_count = 0

  
    for result in results:
        boxes = result.boxes 
        cls = boxes.cls 
        conf = boxes.conf  
        
        for box, class_id, confidence in zip(boxes.xyxy, cls, conf):
            # Check if the class ID corresponds to 'car' or 'free'
            if class_id.item() == 0:  # 'car' label
                car_count += 1
            elif class_id.item() == 1:  # 'free' label
                free_count += 1

    # Print the counts
    print(f"\nNumber of cars detected: {car_count}")
    print(f"Number of free objects detected: {free_count}")

    total = car_count + free_count
    print("Total_count:", total)

    
    image = cv2.imread(img_path)
    for result in results:
        boxes = result.boxes
        cls = boxes.cls
        for box, class_id in zip(boxes.xyxy, cls):
            x1, y1, x2, y2 = [int(x) for x in box]
            color = colors.get(class_id.item(), (255, 255, 255))  # Default color is white
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

   
    _, buffer = cv2.imencode('.png', image)
    img_str = base64.b64encode(buffer).decode('utf-8')

    return render(request, 'result.html', {'image': img_str, 'car_count': car_count, 'free_count': free_count, 'total_count': total})

#----------------------------------------result2---------------------------------------
 

def detect2_objects(request):
    img_path = r"C:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\firstproject\static\images\22.png"
    model_path = r"c:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\models\Mini project\shobi\data1\trained_model\train1\weights\best.pt"

  
    colors = {0: (0, 0, 255), 1: (0, 255, 0)}  # Red for 'car', Green for 'free'

   
    model = YOLO(model_path)

    results = model(img_path)

    car_count = 0
    free_count = 0

    for result in results:
        boxes = result.boxes  # Bounding box coordinates (xmin, ymin, xmax, ymax)
        cls = boxes.cls  # Class IDs
        conf = boxes.conf  # Confidence scores

        
        for box, class_id, confidence in zip(boxes.xyxy, cls, conf):
           
            if class_id.item() == 0:  # 'car' label
                car_count += 1
            elif class_id.item() == 1:  # 'free' label
                free_count += 1

    # Print the counts
    print(f"\nNumber of cars detected: {car_count}")
    print(f"Number of free objects detected: {free_count}")

    total = car_count + free_count
    print("Total_count:", total)

    # Display the image with bounding boxes
    image = cv2.imread(img_path)
    for result in results:
        boxes = result.boxes
        cls = boxes.cls
        for box, class_id in zip(boxes.xyxy, cls):
            x1, y1, x2, y2 = [int(x) for x in box]
            color = colors.get(class_id.item(), (255, 255, 255))  # Default color is white
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

    # Convert image data to base64 for rendering in HTML
    _, buffer = cv2.imencode('.png', image)
    img_str = base64.b64encode(buffer).decode('utf-8')

    return render(request, 'result2.html', {'image': img_str, 'car_count': car_count, 'free_count': free_count, 'total_count': total})

#------------------------------------result3----------------------------------------------
def detect3_objects(request):
    img_path = r"C:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\firstproject\static\images\24.png"
    model_path = r"c:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\models\Mini project\shobi\data1\trained_model\train1\weights\best.pt"


    colors = {0: (0, 0, 255), 1: (0, 255, 0)}  # Red for 'car', Green for 'free'

    model = YOLO(model_path)

   
    results = model(img_path)

    
    car_count = 0
    free_count = 0

    for result in results:
        boxes = result.boxes  # Bounding box coordinates (xmin, ymin, xmax, ymax)
        cls = boxes.cls  
        conf = boxes.conf  

        
        for box, class_id, confidence in zip(boxes.xyxy, cls, conf):
            
            if class_id.item() == 0:  # 'car' label
                car_count += 1
            elif class_id.item() == 1:  # 'free' label
                free_count += 1

  
    print(f"\nNumber of cars detected: {car_count}")
    print(f"Number of free objects detected: {free_count}")

    total = car_count + free_count
    print("Total_count:", total)

    
    image = cv2.imread(img_path)
    for result in results:
        boxes = result.boxes
        cls = boxes.cls
        for box, class_id in zip(boxes.xyxy, cls):
            x1, y1, x2, y2 = [int(x) for x in box]
            color = colors.get(class_id.item(), (255, 255, 255))  # Default color is white
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

   
    _, buffer = cv2.imencode('.png', image)
    img_str = base64.b64encode(buffer).decode('utf-8')

    return render(request, 'result3.html', {'image': img_str, 'car_count': car_count, 'free_count': free_count, 'total_count': total})


#-----------------------------------------------import cv2
from ultralytics import YOLO
from django.shortcuts import render
import cv2

def process_video(video_path, model_path):
    colors = {0: (0, 0, 255), 1: (0, 255, 0)}  # Red for 'car', Green for 'free'
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file.")
        return None, None

    frame_results = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame)

        car_count = 0
        free_count = 0

        for result in results:
            boxes = result.boxes
            cls = boxes.cls
            for box, class_id in zip(boxes.xyxy, cls):
                x1, y1, x2, y2 = [int(x) for x in box]
                color = colors.get(class_id.item(), (255, 255, 255))  # Default color is white
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                if class_id.item() == 0:
                    car_count += 1
                elif class_id.item() == 1:
                    free_count += 1

        frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        frame_results.append({
            'frame': frame_number,
            'car_count': car_count,
            'free_count': free_count,
            'total_count': car_count + free_count
        })

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return frame_results

def detect4_objects(request):
    video_path = r"C:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\firstproject\static\images\carPark.mp4"
    model_path =r"C:\Users\ruban\Documents\company_project\Project_4_mini\project_jango\models\Mini project\shobi\data1\trained_model\train1\weights\best.pt"

    frame_results = process_video(video_path, model_path)

    if frame_results is None:
        return render(request, 'error.html', {'message': 'Error processing video'})

    return render(request, 'result4.html', {'frame_results': frame_results})

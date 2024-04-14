import cv2
import csv
import matplotlib.pyplot as plt
import numpy as np
import imutils
import easyocr
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
img = frame
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cap.release();
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.show()

bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
edged = cv2.Canny(bfilter, 30, 200)  # Edge detection

plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
plt.show()

keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
location = None

for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2 + 1, y1:y2 + 1]

plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show()

reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
result

try:
    text = result[0][-2]
except:
    print("Sorry, Car number not detected!!")
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1] + 60),
                  fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)

plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()
print(text)
c=0
Cars = [
    {"Car_Number": "21 BH 0001 AA", "Make": "Toyota", "Model": "Camry", "Age_Of_Car": 5, "Months_without_Servicing": 5},
    {"Car_Number": "URU 580Y", "Make": "Lamborghini", "Model": "Urus", "Age_Of_Car": 7, "Months_without_Servicing": 2},
    {"Car_Number": "H982 FKL", "Make": "Porsche", "Model": "Fusion", "Age_Of_Car": 4, "Months_without_Servicing": 9},
    {"Car_Number": "MH 04 JM 8765", "Make": "Mahindra", "Model": "Verito", "Age_Of_Car": 13, "Months_without_Servicing": 4},
    {"Car_Number": "MH 20 EE 7602", "Make": "Nissan", "Model": "Altima", "Age_Of_Car": 4, "Months_without_Servicing": 3},
]

with open("Cars.csv", mode="w") as csvfile:
    new=["Car_Number","Age_Of_Car","Months_without_Servicing"]
    fieldnames = Cars[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in Cars:
        writer.writerow(row)
with open("Cars.csv",mode="r") as csvfile:
    file=csv.reader(csvfile)
    list_of_csv=list(file)
    for i in range(2,11):
        if(i%2==0):
            if(list_of_csv[i][0]==text):
                print("The Make of the Car: ",list_of_csv[i][1])
                print("The Model of the Car: ",list_of_csv[i][2])
                print("The Age of the Car:",int(list_of_csv[i][3]))
                c=c+1
                if(int(list_of_csv[i][3])>10):
                    print("Your car is quite old and may cause environmental concerns.")
                print("Months gone without Servicing:",int(list_of_csv[i][4]))
                if(int(list_of_csv[i][4])>6):
                    print("It's recommended to service your car.")
                break
    if(c==0):
        print("Car not registered in Database, Please Provide Car Info")
routes = {
    'Delhi to Kolkata': [('Delhi', 'Jaipur', 'Kolkata', 120), ('Delhi', 'Agra', 'Kolkata', 90)],
    'Amritsar to Chennai': [('Amritsar', 'Patiala', 'Chennai', 150), ('Amritsar', 'Ludhiana', 'Chennai', 110),
                            ('Amritsar', 'Jalandhar', 'Chennai', 130)],
    'Hyderabad to Bangalore': [('Hyderabad', 'Gulbarga', 'Bangalore', 80), ('Hyderabad', 'Raichur', 'Bangalore', 100),
                               ('Hyderabad', 'Bidar', 'Bangalore', 85)],
    'Mumbai to Bhubaneshwar': [('Mumbai', 'Pune', 'Bhubaneshwar', 200), ('Mumbai', 'Surat', 'Bhubaneshwar', 180),
                               ('Mumbai', 'Ahmedabad', 'Bhubaneshwar', 160),
                               ('Mumbai', 'Chennai', 'Bhubaneshwar', 190)],
    'Mumbai to Chennai': [('Mumbai', 'Pune', 'Chennai', 220), ('Mumbai', 'Bangalore', 'Chennai', 250),
                          ('Mumbai', 'Hyderabad', 'Chennai', 280)],
    'Mumbai to Bangalore': [('Mumbai', 'Pune', 'Bangalore', 120), ('Mumbai', 'Surat', 'Bangalore', 110),
                            ('Mumbai', 'Ahmedabad', 'Bangalore', 130)],
    'Mumbai to Kochi': [('Mumbai', 'Pune', 'Kochi', 300), ('Mumbai', 'Bangalore', 'Kochi', 280),
                        ('Mumbai', 'Hyderabad', 'Kochi', 320)],
    'Lucknow to Kolkata': [('Lucknow', 'Kanpur', 'Kolkata', 70), ('Lucknow', 'Allahabad', 'Kolkata', 60),
                           ('Kolkata', 'Kanpur', 'Kolkata', 70), ('Kolkata', 'Lucknow', 'Kolkata', 100),
                           ('Kolkata', 'Allahabad', 'Kolkata', 120)],
    'Lucknow to Chennai': [('Lucknow', 'Kanpur', 'Chennai', 90), ('Lucknow', 'Allahabad', 'Chennai', 80),
                           ('Chennai', 'Kanpur', 'Chennai', 110), ('Chennai', 'Lucknow', 'Chennai', 120),
                           ('Chennai', 'Allahabad', 'Chennai', 130)],
    'Lucknow to Bangalore': [('Lucknow', 'Kanpur', 'Bangalore', 120), ('Lucknow', 'Allahabad', 'Bangalore', 110),
                             ('Bangalore', 'Kanpur', 'Bangalore', 130), ('Bangalore', 'Lucknow', 'Bangalore', 140),
                             ('Bangalore', 'Allahabad', 'Bangalore', 150)],
    'Lucknow to Bhubaneshwar': [('Lucknow', 'Kanpur', 'Bhubaneshwar', 180),
                                ('Lucknow', 'Allahabad', 'Bhubaneshwar', 170),
                                ('Bhubaneshwar', 'Kanpur', 'Bhubaneshwar', 200),
                                ('Bhubaneshwar', 'Lucknow', 'Bhubaneshwar', 210),
                                ('Bhubaneshwar', 'Allahabad', 'Bhubaneshwar', 220)],
    'Lucknow to Kochi': [('Lucknow', 'Kanpur', 'Kochi', 250), ('Lucknow', 'Allahabad', 'Kochi', 240),
                         ('Kochi', 'Kanpur', 'Kochi', 270), ('Kochi', 'Lucknow', 'Kochi', 280),
                         ('Kochi', 'Allahabad', 'Kochi', 290)],
    'Delhi to Chennai': [('Delhi', 'Jaipur', 'Kolkata', 210), ('Delhi', 'Agra', 'Chennai', 180)],
    'Delhi to Bangalore': [('Delhi', 'Jaipur', 'Kolkata', 250), ('Delhi', 'Agra', 'Bangalore', 220)],
    'Delhi to Bhubaneshwar': [('Delhi', 'Jaipur', 'Kolkata', 360), ('Delhi', 'Agra', 'Bhubaneshwar', 330)],
    'Delhi to Kochi': [('Delhi', 'Jaipur', 'Kolkata', 350), ('Delhi', 'Agra', 'Kochi', 320)],
    'Amritsar to Kolkata': [('Amritsar', 'Ludhiana', 'Kolkata', 150), ('Amritsar', 'Jalandhar', 'Kolkata', 110),
                            ('Amritsar', 'Patiala', 'Kolkata', 250), ('Amritsar', 'Ludhiana', 'Kolkata', 220)],
    'Amritsar to Bangalore': [('Amritsar', 'Ludhiana', 'Chennai', 150), ('Amritsar', 'Jalandhar', 'Bangalore', 110),
                              ('Amritsar', 'Patiala', 'Bangalore', 290), ('Amritsar', 'Ludhiana', 'Bangalore', 260),
                              ('Amritsar', 'Jaipur', 'Bangalore', 230)],
    'Amritsar to Bhubaneshwar': [('Amritsar', 'Ludhiana', 'Chennai', 150),
                                 ('Amritsar', 'Jalandhar', 'Bhubaneshwar', 110),
                                 ('Amritsar', 'Patiala', 'Bhubaneshwar', 290),
                                 ('Amritsar', 'Ludhiana', 'Bhubaneshwar', 260),
                                 ('Amritsar', 'Jaipur', 'Bhubaneshwar', 230)],
    'Amritsar to Kochi': [('Amritsar', 'Ludhiana', 'Chennai', 150), ('Amritsar', 'Jalandhar', 'Kochi', 110),
                          ('Amritsar', 'Patiala', 'Kochi', 290), ('Amritsar', 'Ludhiana', 'Kochi', 260),
                          ('Amritsar', 'Jaipur', 'Kochi', 230)],
    'Hyderabad to Kolkata': [('Hyderabad', 'Gulbarga', 'Bangalore', 80), ('Hyderabad', 'Raichur', 'Bangalore', 100),
                             ('Bangalore', 'Bidar', 'Kolkata', 290), ('Bangalore', 'Raichur', 'Kolkata', 260),
                             ('Bangalore', 'Gulbarga', 'Kolkata', 230)],
    'Hyderabad to Bhubaneshwar': [('Hyderabad', 'Gulbarga', 'Bangalore', 80),
                                  ('Hyderabad', 'Raichur', 'Bangalore', 100),
                                  ('Bangalore', 'Bidar', 'Bhubaneshwar', 290),
                                  ('Bangalore', 'Raichur', 'Bhubaneshwar', 260),
                                  ('Bangalore', 'Gulbarga', 'Bhubaneshwar', 230)],
    'Hyderabad to Kochi': [('Hyderabad', 'Gulbarga', 'Bangalore', 80), ('Hyderabad', 'Raichur', 'Bangalore', 100),
                           ('Bangalore', 'Bidar', 'Kochi', 380), ('Bangalore', 'Raichur', 'Kochi', 350),
                           ('Bangalore', 'Gulbarga', 'Kochi', 320)],
    'Mumbai to Kolkata': [('Mumbai', 'Pune', 'Bhubaneshwar', 200), ('Mumbai', 'Surat', 'Bhubaneshwar', 180),
                          ('Bhubaneshwar', 'Ahmedabad', 'Kolkata', 430), ('Bhubaneshwar', 'Surat', 'Kolkata', 400),
                          ('Bhubaneshwar', 'Pune', 'Kolkata', 370)],
    'Mumbai to Kochi': [('Mumbai', 'Pune', 'Bhubaneshwar', 200), ('Mumbai', 'Surat', 'Bhubaneshwar', 180),
                        ('Bhubaneshwar', 'Ahmedabad', 'Kochi', 420), ('Bhubaneshwar', 'Surat', 'Kochi', 390),
                        ('Bhubaneshwar', 'Pune', 'Kochi', 360)],
    'Mumbai to Bangalore': [('Mumbai', 'Pune', 'Bangalore', 120), ('Mumbai', 'Surat', 'Bangalore', 110),
                            ('Bangalore', 'Ahmedabad', 'Bangalore', 130)],
    'Mumbai to Kochi': [('Mumbai', 'Pune', 'Kochi', 300), ('Mumbai', 'Bangalore', 'Kochi', 280),
                        ('Bangalore', 'Hyderabad', 'Kochi', 320)],
    'Lucknow to Kolkata': [('Lucknow', 'Kanpur', 'Kolkata', 70), ('Lucknow', 'Allahabad', 'Kolkata', 60),
                           ('Kolkata', 'Kanpur', 'Kolkata', 70), ('Kolkata', 'Lucknow', 'Kolkata', 100),
                           ('Kolkata', 'Allahabad', 'Kolkata', 120)],
    'Lucknow to Chennai': [('Lucknow', 'Kanpur', 'Chennai', 90), ('Lucknow', 'Allahabad', 'Chennai', 80),
                           ('Chennai', 'Kanpur', 'Chennai', 110), ('Chennai', 'Lucknow', 'Chennai', 120),
                           ('Chennai', 'Allahabad', 'Chennai', 130)],
    'Lucknow to Bangalore': [('Lucknow', 'Kanpur', 'Bangalore', 120), ('Lucknow', 'Allahabad', 'Bangalore', 110),
                             ('Bangalore', 'Kanpur', 'Bangalore', 130), ('Bangalore', 'Lucknow', 'Bangalore', 140),
                             ('Bangalore', 'Allahabad', 'Bangalore', 150)],
    'Lucknow to Bhubaneshwar': [('Lucknow', 'Kanpur', 'Bhubaneshwar', 180),
                                ('Lucknow', 'Allahabad', 'Bhubaneshwar', 170),
                                ('Bhubaneshwar', 'Kanpur', 'Bhubaneshwar', 200),
                                ('Bhubaneshwar', 'Lucknow', 'Bhubaneshwar', 210),
                                ('Bhubaneshwar', 'Allahabad', 'Bhubaneshwar', 220)],
    'Lucknow to Kochi': [('Lucknow', 'Kanpur', 'Kochi', 250), ('Lucknow', 'Allahabad', 'Kochi', 240),
                         ('Kochi', 'Kanpur', 'Kochi', 270), ('Kochi', 'Lucknow', 'Kochi', 280),
                         ('Kochi', 'Allahabad', 'Kochi', 290)],
}


def display_distances():
    print("Distances between places:")
    for route, distances in routes.items():
        print(f"{route}:")
        for start, _, end, distance in distances:
            print(f"  {start} to {end}: {distance} km")
        print()


def find_shortest_route(start, end):
    direct_routes = routes.get(f'{start} to {end}', [])

    if not direct_routes:
        return "Invalid input. Please enter valid routes."

    shortest_route = min(direct_routes, key=lambda x: x[3])
    return f"The greenest route from {start} to {end} is: {shortest_route[:-1]} ({shortest_route[-1]} km)"

# Take user input for starting and destination points
ch=input("Do you wish to choose a route:(Y/N) ")
if(ch=="y" or ch=="Y"):
    start_point = input("Enter starting point (Delhi, Amritsar, Hyderabad, Mumbai, Lucknow): ").capitalize()
    end_point = input("Enter destination point (Kolkata, Chennai, Bangalore, Bhubaneshwar, Kochi): ").capitalize()
    result = find_shortest_route(start_point, end_point)
    print(result)
else:
    print("Thank you for your cooperation")
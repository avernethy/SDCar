import logging
from SDCar import SDCar
import cv2
import datetime
from hand_coded_lane_follower import HandCodedLaneFollower
from objects_on_road_processor import ObjectsOnRoadProcessor

INITIAL_SPEED = 0
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

#Create all the objects
car = SDCar()

lane_follower = HandCodedLaneFollower
traffic_sign_processor = ObjectsOnRoadProcessor


fourcc = cv2.VideoWriter_fourcc(*'XVID')
datestr = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
video_orig = create_video_recorder('../data/tmp/car_video%s.avi' % datestr)
video_lane = create_video_recorder('../data/tmp/car_video_lane%s.avi' % datestr)
video_objs = create_video_recorder('../data/tmp/car_video_objs%s.avi' % datestr)
camera = cv2.VideoCapture(-1)
camera.set(3, SCREEN_WIDTH)
camera.set(4, SCREEN_HEIGHT)

while camera.isOpened():
    _, image_lane = camera.read()
    image_objs = image_lane.copy()
    i += 1
    video_orig.write(image_lane)

    image_objs = process_objects_on_road(image_objs)
    video_objs.write(image_objs)
    how_image('Detected Objects', image_objs)

    image_lane = follow_lane(image_lane)
    video_lane.write(image_lane)
    show_image('Lane Lines', image_lane)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cleanup()
        break

def create_video_recorder(path):
    return cv2.VideoWriter(path, self.fourcc, 20.0, (self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT))

def process_objects_on_road(image):
        image = traffic_sign_processor.process_objects_on_road(image)
        return image

def follow_lane(image):
        #image = self.lane_follower.follow_lane(image)
        return image

def cleanup():
    """ Reset the hardware"""
    logging.info('Stopping the car, resetting hardware.')
    
    car.stop_all()
    camera.release()
    video_orig.release()
    video_lane.release()
    video_objs.release()
    cv2.destroyAllWindows()

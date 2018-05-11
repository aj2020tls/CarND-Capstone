from math import atan
import rospy

class YawController(object):
    def __init__(self, wheel_base, steer_ratio, min_speed, max_lat_accel, max_steer_angle):
        self.wheel_base = wheel_base
        self.steer_ratio = steer_ratio
        self.min_speed = min_speed
        self.max_lat_accel = max_lat_accel

        self.min_angle = -max_steer_angle
        self.max_angle = max_steer_angle


    def get_angle(self, radius):
        angle = atan(self.wheel_base / radius) * self.steer_ratio
        return max(self.min_angle, min(self.max_angle, angle))

    def get_steering(self, linear_velocity, angular_velocity2, current_velocity):
        angular_velocity = current_velocity * angular_velocity2 / linear_velocity if abs(linear_velocity) > 0. else 0.
        #max_yaw_rate = abs(self.max_lat_accel / current_velocity);
        if abs(current_velocity) > 0.01:
            max_yaw_rate = abs(self.max_lat_accel / current_velocity);
            angular_velocity = max(-max_yaw_rate, min(max_yaw_rate, angular_velocity))
            
        angle = self.get_angle(max(current_velocity, self.min_speed) / angular_velocity) if abs(angular_velocity) > 0. else 0.0
        #if (linear_velocity<0):
        #    angle = -angle

        #if abs(current_velocity) > 0.01:        
        #    rospy.logwarn("angle = " + str(angle) + " c_v = " + str(current_velocity) + "  max_yaw = " + str(max_yaw_rate) + " angular_vel = " + str(angular_velocity) + " angular_v2 = " + str(angular_velocity2) + " linear_vel = " + str(linear_velocity))

        return angle;

# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
# due to gravity is 9.8m/s2. You can use the formula vf =
# 
# v2
# i
# + 2ad to compute the
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.

h=int(input("Enter the height here:"))

print(f"Object droped from {h}m will hit ground with speed of {pow(2*9.8*h,0.5)} ")
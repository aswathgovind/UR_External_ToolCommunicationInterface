# UR_External_ToolCommunicationInterface
I found an easy way to communicate with the rs485 port and I have documented that elaborately so that it might be easy for beginners to easily integrate their custom end-effectors with UR robots 

Transfer the URCaps file to the Robot controller with the help of this reference:-
https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/install_urcap_e_series.md

Once if the urcap file is loaded successfully you will be able see the output in the teach pendant saying that “RS-485 daemaon runs”

![rs485Output](https://user-images.githubusercontent.com/29711990/167360024-b70b887b-dfa5-4f8d-9ecb-a822d1a8c6d4.jpeg)

Once if that is achieved, use rs485_pythonInterface.py in jupyter notebook or any other python programming interface to send and receive the data in TCI from remote port.

References

https://www.tutorialspoint.com/python/python_networking.html → helped in socket python code
https://www.geeksforgeeks.org/socket-programming-python/ → helped in socket python code
https://github.com/UniversalRobots/Universal_Robots_ToolComm_Forwarder_URCap -> the urcap package that we used
https://github.com/BomMadsen/URCap-ToolCommunicationInterface → gives a code level understanding of the URCap daemon (XmlRpc, /dev/ttyTool etc)

I Hope it helped!!!

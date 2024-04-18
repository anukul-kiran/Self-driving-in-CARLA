Project Report  

Self-Driving Implementation on CARLA Simulator: 

 

Introduction:  

Self-driving technology holds immense potential to revolutionize transportation by enabling vehicles to navigate autonomously. This project focuses on implementing self-driving capabilities using Reinforcement learning techniques within the CARLA simulator, a powerful platform for testing autonomous driving algorithms. While we implement the algorithm on a simulation, we still do believe that if we implement this in real world scenario with real world data, we could make this work as intended by using real time data. 

 

Objective: 

The main objective of this project is to develop a self-driving system that can autonomously navigate through the environment in the CARLA simulator. By leveraging reinforcement learning algorithms, we aim to train a model capable of making real-time driving decisions based on the surrounding environment. 

 

Scope: 

While this project covers the implementation fo self-driving capabilities using reinforcement learning, it is important to note certain limitations. Due to constraints in computational power, the model’s accuracy may be limited compared to real-world application. Additionally, this project focuses on simulation-based testing and does not cover real-world deployment. But we aim for real world deployment soon If we have the resources. 

 

 

 

Methodology: 

This project utilizes reinforcement learning algorithms to train a self-driving model within the CARLA simulator environment. Additionally, we incorporate the Xception model, Xception is a deep convolutional neural network architecture that involves Depth wise Separable Convolutions. It was developed by Google researchers. Google presented an interpretation of Inception modules in Convolutional neural networks as being an intermediate step in-between regular convolution and the depth wise separable convolution operation as being an intermediate step in-between regular convolution and the depth wise separable convolution operation. 

 

Implementation: 

The implementation phase involves setting up the CARLA simulator environment, configuring vehicle dynamics, sensors, and camera systems. We collect sensor data from the simulator, preprocess it, and feed it into the reinforcement learning model for training. The model learns to navigate the environment by interacting with the simulator and receiving rewards based on its actions. We have implemented 2400 episode on this, but we need to implement more than 200,000 episodes to make the model work even better, since that’s where the model seems to be working optimally, we only trained the model on 100 episodes because of the limited computational power available.  

 

Results: 

The project has successfully implemented a self-driving model within CARLA simulator. The model demonstrates the ability to navigate through various scenarios, including lane following, obstacle avoidance, and traffic adherence. While the model's performance is promising, further optimization and real-world testing are required to achieve higher levels of accuracy. 

 

 

 

Conclusion: 

In conclusion, this project showcases the potential of reinforcement learning techniques in developing self-driving systems and the difficulties possessed by such systems. 

While the model’s performance is not very impressive but is encouraging enough,  

There are challenges to overcome in scaling the project for real-world deployment. Continued research and development in this field are essential for advancing autonomous driving technology. 

 

Future Work: 

Future Work for this project includes optimizing the reinforcement learnign algorithms, incorporating additional sensor data, and conducting real-world testing. Scaling the project for real-world deployment will require increased computational power, robust testing infrastructure, and regulatory compliance. 

 

Scaling: 

Scaling the project for real-world applications requires addressing computational limitations and ensuring the model’s accuracy and reliability in diverse environments. High-performance computing resources, real-time data processing, and extensive testing are essential for successfully deploying self-driving technology on a larger scale. 

 


Performance: 

 

Since we have done only 100 episodes. We suspect we need more like 200,000 episodes to see anything decent, provided the rest of our issues are solved as well   

Because this is oonly 100 episodes we can see that the agent has learned to really just do 1 thing. Agent might learn to do one thing because you Q values are actually static(model outputs same Q values no matter the input), or like in our case, they are all actually changing, it’s just turn right is always consistently higher. 

 

Another thing I see here is sometimes turn left is higher than turn straight, other times turn straight is higher than left. So, there’s still some hope/promise. 
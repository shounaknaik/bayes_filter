## What we want to do?

You have a robot that has a camera and a manipulator arm. The camera and sensor suite are configured
to detect if the door is open or not. Similarly, the manipulator arm is a simple piston which may push the
door to open it. The robot is being used to monitor the state of the door. Mathematically, the system
state (𝑥𝑡 ) corresponds to the door being open or closed, the measurement (𝑧𝑡 ) is also the door being
open or closed, and the input to the system (𝑢𝑡 ) is either nothing or a push on the door. Since this is a
binary state, we can simply map this to zero or one for the sake of mathematical representation.
Table 2: State mappings to binary.

<table>
  <tr>
      <td align = "center" rowspan ="2"> 𝑥𝑡</td>
      <td align = "center">Closed</td>
      <td align = "center">0</td>
  </tr>
  <tr>
      <td align = "center">Open</td>
      <td align = "center">1</td>
  </tr>
  <tr>
      <td align = "center" rowspan ="2"> 𝑧𝑡</td>
      <td align = "center">Closed</td>
      <td align = "center">0</td>
  </tr>
  <tr>
      <td align = "center">Open</td>
      <td align = "center">1</td>
  </tr>
  <tr>
      <td align = "center" rowspan ="2"> 𝑢𝑡</td>
      <td align = "center">Closed</td>
      <td align = "center">0</td>
  </tr>
  <tr>
      <td align = "center">Open</td>
      <td align = "center">1</td>
  </tr>
</table>
However, the robot’s camera is a low quality black and white camera with a poorly tuned sensor model.
Thus, it cannot always accurately detect when the door is open. The robot has a true positive rate (sense
open when the door is open) of 0.6, and a true negative rate (sense closed when the door is closed) of
0.8. Being binary events, the false positive and false negative rates must in turn sum to zero. The sensor
model probabilities are summarized below.

𝑝(𝑧𝑡 = 1 |𝑥𝑡 = 1) = 0.6
𝑝(𝑧𝑡 = 0 |𝑥𝑡 = 1) = 0.4
𝑝(𝑧𝑡 = 1 |𝑥𝑡 = 0) = 0.2
𝑝(𝑧𝑡 = 0 |𝑥𝑡 = 0) = 0.8
The robot can also use its manipulator to affect the state of the door. Again, this manipulator is not
perfect and will have varying success given the actual state of the door. If the robot takes no action (𝑢𝑡 =
0) the door’s state will remain the same. Similarly, if the door is already open (𝑥𝑡 = 1) and the robot
pushes (𝑢𝑡 = 1) the door will remain open. Conversely, if the door is closed, the robot will open the door
with a probability of 0.8.


## Use your code to answer the following questions:
1. If the robot always takes the action “do nothing” and always receives the measurement “door
open” how many iterations will it take before the robot is at least 99.99% certain the door is
open?
2. If the robot always takes the action “push” and always receives the measurement “door open”
how many iterations will it take before the robot is at least 99.99% certain the door is open?
3. If the robot always takes the action “push” and always receives the measurement “door closed”
what is the steady state belief about the door? Include both the state and the certainty.

## Answer to Q3
The estimate would be the door would be open with probability of 1. The action push triggers a belief in the system that the door is now open. As this belief starts to increase, the belief that the door is closed starts to decrease. Eventually this leads to a complete faith that the door is open. 



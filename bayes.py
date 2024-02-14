def prediction_step(prior_belief, action):
    """
    Prediction step of the Bayes Filter algorithm.
    This calculates with all possible states x_t
    
    Args:
    prior_belief (float): Prior belief probability of the door being open.
    action (int): Action taken by the robot. 0 for "do nothing" and 1 for "push". We should know this.
    
    Returns:
    float: Updated prior belief probability after prediction.
    """
    # If action is "do nothing", the prior belief remains unchanged
    if action == 0:
        # belief that door is open*prob(door is open given do nothing,door is open) + belief that door is closed*prob(door is closed given do nothing, door is open)
        return prior_belief * 1 + (1 - prior_belief) * 0
    # Open*prior_belief_open + prior_belief_closed*pushed_open
    return 1 * prior_belief + 0.8 * (1 - prior_belief)


def measurement_update_step(prior_belief, measurement):
    """
    Measurement update step of the Bayes Filter algorithm.
    
    Args:
    prior_belief (float): Prior belief probability of the door being open.
    measurement (int): Measurement received by the robot. 0 for "door closed" and 1 for "door open".
    
    Returns:
    float: Updated belief probability after measurement update.
    """
    # Update belief based on the sensor model probabilities
    if measurement == 1:
        # total prob is belief_that_door_is_open*sensor_error + belief that door is closed*sensor_error
        total_prob = 0.6 * prior_belief + 0.2*(1-prior_belief)
        likelihood = 0.6*prior_belief/total_prob

    else:
        # total prob is belief_that_door_is_open*sensor_error + belief that door is closed*sensor_error
        total_prob = 0.4 * prior_belief + 0.8*(1-prior_belief)
        likelihood = 0.4 * prior_belief/total_prob
    
    return likelihood


def bayes_filter(iterations, initial_belief=0.5, action_sequence=None, measurement_sequence=None):
    """
    Perform Bayes Filter algorithm for a given number of iterations.
    
    Args:
    iterations (int): Number of iterations to run the Bayes Filter algorithm.
    initial_belief (float): Initial belief probability of the door being open. Default is 0.5.
    action_sequence (list): Sequence of actions taken by the robot. 0 for "do nothing" and 1 for "push".
    measurement_sequence (list): Sequence of measurements received by the robot. 0 for "door closed" and 1 for "door open".
    
    Returns:
    float: Final belief probability after the specified number of iterations.
    """
    assert action_sequence is not None and measurement_sequence is not None, "Action and measurement sequences must be provided"
    assert len(action_sequence) == len(measurement_sequence), "Action and measurement sequences must have the same length"
    
    belief_li =[]
    belief = initial_belief
    
    for i in range(iterations):
        # Perform prediction step
        belief = prediction_step(belief, action_sequence[i])
        
        # Perform measurement update step
        belief = measurement_update_step(belief, measurement_sequence[i])
        belief_li.append(belief)
        
    return belief_li


# Answering the questions

# Question 1: If the robot always takes the action “do nothing” and always receives the measurement “door open”, 
# how many iterations will it take before the robot is at least 99.99% certain the door is open?

action_sequence_q1 = [0] * 1000  # Always "do nothing"
measurement_sequence_q1 = [1] * 1000  # Always "door open"
final_belief_q1 = bayes_filter(1000, action_sequence=action_sequence_q1, measurement_sequence=measurement_sequence_q1)
print("Question 1:")
print("Iterations to be 99.99% certain the door is open:", next(i for i, belief in enumerate(final_belief_q1) if belief >= 0.9999))

# Question 2: If the robot always takes the action “push” and always receives the measurement “door open”, 
# how many iterations will it take before the robot is at least 99.99% certain the door is open?

action_sequence_q2 = [1] * 1000  # Always "push"
measurement_sequence_q2 = [1] * 1000  # Always "door open"
final_belief_q2 = bayes_filter(1000, action_sequence=action_sequence_q2, measurement_sequence=measurement_sequence_q2)
print("\nQuestion 2:")
print("Iterations to be 99.99% certain the door is open:", next(i for i, belief in enumerate(final_belief_q2) if belief >= 0.9999))

# Question 3: If the robot always takes the action “push” and always receives the measurement “door closed”, 
# what is the steady state belief about the door? Include both the state and the certainty.

action_sequence_q3 = [1] * 1000       # Always "push"
measurement_sequence_q3 = [0] * 1000  # Always "door closed"
final_belief_q3 = bayes_filter(1000, action_sequence=action_sequence_q3, measurement_sequence=measurement_sequence_q3)
print("\nQuestion 3:")
print("Steady state belief about the door being open is:", final_belief_q3[-1])

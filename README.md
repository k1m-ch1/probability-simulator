# probability-simulator
simulates binomial and geometric probability with animation

# Get started
- clone this repository and install the necessary dependecies

```
pip install -r requirements.txt
```

# Distributions
## Geometric distribution
This will run the probability until you get n amount of successes and will record the amount of times you have to run the probability until you get a success.
For example if you flip a coin over and over again until you get a heads and got a heads on the **3rd** try. The bar at **3** will increase by one.
Find more about Geometric distribution here: https://en.wikipedia.org/wiki/Geometric_distribution 

## Binomial distribution
Thiswill run the probability n amount of times and record the number of successes into the bar.
For example if you flip a coin **10** times and got **6** heads, the bar at **6** will increase by 1.

## Initializing Geometric distribution
```
import probsim
X = probsim.GeometricDistribution(0.3, 10_000)
# 0.3 is the probability, 10_000 is the max frame and is also the amount of successes for this simulation
```
## Simulating Geometric distribution
This will run the probability and graph it out.
```
X.simulate()
```
Output:
![image](https://github.com/k1m-ch1/probability-simulator/assets/116435978/93af9940-c8db-486d-9e5d-75ee75094b16)

## Theoretical Binomial Distribution
This won't run the probability but will give the theoretical probability that you will get. According to this formula
$$
P(X = k) = (1-p)^{k-1} \times p
$$
```
X.get_theoretical_probability()
```
Output:
![image](https://github.com/k1m-ch1/probability-simulator/assets/116435978/b8843239-d249-4b56-80a5-dadc528c1706)

## Playing adding value animation
This will add the value one by one until the maximum number of successes is reached (aka the max frame).
```
# If return_anim is true, then it won't play the animation and will return the animation object, otherwise it will play the animation. Default is False
X.play_adding_value_animation(return_anim=True)
```

Output:





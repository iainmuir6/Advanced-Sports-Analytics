<p align='center'>
  <img src="https://upload.wikimedia.org/wikipedia/en/8/85/PFF-Logo-White-1_reduced.png" width="200"/>
</p>  

# STAT4800 - Advanced Sports Analytics

## Course Objectives

Explore sports analytics through advanced statistical methods, including simulation, markov chains, generalized linear models, and mixture models. Deliverables include biweekly homeworks and mainly a final project, aimed to create an Expected Points Added Model.

## Homework

1. Expected Points Model
2. Markov Chains – College Football Ranking
3. Hockey Shot Rates

## Final Project

### Question of Interest
Is there an optimal split between running and pass plays in college football to maximize expected points?

### Results Summary

Check out the final project write-up, titled 'Sports Analytics Project Writeup.pdf', to see a more detailed report of our findings. Attached below are some visualization of our key findings:

Specifically with regard to our Question of Interest, it is apparent that leaning more on run plays generally results in greater expected points. As shown in the figure below, the expected points when running the ball 75% of the time was almost exclusively higher than that of running the ball 25% of the time. Especially for short yardage situations, run plays dominate pass plays. Although not depicted, a 50/50 split of run and pass plays falls in between these values as expected.   
<p align='center'>
  <img src="https://github.com/iainmuir6/Advanced-Sports-Analytics/blob/master/snippets/run_pass_diff.png" width="400"/> <br>
  <img src="https://github.com/iainmuir6/Advanced-Sports-Analytics/blob/master/snippets/completion_pct.png" width="500"/>
</p> 

The following sets of graphs show density plots for passes and runs, broken down by down and yards to a first down (segmented into short, medium, and long).
<p align='center'>
  <img src="https://github.com/iainmuir6/Advanced-Sports-Analytics/blob/master/snippets/runs.png" width="400"/>
  <img src="https://github.com/iainmuir6/Advanced-Sports-Analytics/blob/master/snippets/pass.png" width="400"/>
</p>  

Our Expected Points Added model appears to be performing quite well. For evidently advantageous situations, the model outputs a number close to 7, while the model outputs close to -3 for disadvantageous situations. For example, 1st and 10 on your opponents 10 should yield around 6 expected points, while 4 and 10 on your own 10 should likely yield negative; this is because the offensive team will punt and give the opponent good field position. This spectrum of expected points added is visualized below:  
<p align='center'>
  <img src="https://github.com/iainmuir6/Advanced-Sports-Analytics/blob/master/snippets/epa_x_position.png" width="700"/>
</p> 

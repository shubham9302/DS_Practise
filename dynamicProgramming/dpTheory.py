"""
Dp or Dynamic Programming is an enhanced Recursion Problem .
When you break a big problem into multiple smaller problem then
it is called recursion

### Tricks for identifying DP/Recursive  problem
1. If have to find something optimal like max,min etc.
2.If we are given choices like whether to include the element or exclude the element
3.If recursive call is doing 2 or more function calls then it has a probability that
we can apply DP in this case

###DP problems:
1. 0/1 knapsack : In this problem ,while doing the optimisation ,we can only use one
full instance of object
2. Unbounded knapsack : In this problem ,while doing the optimisation ,we can  use one or more
full instance of the same object.
3.Fraction Knapsack : In this problem ,while doing the optimisation ,we can also
use partial instance of object. This problem comes under greedy problem approach

### 0/1 Knapsack Problem:
While solving any DP problem ,we would first write the recursive solution as
its a enhanced recursion only.
If we do recursion + storage that is DP

###Recursion
While doing recursive solution we should always try to bifurcate the
solution in 2 parts
1.Base Condition -> This means min possible valid input values for the constraints
2.Choice Diagram -> As we are optimizing ,thus choices are available to us ,so which
try to create flow diagram with all the available choices at our disposal

Once the recursion solution is done ,we can move to memoization .

### Memoization :
In this solution ,we would try to create a matrix with dimension corresponding to
entities which are changing in our recursive solution
Which should initialize all the matrix value with -1
and while doing recursion if we get result for any matrix which should
update the matrix value

"""
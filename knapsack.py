def knapsack(values,weights,capacity):

      dp = [ _ for _ in range(len(weights))]

      dp[0]=capacity
      temp = 0 
      for i in range(1,len(weights)):
            if values[i] > temp and weights[i] <= dp[i-1]:
                  temp = values[i]
                  dp [i] = dp[i-1] - weights[i]
            else :
                  temp = temp + values[i]
                  dp[i] = dp[i] - weights[i]

      return temp 

values = [60, 100, 120, 150]
weights = [10, 20, 30, 50]
capacity = 50

# Output the result
print("Maximum value that can be packed in the truck:", knapsack(values, weights, capacity))
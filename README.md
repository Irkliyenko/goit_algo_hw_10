## Monte Carlo Integration vs. SciPy's quad Function

In this homework, I implemented Monte Carlo integration to estimate the definite integral of a function and compared the results with SciPy's `quad` function. The Monte Carlo integration was performed using random sampling to estimate the integral. The results were obtained by generating a large number of random points within the specified range and calculating the average function value multiplied by the total area. SciPy's `quad` function was used for numerical integration. This function provides an accurate result for definite integrals by employing sophisticated algorithms under the hood.

## Results and Conclusion

After running the Monte Carlo integration with 1,000,000, 100,000, and 10,000 random points, I obtained the results presented in Table 1. The results of the experiment were comparable to the result from SciPy's quad function, which was 2.66667. The results from Monte Carlo integration were close to the values obtained from SciPy's quad function; however, we can see that when we decrease the number of random points, the difference between quad and Monte Carlo is growing. The discrepancy can be attributed to the probabilistic nature of the Monte Carlo method. To achieve a more optimal result, more randomly generated data and experiments are needed. It's essential to consider the trade-offs between different integration methods based on the precision required and computational efficiency.

**Table 1: Results Obtained with Monte Carlo Integration vs Numerical Integration with SciPy's `quad`.**

| Integration  | 10_000  | 100_000 | 1_000_000 |
| ------------ | ------- | ------- | --------- |
| Monte Carlo  | 2.69840 | 2.67072 | 2.66303   |
| SciPy `quad` | 2.66667 | 2.66667 | 2.66667   |

---

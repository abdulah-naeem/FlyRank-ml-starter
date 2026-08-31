# Week 06: Explain It Like You Built It

**Topic:** The Random Forest Model (from ML-08 Week 5 Build)

**Explanation:**
A random forest is basically an ensemble method that uses multiple decision trees to make a decision, and then makes its prediction based on the one with the most votes.

*(Context: In our pipeline, instead of relying on one single rigid rule to flag underperforming web pages, we use this "crowd of trees" to look at different signals like staleness and CTR, and then rank the pages based on what percentage of the trees voted that the page is declining.)*

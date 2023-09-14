# CMPS 2200  Recitation 02

**Name (Team Member 1):**__Cameron McLaren______  
**Name (Team Member 2):**__Kayla Willis________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**
f(n) = 1

root: 1
level 1: 2 * 1
O(n)


f(n) = log(n)

root: log(n)
level 1: log(n/2)
O(logn(n))


f(n) = n

root: n
level 1: (n/2) + (n/2)
O(nlog(n))


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asymptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**
if a = 2 and b = 2:

c < logb(a) --> logb(a) = 1

W(n) = 2W(n/2) + n^log2(1) simplifies to W(n) = 2W(n/2) + 1 since n^0 = 1.

Hence:
root = 1
level = 2 * 1

W(n) = O(n)

c = logb(a)

W(n) = 2W(n/2) + n^log2(2) simplifies to W(n) = 2W(n/2) + n since n^1 = n.

Therefore:
root = n
level 1 = (n/2) + (n/2) + n

W(n) = O(nlogn)

c > logb(a):

W(n) = 2W(n/2) + n^log2(4) simplifies W(n) = 2W(n/2) + n^2 since log2(4) = 2.

Thus:
root = n^2
level 1 = (n/2)^2 + (n/2)^2 = n^2/2

W(n) = O(n^2)

Our tabulate didn't work in the IDE and Replit was throwing indentation errors that the IDE did not have.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
f(n) = 1:

S(n) = O(logn) since we know the tree is balanced, so we know that the height is log(n), which would give us the span

f(n) = log(n)

S(n) = O(logn)

f(n) = n

S(n) = O(n^2) since the root 

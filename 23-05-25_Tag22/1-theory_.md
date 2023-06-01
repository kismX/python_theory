**Today** 
- 



## Closures  ##weiter

- when invoked, *make average* returns an *average* func object

...

note that **series** is a local variable of *make_averager* because the assignment **series** = [] happens in the body of that func

But when *avg(10)* is called, *make_averageer* has already returned, and irs local scope is a long gone.
whithin *averager* , **series** is a *free variable*

![closure] ein img

*The closure of the average extends the sope of that func to include the binding for the free var series*





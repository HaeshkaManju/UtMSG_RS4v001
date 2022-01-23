'''
This file shall handle random result generation for weighted results.
The intent is to start off rather simple in execution, using hard-coded data,
then move up to making the system more contextual.
Weighted Results refers to the System (Game) process where there's a standard set of results,
but one or more results gain additional "weight" thereby skewing the statistical odds of rolling
that particular result.

Common example of this: When scouting a new grid, there's an equal chance of finding:
- The Settlement in the Grid,
- A Hostile Encounter,
- A Resource Node (if it's not a Plains Grid.)

Because there are three possibilities, there should be a roughly 33% chance of any result.
If, due to the month's events, or some other effect: one of the results has "an additional weight" (let's say: Resource Nodes has the additional weight), then the list of possibilities would look like this:
- Settlement,
- Encounter,
- Resource Node,
- Resource Node.

This means that each result has a 25% chance of happening, with Resource Nodes occupying two of those potential results - thus Resource Nodes would have a 50% chance of being the result.
'''

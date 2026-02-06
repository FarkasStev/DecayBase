# DecayBase
Codebase decay simulator

## A model of a codebase

- number of modules
- average function size
- dependency graph density
- test coverage
- documentation quality
- team size / churn

just data structures.

## A set of actions (decisions)

Each “turn” you choose actions like:
- add feature
- refactor
- skip tests
- onboard new dev
- rush a deadline

Each action has side effects, for example:

Adding a feature:
- value
- complexity
- coupling

Skipping tests:
- short-term velocity
- long-term bug rate

These effects compound.

## Decay rules

- complexity increases bug probability non-linearly
- high coupling increases cost of change
- high churn increases defect rate
- delayed refactors become exponentially harder


## Time simulation

simulate weeks/months:
- apply decay every step
- introduce random events (prod incident, deadline, key dev leaves)
- observe emergent behavior
don’t hardcode outcomes — let them emerge.

## Output / insight layer

The output could be:
- graphs over time
- “project health score”
- narrative summaries:

> “Velocity collapsed after month 8 due to compounding coupling.”



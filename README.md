# graph-floude-method
Finding the shortest path in the graph with Floude's method

***example 1***
```python

    |   1       2       3       4
----|-----------------------------
  1 |  0	4	0	2
  2 |  0	0	6	0
  3 |  0	0	0	0
  4 |  0	1	10	0

Status = Compete
0->1: Weight = 3.0;
Paths = '0 -> 3 -> 1'
MinPaths: '0 -> 3 -> 1'

Status = Compete
1->2: Weight = 6.0;
Paths = '1 -> 2'
MinPaths = '1 -> 2'

Status = Compete
0->3: Weight = 2.0
Paths = '0 -> 3'
MinPaths = '0 -> 3'

Status = Compete
0->2: Weight = 9.0
Paths = '0 -> 3 -> 1 -> 2'
MinPaths = '0 -> 3 -> 1 -> 2'
```

***example2***
```python

    |   1       2       3       4       5       6       7       8
----|------------------------------------------------------------
  1 |  0	10	20	0	20	0	0	0
  2 |  10	0	0	20	0	0	0	0
  3 |  10	0	0	0	0	20	0	0
  4 |  0	10	0	0	20	0	20	0
  5 |  10	0	0	20	0	20	0	0
  6 |  0	0	10	0	20	0	0	20
  7 |  0	0	0	10	0	0	0	20
  8 |  0	0	0	0	0	20	3	0

Status = Compete
0->5: Weight = 40.0
Paths = ['0 -> 4 -> 5', '0 -> 2 -> 5']
MinPaths = '0 -> 4 -> 5', '0 -> 2 -> 5')
```

***example 3***
```python
    |   1       2       3       4       5
----|------------------------------------
  1 |  0	0	0	1	1
  2 |  0	0	0	0	0
  3 |  0	1	0	0	0
  4 |  0	0	1	0	0
  5 |  0	2	0	0	0

Status = Compete
0->1: Weight = 3.0
Paths = ['0 -> 4 -> 1', '0 -> 3 -> 2 -> 1']
MinPaths = ['0 -> 4 -> 1', '0 -> 3 -> 2 -> 1']
```

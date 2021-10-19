# graph-floude-method
Finding the shortest path in the graph with Floude's method

***example 1***
```python
0	4	0	2
0	0	6	0
0	0	0	0
0	1	10	0

status - Compete
0->1: weight = 3.0;
paths: ('0 -> 3 -> 1',);
min_paths: ('0 -> 3 -> 1',);

status - Compete
1->2: weight = 6.0;
paths: ('1 -> 2',);
min_paths: ('1 -> 2',);

status - Compete
0->3: weight = 2.0;
paths: ('0 -> 3',);
min_paths: ('0 -> 3',);

status - Compete
0->2: weight = 9.0;
paths: ('0 -> 3 -> 1 -> 2',);
min_paths: ('0 -> 3 -> 1 -> 2',);
```

***example2***
```python
0	10	20	0	20	0	0	0
10	0	0	20	0	0	0	0
10	0	0	0	0	20	0	0
0	10	0	0	20	0	20	0
10	0	0	20	0	20	0	0
0	0	10	0	20	0	0	20
0	0	0	10	0	0	0	20
0	0	0	0	0	20	3	0

status - Compete
0->5: weight = 40.0;
paths: ('0 -> 4 -> 5', '0 -> 2 -> 5');
min_paths: ('0 -> 4 -> 5', '0 -> 2 -> 5');
```

***example 3***
```python
0	0	0	1	1
0	0	0	0	0
0	1	0	0	0
0	0	1	0	0
0	2	0	0	0

status - Compete
0->1: weight = 3.0;
paths: ('0 -> 4 -> 1', '0 -> 3 -> 2 -> 1');
min_paths: ('0 -> 4 -> 1', '0 -> 3 -> 2 -> 1');
```
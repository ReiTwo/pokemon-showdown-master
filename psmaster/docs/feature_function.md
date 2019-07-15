# Feature function

## **x**(*s*): vector of features visible when in state *s*

This binary representation is constructed by first assigning indices, from 1 to *k*, to all states. Then, the binary encoding of the state index is used as a feature vector to represent that state. The length of a feature vector is determined by the total number of states.

**My active pokemon**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>0* | | 1 | 0 |
| *s<sub>1* | | 1 | 0 |
| *s<sub>2* | | 1 | 0 |
| *s<sub>3* | | 1 | 0 |
| *s<sub>4* | | 1 | 0 |
| *s<sub>5* | | 1 | 0 |
| *s<sub>6* | | 1 | 0 |
| *s<sub>7* | | 1 | 0 |
| *s<sub>8* | | 1 | 0 |
| *s<sub>9* | | 1 | 0 |

## **x**(*s*, *a*): vector of features visible when in state *s* taking action *a*

A common way to derive an action-feature vector **x**(*s*, *a*) from a state-feature vector **x**(*s*) involves an action-feature vector of size *n*|*A*|, where *n* is the number of state features and |*A*| is the number of actions. Each action corresponds with a block of *n* features in this action-feature vector. The features in **x**(*s*, *a*) that corresponds to action *a* take on the values of the state features; the features corresponding to other actions have a value of 0.

# hd-repo

```bash {cmd=true}
date
```

```javascript {cmd="node"}
const date = Date.now()
console.log(date.toString())
```

```gnuplot {cmd=true output="html"}
set terminal svg
set title "Simple Plots" font ",20"
set key left box
set samples 50
set style data points

plot [-10:10] sin(x),atan(x),cos(atan(x))

```

```python {cmd=true id="izdlk700"}
x = 1
```

```python {cmd=true id="izdlkdim"}
x = 2
```

```python {cmd=true continue="izdlk700" id="izdlkhso"}
print(x) # will print 1
```

```python {cmd=true matplotlib=true}
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show() # show figure
```


```gnuplot {cmd=true output="html"}
set terminal svg
set title "Simple Plots" font ",20"
set key left box
set samples 50
set style data points

plot [-10:10] sin(x),atan(x),cos(atan(x))
```
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
a = [1, 2, 3, 4] 
b = [5, 6, 7, 8]

plt.plot(a, b, 'b--', label = 'aa')
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('this is a demo')
plt.legend() # 将样例显示出来

plt.plot()
plt.show()
```


```gnuplot {cmd=true output="html"}
set terminal svg
set title "Simple Plots" font ",20"
set key left box
set samples 50
set style data points

plot [-10:10] sin(x),atan(x),cos(atan(x))
```
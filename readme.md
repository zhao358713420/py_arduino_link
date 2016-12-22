## 利用python从arduino中读取数据
这是一个利用python从arduino中读取信息的例子。

## 运行要求
- python3
- 安装pyserial
```
$pip install pyserial
```
- 烧录example.ino进arduino开发板
- 将example.py中的串行接口`com3`改成自己的开发板接口

## 解释
example.py中
- `ser = serial.Serial('COM3', 9600)`

    将程序与arduino开发板连接
- `ser.readline()`是指从arduino读取一行信息，类型为String，该信息对应于example.ino中的
```
Serial.print(val1);
Serial.print(" ");
Serial.print(val2);
Serial.print("\n");
```

## 博客地址<br>
http://www.stoneway.cn/2016/12/22/35/
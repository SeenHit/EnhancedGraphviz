# EnhancedGraphviz
对graphviz相关功能的二次封装，通过简化流程达到提高效率的目标

# TODO:
1, 根据个人需要增加定制性，增加定制化的使用场景  <br/>
2, 优化代码 （格式等）   <br/>
3，使能更多的graphviz的功能，使其功能更加完备  <br/>
4，直接对接其他模块，一键生成图片   <br/>
5, 增加更多的注释，包括graphviz官网参考, 以及依赖包等   <br/>


# 配置声明节点用法：
直接在init.cfg里面声明节点，会自动生成有向图   <br/>
节点有两种声明方式    <br/>
a b   // 代表a to b   <br/>

a  <br/>
b   <br/>
//  这种上下隔一行的方式也代表 a to b  <br/>

# 脚本使用方法:
mkdir Mytest  <br/>
python3 EnhancedGraphViz.py  <br/>
会自动在当前目录下的 Mytest目录下，生成一个名字为 MyPicture.png 的有向图  <br/>

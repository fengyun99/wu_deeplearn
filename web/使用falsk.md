1.安装
```bash
pip3 install flask
```
1.1依赖wsgi----web服务网关接口
1.2使用flask实现

## 总结
1. flask框架是基于werkzeug的wsgi实现
2. 用户请求到达，就调用app.__call__方法
3. 流程
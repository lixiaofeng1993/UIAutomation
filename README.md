# UIAutomation框架

### 环境
```
python                  3.6.5
unittest    
selenium                3.11.0   
appium工具              1.10.0
BeautifulReport     运行case，生成html报告
```

#### 元素定位方法

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"



#### 命名规范： 见名知意 下划线命名法
    

    case    test_*.py
    page    page_*.py
        元素  *_loc
        点击  click_*()
        输入  input_*()
        获取文本    text_*()
        定位元素 element_*()
        定位一组元素  elements_*()
        弹框  alert_*()
        鼠标悬停    move_*()
        下拉框 select_*()
        切换  switch_*()


#### 目录结构
    case
        test_*
            测试用例;
    common  公共函数
        basics
            [基于原生的selenium框架做二次封装](https://www.cnblogs.com/changqing8023/p/10153156.html);
        connectDB
            连接数据库,返回 dict 和 str 指定sql删除测试数据;
        ID_code
            识别验证码；      未完善
        logger
            日志模块;
        readConfig
            读取配置文件;
    config
        cfg.ini
            配置文件;
    data
        存放需要参数化的测试数据;
    driver
        浏览器驱动，grid服务；
    logs
        存放 log 日志;
    page
        页面元素定位封装
    report
        存放结果报告;
        img
            截图保存路径；
    tmp
        临时文件；
    run_this
        运行测试case，生成报告,发送 email;

### 示例：
<a href="https://www.cnblogs.com/changqing8023/p/10153371.html">BeautifulReport 实现app UI自动化测试</a>
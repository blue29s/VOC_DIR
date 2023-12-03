# VOC_DIR 用于 YOLO 数据集创建
### 如何使用

#### 1.使用时请将下列文件夹清空
    ├─DateSet
    ├─Images
    ├─labels_txt
    ├─labels_xml
    └─Video
#### 2.将自己的视频放入Video文件夹
![将自己的视频放入Video文件夹](/0.README_img/2.png)
#### 3.将视频准换为图片(删除无效图片)
    python VideoToImage.py
![将视频准换为图片](/0.README_img/3.png)
#### labelimg标注数据集
![labelimg标注数据集](/0.README_img/4.png)
#### 5.转换xml为txt格式(修改类别)
![转换xml为txt格式(修改类别)](/0.README_img/5.png)    

    python xml_to_txt.py

![转换xml为txt格式(修改类别)](/0.README_img/5.1.png)      
#### 6.通过labels_txt与images构建DateSet数据集得到如下目录
    python Dateset_init.py
![转换xml为txt格式(修改类别)](/0.README_img/6.png)
### 文件类型讲解

#### 文件夹目录：
![文件夹目录：](/0.README_img/7.png)

#### DateSet目录:

    ├─images        
    │  ├─test       图片文件：测试集
    │  ├─train      图片文件：训练集
    │  └─val        图片文件：验证集
    |
    └─labels        
        ├─test      标签文件：测试集
        ├─train     标签文件：训练集
        └─val       标签文件：验证集
#### images文件夹：
    用于存放使用 labelimg 标注的数据集图片。
#### lables_xml:
    使用 labelimg 标注 xml类型文件     #方便查看特征
#### lables_txt:
    用于 labelimg 标注 txt类型文件     #用于 yolo 分类训练
#### Video文件夹：
    视频文件
#### dateset_init.py：
    ├─images
    └─labels_txt
    将上述文件夹分别转为对应的 测试集，训练集，验证集
    ├─images        
    │  ├─test       图片文件：测试集
    │  ├─train      图片文件：训练集
    │  └─val        图片文件：验证集
    |
    └─labels        
        ├─test      标签文件：测试集
        ├─train     标签文件：训练集
        └─val       标签文件：验证集
#### VideoToImage.py：
    用于将 Video 文件夹目录下的视频转化为图片
#### xml_to_txt.py：
    用于将 labelimg 标注完的 xml文件 转为 yolo训练使用的 txt文件格式
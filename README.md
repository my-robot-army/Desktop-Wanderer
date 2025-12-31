# Desktop-Wanderer
基于视觉引导的移动操作机器人系统，能够自主搜索、跟踪和抓取网球。

## 功能特性
🎯 视觉目标检测  
基于YOLO神经网络实时检测网球  
支持50 FPS处理频率  
硬件加速：支持ONNX CPU推理和Atlas 310B NPU推理

🤖 自主导航  
视觉伺服控制：机器人自动导航至目标位置  
智能搜索：球消失时根据最后位置进行方向性搜索  
分层控制策略：优先旋转对齐，再进行前后移动  

🦾 双模式机械臂控制  
ACT模式：基于Action Chunking Transformer的端到端学习策略  
逆运动学模式：基于P控制的8步抓取序列

⚡ 实时控制
50 FPS精确控制循环  
状态机架构：SEARCH ↔ CATCH状态切换
## 系统架构
```
Desktop-Wanderer/  
├── src/  
│   ├── main.py                 # 主控制循环  
│   ├── setup.py               # 配置管理  
│   ├── robot_setup.py         # 机器人接口  
│   ├── move_controller.py     # 移动控制  
│   ├── arm_act_controller.py  # ACT策略控制器  
│   ├── arm_inverse_controller.py # 逆运动学控制器  
│   ├── yolov/                 # YOLO检测模块  
│   └── lekiwi/               # 硬件抽象层  
├── config.yaml               # 配置文件  
└── README.md  
```

## 分层架构
应用层：主控制逻辑和状态机  
控制层：视觉处理、导航、机械臂控制  
抽象层：机器人接口、配置管理  
硬件层：电机控制、相机访问
## 安装配置
### 环境要求
Python 3.10  
OpenCV  
PyTorch (ACT模式)  
LeRobot框架  
串口通信库
## 配置文件
编辑 config.yaml：
```
# 硬件模式：normal (CPU) 或 310b (NPU)  
hardware_mode: 'normal'  
  
# 控制模式：act (学习策略) 或 inverse (逆运动学)  
control_mode: 'inverse'  
  
# 串口配置  
port: '/dev/ttyUSB0'  
  
# 日志级别  
log_level: 'INFO'
```
## 使用方法
### 启动系统
```commandline
python -m src.main
```
操作流程  
初始化：系统加载配置，初始化机器人连接  
搜索模式：机器人自主搜索网球  
抓取模式：检测到目标后执行抓取序列  
循环运行：返回搜索模式继续任务  
键盘控制（可选）  

支持键盘遥操作控制：
W/S：前进/后退  
A/D：左移/右移  
Q/E：左转/右转  
[/]：减速/加速  

控制模式详解
ACT模式  
需要预训练模型：src/policy/train/catch_ball_test/checkpoints/last/pretrained_model  
使用LeRobot数据集统计信息进行预处理  
端到端 visuomotor 控制  
逆运动学模式  
预定义8步抓取序列  
P控制反馈回路  
2连杆机械臂逆运动学求解  
## 核心组件

状态机
```
class RobotStatus(Enum):  
    SEARCH = "search"  # 搜索目标  
    CATCH = "catch"    # 抓取操作  
    FIND = "find"      # 发现目标
```
方向控制
支持多档速度控制：

慢速：0.1 m/s, 30°/s  
中速：0.25 m/s, 60°/s  
快速：0.4 m/s, 90°/s 

## 注意事项  
确保串口连接正确  
ACT模式需要预训练模型文件  
首次运行会进行关节位置校准  
建议在开阔空间测试导航功能  

## 开发说明
添加新功能
在相应控制器模块中添加逻辑  
更新状态机（如需要）  
修改配置文件支持新参数  
调试模式  
设置 hardware_mode: 'normal' 可启用可视化界面，显示检测结果和目标区域 。

## Notes  
本项目基于LeKiwi机器人平台开发  
支持20 FPS实时控制，确保系统响应性  
模块化设计便于功能扩展和维护  
详细架构信息请参考项目Wiki文档
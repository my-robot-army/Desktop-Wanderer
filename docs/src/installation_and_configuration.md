# 安装与配置 (Installation & Configuration)

## 环境要求和依赖

在PC上进行调试需要安装lerobot平台，具体安装方法可以参考 [lerobot_Installation](https://huggingface.co/docs/lerobot/installation),下文也会给出。

### 安装miniforge

```commandline
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

### 创建python3.10环境

```commandline
conda create -y -n lerobot python=3.10
```

激活环境
```commandline
conda activate lerobot
```

conda安装ffmpeg

```commandline
conda install ffmpeg -c conda-forge
```
### 从源码下载安装lerobot
克隆仓库
```commandline
git clone https://github.com/huggingface/lerobot.git
cd lerobot
```

安装
```commandline
pip install -e .
```

安装舵机控制SDK

```commandline
pip install -e ".[feetech]"
```
基础环境准备完毕，在代码根目录运行

```commandline
python -m src.main
```

## 配置文件说明

配置文件内容
```commandline
port: /dev/ttyACM0 # 在控制板上的默认端口号
fps: 20 # 每秒识别20帧
log_level: INFO # 日志级别
hardware_mode: normal # normal,310b,rk3588 支持的硬件
control_mode: inverse # inverse, act 行动模式
```

其中
- port：在安装lerobot后，处于lerobot环境下，将设备连接到电脑运行`lerobot-find-port`,之后会出现一堆设备号，根据指示，拔掉连接线后按回车，即可获得串口号，控制板上的环境已经安装完毕，端口号为固定的 '/dev/ttyACM0'
- hardware_mode: 在PC上调试的时候选择normal模式，在控制板上运行的时候，为rk3588

## 首次运行

#### 机械臂初始设置

连接机械臂后首次运行代码，由于没有硬件配置文件，需要初始化机械臂

正常会看见
```
"Move robot to the middle of its range of motion and press ENTER...."
```
之后将所有电机置于中点位置，按回车，之后缓慢的转动所有电机，到每个电机的上下限位，之后按回车，即可完成配置文件的录入。

#### 项目再次启动

如果已经生成配置文件，打开项目能看到

```
"Press ENTER to use provided calibration file associated with the id {self.id}, or type 'c' and press ENTER to run calibration: "
```

之后可以按ENTER进入项目，或者等待3秒进入项目，或者输入c + ENTER重新初始化。

配置文件路径为

```
~/.cache/huggingface/lerobot/calibration/robots/lekiwi/None.json
```

删除它后进入项目自动进入初始化模式

## 硬件连接设置
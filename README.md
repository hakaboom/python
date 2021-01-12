https://www.zybuluo.com/hakaboom/note/1417109

## **CMD**

### 查询端口占用
```PowerShell
netstat -ano|findstr <端口号>
```
###终止端口
```PowerShell
 taskkill /pid <进程号> /F
```

---------------------------------------------------------
## **FastAPI**
---------------------------------------------------------
### 启动服务
```PowerShell
uvicorn main：app --reload
```
 - [x]  用fastApi搭建darknet识别服务端

 - **main**: 文件main.py
 - **app**: main.py内的app = FastAPI()
 - **--reload**: 更改代码后使服务器重新启动(仅用于开发)
 

---------------------------------------------------------
## **Opencv**
---------------------------------------------------------
 - [ ]  源代码编译opencv-cpu
 - [ ]  源代码编译opencv-cudn
 - [ ]  opencv使用yolov4识别
 - [ ]  opencv进行图像识别

---------------------------------------------------------
###下载源代码(记得要对应版本的)
https://github.com/opencv/opencv_contrib
https://github.com/opencv/opencv


 
---------------------------------------------------------
## **Android**
---------------------------------------------------------
 - [ ]  解决截图速度

### adb

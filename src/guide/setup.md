# Setting Up Go Environment
1. 安装Go：
   - 前往官方网站（https://golang.org/dl/）下载适用于你的操作系统的Go安装包。
   - 打开安装包并按照安装向导的指示完成安装过程。选择默认的安装选项即可。

2. 配置环境变量：
   - 在Windows上：
     - 右键点击“计算机”（或“此电脑”），选择“属性”。
     - 点击“高级系统设置”。
     - 在系统属性对话框中，点击“环境变量”按钮。
     - 在“系统变量”部分，找到名为“Path”的变量，双击打开它。
     - 在变量值的末尾添加Go的安装路径（例如：C:\Go\bin）。
     - 点击“确定”保存更改。
   - 在macOS上：
     - 打开终端。
     - 运行以下命令来编辑bash配置文件：
       ```
       nano ~/.bash_profile
       ```
     - 在文件末尾添加以下内容：
       ```
       export PATH=$PATH:/usr/local/go/bin
       ```
     - 按下Ctrl+X，然后按Y保存更改。
     - 运行以下命令以使更改生效：
       ```
       source ~/.bash_profile
       ```
   - 在Linux上：
     - 打开终端。
     - 运行以下命令来编辑bash配置文件（根据你使用的shell可能会有所不同）：
       ```
       nano ~/.bashrc
       ```
     - 在文件末尾添加以下内容：
       ```
       export PATH=$PATH:/usr/local/go/bin
       ```
     - 按下Ctrl+X，然后按Y保存更改。
     - 运行以下命令以使更改生效：
       ```
       source ~/.bashrc
       ```

3. 验证安装：
   - 打开终端或命令提示符。
   - 运行以下命令来验证Go是否正确安装并配置：
     ```
     go version
     ```
   - 如果安装成功，你将看到类似于以下内容的输出：
     ```
     go version go1.x.x windows/amd64
     ```

4. 设置工作目录：
   - 创建一个文件夹用于存储你的Go项目。
   - 打开终端或命令提示符，并导航到该文件夹：
     ```
     cd /path/to/your/folder
     ```
   - 从现在开始，你将在该文件夹中进行Go编程。

现在，你已经成功设置了Go编程环境。你可以开始编写和运行Go程序了。

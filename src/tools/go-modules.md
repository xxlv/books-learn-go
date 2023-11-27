# Go Modules

```go
要使用 Go 模块，首先需要在项目中初始化一个模块。使用以下命令：
```

``` bash
go mod init <module_name>
```

这将创建一个 go.mod 文件，其中包含项目的基本信息以及依赖的初始版本。

```go
import (
    "fmt"
    "github.com/example/package1"
)

func main() {
    fmt.Println(package1.SomeFunction())
}
```

在这个例子中，`github.com/example/package1` 是一个外部包，通过导入并使用，Go 模块系统会自动处理依赖的下载和版本管理。

```go
module myproject

go 1.17

require (
    github.com/example/package1 v1.2.0
    github.com/example/package2 v0.3.1
)
```

这里，`v1.2.0` 和 `v0.3.1` 是具体的版本号，Go 模块系统会根据这些信息下载适当版本的依赖。

### 与 GOPATH 对比
Go 模块与传统的 GOPATH 目录方式相比，提供了更好的版本管理和依赖隔离。模块可以在项目级别定义依赖，而不会影响全局的 GOPATH。

总体而言，Go 模块是 Go 语言社区在管理依赖方面的一大进步，使得项目更易维护和分享。

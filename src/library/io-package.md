# io Package

`io` 包提供了一组通用的接口和函数，用于进行输入和输出操作。它定义了 `Reader` 和 `Writer` 接口，以及许多实现这些接口的具体类型。

## `io` 包概述

`io` 包提供了一组通用的接口和函数，用于进行输入和输出操作。它定义了 `Reader` 和 `Writer` 接口，以及许多实现这些接口的具体类型。

## 读取操作

### 使用 `Reader` 接口

`Reader` 接口定义了读取操作的通用方法。通过使用 `Read` 方法，可以从实现了 `Reader` 接口的类型读取数据。

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    data := "Hello, World!"
    reader := strings.NewReader(data)

    buffer := make([]byte, 5)
    n, err := reader.Read(buffer)

    if err == nil || err == io.EOF {
        fmt.Printf("Read %d bytes: %s\n", n, buffer[:n])
    } else {
        fmt.Println("Error:", err)
    }
}
```

这里，我们使用 `strings.NewReader` 创建一个实现了 `Reader` 接口的类型，然后使用 `Read` 方法读取数据到缓冲区。

## 写入操作

### 使用 `Writer` 接口

`Writer` 接口定义了写入操作的通用方法。通过使用 `Write` 方法，可以向实现了 `Writer` 接口的类型写入数据。

```go
package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    file, err := os.Create("output.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer file.Close()

    data := "Hello, Go!"
    n, err := file.Write([]byte(data))

    if err == nil {
        fmt.Printf("Wrote %d bytes\n", n)
    } else {
        fmt.Println("Error:", err)
    }
}
```

这里，我们使用 `os.Create` 创建一个文件，并通过 `Write` 方法向文件写入数据。

## 复制操作

### 使用 `Copy` 函数

`io` 包提供了 `Copy` 函数，用于将数据从一个 `Reader` 复制到一个 `Writer`。

```go
package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    sourceFile, err := os.Open("source.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer sourceFile.Close()

    destinationFile, err := os.Create("destination.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer destinationFile.Close()

    n, err := io.Copy(destinationFile, sourceFile)

    if err == nil {
        fmt.Printf("Copied %d bytes\n", n)
    } else {
        fmt.Println("Error:", err)
    }
}
```

这里，我们使用 `os.Open` 打开一个源文件和 `os.Create` 创建一个目标文件，然后使用 `Copy` 函数将数据从源文件复制到目标文件。

总的来说，`io` 包提供了通用的输入和输出操作接口，使得在处理不同类型的输入和输出时更加灵活和统一。

# fmt Package

`fmt` 包是 Go 语言中用于格式化输入和输出的标准包。本章将概述 `fmt` 包的功能以及在格式化 I/O 中的使用示例。

## fmt 包概述

`fmt` 包提供了一系列函数，用于格式化输出到控制台或其他输出流，以及从输入流读取和解析格式化数据。

## 格式化输出

使用 `Printf` 函数可以将格式化的字符串输出到标准输出：

```go
package main

import "fmt"

func main() {
    name := "John"
    age := 30

    fmt.Printf("Name: %s, Age: %d\n", name, age)
}
```

这里，`Printf` 函数使用占位符 `%s` 和 `%d` 将变量 `name` 和 `age` 格式化输出到控制台。

## 格式化输入

使用 `Scanf` 函数可以从标准输入读取格式化的数据：

```go
package main

import "fmt"

func main() {
    var name string
    var age int

    fmt.Print("Enter your name: ")
    fmt.Scanf("%s", &name)

    fmt.Print("Enter your age: ")
    fmt.Scanf("%d", &age)

    fmt.Printf("Name: %s, Age: %d\n", name, age)
}
```

这里，`Scanf` 函数使用格式化字符串 `%s` 和 `%d` 从标准输入读取姓名和年龄。

## 字符串拼接

`Sprintf` 函数用于格式化字符串并返回结果字符串：

```go
package main

import "fmt"

func main() {
    name := "Jane"
    age := 25

    result := fmt.Sprintf("Name: %s, Age: %d", name, age)
    fmt.Println(result)
}
```

这里，`Sprintf` 函数将格式化后的字符串赋值给变量 `result`，然后输出到控制台。

## 与其他语言对比

`fmt` 包的格式化功能与其他语言中的格式化输出函数相似，但 Go 中通过占位符的使用更加简洁和灵活。

## 例子：格式化输出表格

```go
package main

import "fmt"

func main() {
    header := "Name\tAge\tCity"
    row1 := "John\t30\tNew York"
    row2 := "Jane\t25\tSan Francisco"

    fmt.Println(header)
    fmt.Println(row1)
    fmt.Println(row2)
}
```

这里，我们使用制表符 `\t` 创建一个简单的表格并输出到控制台。

总的来说，`fmt` 包提供了丰富的功能，可用于格式化输入和输出，使得 Go 语言在处理 I/O 时更加方便和灵活。

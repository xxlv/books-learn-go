# Control Flow

在Go语言中，控制流结构允许我们根据不同的条件执行不同的代码块，同时也提供了多种循环方式。本章将深入探讨这些概念，帮助读者更好地理解如何掌握Go语言的控制流。

## 条件语句

条件语句允许我们根据不同的条件执行不同的代码。Go语言提供了if、else if和else语句，用于实现条件控制。

```go
// 示例：根据年龄输出不同的信息
age := 25

if age < 18 {
    fmt.Println("未成年人")
} else if age >= 18 && age < 60 {
    fmt.Println("成年人")
} else {
    fmt.Println("老年人")
}

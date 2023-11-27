# Data Types


Go是一种静态类型的编程语言，提供了丰富的数据类型用于存储和操作数据。本章将介绍Go语言中各种可用的数据类型，包括基本数据类型和复合数据类型。

## 基本数据类型

Go语言提供了以下基本数据类型：

- **布尔型（bool）**：表示真假值的类型，只有两个取值：`true`和`false`。
- **整型（int）**：表示整数值的类型，根据位数可以分为不同精度的整型，例如`int8`、`int16`、`int32`和`int64`。
- **浮点型（float）**：表示小数值的类型，可以分为单精度浮点型（`float32`）和双精度浮点型（`float64`）。
- **复数型（complex）**：表示复数值的类型，由实部和虚部组成，可以分为单精度复数型（`complex64`）和双精度复数型（`complex128`）。
- **字符串型（string）**：表示文本字符串的类型，由一系列的字符组成。

以下是一个示例，展示了如何声明和使用不同的基本数据类型：

```go
package main

import "fmt"

func main() {
    var flag bool = true
    var num int = 10
    var pi float64 = 3.14
    var c complex128 = 1 + 2i
    var name string = "Go语言"

    fmt.Println(flag)
    fmt.Println(num)
    fmt.Println(pi)
    fmt.Println(c)
    fmt.Println(name)
}
```

除了基本数据类型，Go语言还提供了以下复合数据类型：

- **数组（array）**：表示相同类型的固定长度序列的数据结构。
- **切片（slice）**：表示可变长度的序列，是对数组的封装。
- **字典（map）**：表示键值对的集合。
- **结构体（struct）**：表示自定义的复合类型，可以包含多个字段。
- **接口（interface）**：表示一组方法的集合，用于实现多态。

以下是一个示例，展示了如何声明和使用不同的复合数据类型：

```go
package main

import "fmt"

func main() {
    // 数组
    var numbers [5]int = [5]int{1, 2, 3, 4, 5}

    // 切片
    var fruits []string = []string{"apple", "banana", "orange"}

    // 字典
    var ages map[string]int = map[string]int{
        "Alice": 25,
        "Bob":   30,
        "Carol": 35,
    }

    // 结构体
    type Person struct {
        Name string
        Age  int
    }
    var person Person = Person{Name: "Alice", Age: 25}

    // 接口
    type Shape interface {
        Area() float64
    }
    type Circle struct {
        Radius float64
    }
    func (c Circle) Area() float64 {
        return 3.14 * c.Radius * c.Radius
    }
    var shape Shape = Circle{Radius: 5.0}

    fmt.Println(numbers)
    fmt.Println(fruits)
    fmt.Println(ages)
    fmt.Println(person)
    fmt.Println(shape.Area())
}
```

## 类型对比

与其他编程语言相比，Go语言的数据类型有以下特点：

- **静态类型**：Go是一种静态类型语言，变量的类型在编译时就确定了，可以提前检测类型错误。
- **内置类型丰富**：Go语言提供了丰富的内置类型，包括整型、浮点型、字符串等，以及复合类型如数组、切片、字典等。
- **类型推断**：在变量声明时，可以使用`:=`操作符进行类型推断，无需显式指定类型。
- **值传递**：Go语言中的基本类型在函数调用时是按值传递的，而非引用传递。

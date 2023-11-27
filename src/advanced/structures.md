# Structures


Go 语言的结构体是一种复合数据类型，它将不同类型的变量组合在一个名称下。本章将帮助你深入理解结构体的概念和在 Go 中的实现方式。

## 声明结构体

在 Go 中，使用 `struct` 关键字后跟结构体的名称来声明结构体。在花括号内定义字段及其对应的数据类型。

```go
type Person struct {
    FirstName string
    LastName  string
    Age       int
}
```
在这里，我们声明了一个名为 Person 的结构体，包含三个字段：FirstName、LastName 和 Age。

创建结构体实例
要创建结构体的实例，可以使用以下语法：

``` go
p := Person{
    FirstName: "John",
    LastName:  "Doe",
    Age:       30,
}
```
这样就初始化了一个名为 p 的 Person 实例，并设置了相应的值。

访问结构体字段
可以使用点 (.) 运算符来访问结构体的字段：

``` go
fmt.Println("First Name:", p.FirstName)
fmt.Println("Last Name:", p.LastName)
fmt.Println("Age:", p.Age)
```

与其他语言对比
不同于一些语言，Go 中没有类的概念。Go 的结构体更简单，不支持像面向对象语言中类那样的方法。不过，在 Go 中你可以在类型上定义方法，包括结构体类型。

使用方法的例子

``` go
func (p Person) FullName() string {
    return p.FirstName + " " + p.LastName
}

fullName := p.FullName()
fmt.Println("Full Name:", fullName)
```

这里我们定义了一个 FullName 方法，通过这个方法获取完整的姓名。

总的来说，Go 的结构体提供了一种清晰高效的方式来组织和管理数据，而不会引入一些其他语言中类的复杂性。





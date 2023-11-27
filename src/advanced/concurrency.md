# Concurrency

Go 语言以其强大的并发支持而闻名，本章将深入探讨 Go 中的并发特性及其使用。

## 什么是并发

并发是指多个独立的执行过程同时运行的能力。Go 通过 goroutine 和 channel 提供了优雅而高效的并发模型。

## Goroutine

Goroutine 是轻量级线程，由 Go 运行时管理。它允许在程序中并发执行函数或方法。

### 创建 Goroutine

使用关键字 `go` 可以创建一个新的 Goroutine，例如：

```go
func printNumbers() {
    for i := 1; i <= 5; i++ {
        fmt.Println(i)
    }
}

go printNumbers()
```

这里，`printNumbers` 函数会在新的 Goroutine 中运行。

## Channel

Channel 是用于在 Goroutines 之间传递数据的管道。它提供了同步的方式，确保数据安全传递。

### 创建 Channel

使用 `make` 函数创建一个新的 Channel，例如：

```go
ch := make(chan int)
```

这里，创建了一个传递整数的 Channel。

### 使用 Channel

通过 `<-` 运算符发送和接收数据，示例：

```go
ch <- 42  // 发送数据
value := <-ch  // 接收数据
```

这里，通过 Channel 将整数 42 发送到 Goroutine 中，然后从中接收结果。

## 并发控制

通过使用 `sync` 包中的 `WaitGroup` 可以有效控制并发程序的执行。

### 使用 WaitGroup

```go
var wg sync.WaitGroup

func main() {
    wg.Add(1)
    go printNumbers()
    wg.Wait()
}

func printNumbers() {
    defer wg.Done()
    // 业务逻辑
}
```

这里，使用 `WaitGroup` 确保在所有 Goroutines 执行完毕之前等待主程序结束。

## 与其他语言对比

相较于一些传统的并发模型，Go 的 goroutine 和 channel 提供了更为简单和高效的方式来处理并发。

## 例子：并发的计算

```go
func calculateSum(numbers []int, result chan int) {
    sum := 0
    for _, num := range numbers {
        sum += num
    }
    result <- sum
}

func main() {
    numbers := []int{1, 2, 3, 4, 5}
    resultChan := make(chan int)

    go calculateSum(numbers[:len(numbers)/2], resultChan)
    go calculateSum(numbers[len(numbers)/2:], resultChan)

    partialSum1, partialSum2 := <-resultChan, <-resultChan
    totalSum := partialSum1 + partialSum2

    fmt.Println("Total Sum:", totalSum)
}
```

这里，我们使用两个 Goroutines 并发地计算切片的两个部分的和，然后通过 Channel 将结果传递回主程序。

总的来说，Go 中的并发特性为编写高效、简洁的并发程序提供了强大的工具。

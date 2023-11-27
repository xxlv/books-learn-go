# Writing Tests


在Go语言中，编写有效的测试对于确保代码的可靠性和可维护性至关重要。本章将提供一些建议，帮助你编写有效的Go代码测试。

## 单元测试

### 使用标准测试框架

Go语言内置了一个强大的测试框架，使用 `testing` 包。确保你的测试文件以 `_test.go` 结尾，并使用 `go test` 命令运行测试。

```go
package main

import "testing"

func TestAdd(t *testing.T) {
    tests := []struct {
        a, b, expected int
    }{
        {1, 2, 3},
        {0, 0, 0},
        {-1, 1, 0},
    }

    for _, test := range tests {
        result := Add(test.a, test.b)
        if result != test.expected {
            t.Errorf("Add(%d, %d) = %d; expected %d", test.a, test.b, result, test.expected)
        }
    }
}
```

这里，我们使用表格驱动测试来测试 `Add` 函数的不同输入情况。

## 示例测试

Go支持示例测试，这是一种将示例代码嵌入到文档中并确保其正确性的方式。

```go
package main

import "fmt"

func ExampleHello() {
    fmt.Println(Hello())
    // Output: Hello, World!
}
```

在示例测试中，你可以展示如何使用你的代码，并验证输出是否符合预期。

## Mocking

使用Mocking技术模拟依赖项，确保你的测试关注于被测试的代码而不是外部依赖。

```go
// UserService.go
package main

type UserService interface {
    GetUserByID(id int) string
}

// UserHandler.go
package main

type UserHandler struct {
    UserService UserService
}

func (h *UserHandler) GetUserByIDHandler(id int) string {
    return h.UserService.GetUserByID(id)
}

// UserHandler_test.go
package main

import (
    "testing"
    "github.com/stretchr/testify/mock"
)

type MockUserService struct {
    mock.Mock
}

func (m *MockUserService) GetUserByID(id int) string {
    args := m.Called(id)
    return args.String(0)
}

func TestGetUserByIDHandler(t *testing.T) {
    mockUserService
```

这里，我们使用Mocking技术创建了一个`MockUserService`来模拟`UserService`接口的实现。

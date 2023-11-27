# Pprof

```go
// Go语言中的pprof（性能剖析）

// pprof是Go语言内置的性能剖析工具，用于分析程序的性能瓶颈
// 主要通过采样和追踪两种方式进行性能分析

// 采样分析

// 导入pprof包
import _ "net/http/pprof"
import "net/http"

// 在程序中开启HTTP服务，以便pprof工具连接
func startPProf() {
	go func() {
		http.ListenAndServe(":6060", nil)
	}()
}

// 在main函数中调用startPProf函数，使pprof可用
func main() {
	startPProf()
	// 你的程序逻辑...
}

// 在浏览器中访问http://localhost:6060/debug/pprof/，可以看到各种性能分析的选项
// 例如，访问http://localhost:6060/debug/pprof/profile 可以生成CPU剖析图

// 追踪分析

// 导入pprof包
import "runtime/pprof"
import "os"

// 在程序中创建一个文件用于保存追踪数据
func startTrace() *os.File {
	f, _ := os.Create("trace.out")
	pprof.StartCPUProfile(f)
	return f
}

// 在main函数中调用startTrace函数开始CPU追踪
func main() {
	traceFile := startTrace()
	defer func() {
		pprof.StopCPUProfile()
		traceFile.Close()
	}()
	// 你的程序逻辑...
}

// 使用go tool pprof命令分析生成的trace数据
// 例如，go tool pprof trace.out
```
---
sidebar_position: 2
---

# Module
quick start and example see: https://github.com/NubeIO/module-contrib-demo


# Modules Naming
```
module-core-lora
module-oem-cps
module-contrib-xxx (for open module developed by the third party)
module-contrib-oem-xxx (for private module developed by the third party)
```
`module-<TYPE>-<SPECIFICS>`

# Prerequisites
- Go 1.18
- [GoLand by JetBrains](https://www.jetbrains.com/go/)

# Creating a Plugin
To create a new rubix-os module (plugin), start by running the following command,

```zsh
go mod init github.com/NubeIO/<module-name>
```

This command initializes a new Go module with the specified module path. The module path follows the URL-like syntax and should be unique.
Once executed, a `go.mod` file will be created, and you can add necessary dependencies.

# Managing Dependencies
Adding a dependency to your Go module is as simple as importing the desired package in your code. Go modules will automatically detect and manage the dependency.

To add a new dependency, run the following command in your project's directory:

```zsh
go get <package-name>
```

This command downloads the specified package and adds it to your `go.mod` file, along with its version. If you want to use a specific version of the package, you can append `@<version>` to the package name.

# rubix-os as Dependency
`rubix-os` is one of the major dependencies that need to be added to all modules. Follow the following command to add `rubix-os`:

```zsh
go get github.com/NubeIO/rubix-os
```

Additionally, if you want to use a local version of `rubix-os`, use the following command to point to the local `rubix-os`:

```zsh
go mod edit -replace github.com/NubeIO/rubix-os=/<path-to>/rubix-os
```

# Plugin System Over RPC
A plugin system over RPC allows us to separate or extend the core functionality of rubix-os. With this system, a plugin must adhere to the pre-defined interface, and the main application can communicate with plugins using RPC.

## Installation
`go-plugin` by `HashiCorp` is used to build a plugin system over RPC. To add this package follow the following command:

```zsh
go get github.com/hashicorp/go-plugin
```

## Implement the Interface
Create plugin implementations that satisfy the interface requirements by going through the following steps,

### 1. Define a `struct`
Each plugin will need to define a `struct` that implements the interface methods. For example, in above mentioned module [Example](#Example), we've defined `struct` **Module** as follows:

```go
// ./pkg/module.go

type Module struct {
    dbHelper       shared.DBHelper
    moduleName     string
    grpcMarshaller shared.Marshaller
    config         *Config
    store          *cache.Cache
}
```

### 2. Add Necessary Implementation
Following pre-defined methods needs to be implemented by previously defined `struct`,
- ValidateAndSetConfig
- Init
- Enable
- Disable
- GetInfo
- Get
- Post
- Put
- Patch
- Delete

> NOTE: Refer to [Example](#Example) for a reference.

## Serve the Plugin
Finally, call `plugin.Serve` to serve a plugin from the main function.


## API

`http://0.0.0.0:1660/api/modules/MODULE NAME/END POINT`

example
```
http://0.0.0.0:1660/api/modules/module-core-modbus/schema/json/network
```

```go
// main.go

func ServePlugin() {
    plugin.Serve(&plugin.ServeConfig{
	HandshakeConfig: shared.HandshakeConfig,
	Plugins:         plugin.PluginSet{"module-core-system": &shared.NubeModule{Impl: &pkg.Module{}}},
	GRPCServer:      plugin.DefaultGRPCServer,
    })
}

func main() {
    ServePlugin()
}
```
> NOTE: Here `shared.NubeModule` is the interface provided by `rubix-os` that an author's `struct` **Module** needs to implement.

# Logging with Logrus
Logrus is used to log necessary information which is crucial for tackling any issues.

## Installation
To get started with Logrus, use the following command to install the package:

```zsh
go get github.com/sirupsen/logrus
```

## Configuration
Logrus can be configured by passing needed arguments to their pre-defined methods. `rubix-os` requires only two configurations which are as follows,

```go
log.SetFormatter(&log.TextFormatter{
    DisableTimestamp: true,
})
```
```go
log.SetLevel(<log-level>)
```

Here, the `<log-level>` is extracted from an argument passed to the `ValidateAndSetConfig` method of the plugin interface. As logrus's `SetLevel` method takes pre-defined logrus log level constant, you may need to parse the extracted log level value coming in an argument.

```go
func (m *Module) ValidateAndSetConfig(config []byte) ([]byte, error) {
    newConfig := DefaultConfig()
    _ = yaml.Unmarshal(config, newConfig)

    logLevel, err := log.ParseLevel(newConfig.LogLevel)
    if err != nil {
	logLevel = log.ErrorLevel
    }
    logger.SetLevel(logLevel)
}
```

# Build the Plugin
Finally, use the following command to build the module,

```zsh
go build -o <module-name>
```
add in the build in the modules dir and restart `rubix-os`
```
/home/user/rubix-os/data/modules
```

# Proto
https://github.com/NubeIO/rubix-os#update-proto
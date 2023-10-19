---
sidebar_position: 3
---

# Secret

Secret's are a way of saving a password as an example in a module config


```go
type User struct {
	User     string `yaml:"user"`
	Password string `yaml:"password" type:"secret"`
}
```
passwords with the type:`secret`

![password-body.png](..%2Fimg%2Fpassword-body.png)
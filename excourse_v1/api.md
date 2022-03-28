---
title: excourse_v1 v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.5"

---

# excourse_v1

> v1.0.0

# users

## POST 获取验证码

POST /vertifications/

> Body 请求参数

```json
{
  "username": "郝高阳",
  "phone": "13833916349"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 否 | 用户名|none|
|» phone|body|string| 否 | 手机号|none|

> 返回示例

> 成功

```json
{
  "message": "发送成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|» message|string|true|none|none|

## GET 获取某个教师的信息

GET /users/{pk}/

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "id": 4,
  "password": "pbkdf2_sha256$150000$zXX2nhRqHubB$ugUR2FKCiGtYYYOMZFetiEO7fbGrWDBTti9ArJ5t/8Y=",
  "last_login": null,
  "is_superuser": false,
  "username": "包冬璟",
  "work_id": null,
  "icon": null,
  "phone": "11111195337",
  "email": null,
  "is_grade": 0,
  "is_super": 0,
  "is_active": true,
  "wechat": null,
  "create_time": "2022-03-22T21:42:10.034544+08:00",
  "update_time": "2022-03-23T11:11:10.391765+08:00",
  "is_delete": false,
  "school_id": 1,
  "groups": [],
  "user_permissions": []
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|» id|integer|true|none|none|
|» password|string|true|none|none|
|» username|string|true|none|none|
|» work_id|string¦null|true|none|none|
|» icon|string¦null|true|none|none|
|» phone|string|true|none|none|
|» email|string¦null|true|none|none|
|» is_grade|integer|true|none|none|
|» is_super|integer|true|none|none|
|» is_active|boolean|true|none|none|
|» wechat|string¦null|true|none|none|
|» create_time|string|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» school_id|integer|true|none|none|

## PUT 修改教师信息

PUT /users/{pk}/

> Body 请求参数

```json
{
  "password": "yiner0326"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "id": 115,
  "password": "pbkdf2_sha256$150000$Nx0Pew3sqga0$p6H9JxNenGTWIpDlY6F2QV1jaHa9CBAzfzGKMpd9L1o=",
  "last_login": null,
  "is_superuser": false,
  "username": "郝高阳",
  "work_id": null,
  "icon": null,
  "phone": "13833916349",
  "email": null,
  "is_grade": 0,
  "is_super": 0,
  "is_active": true,
  "wechat": null,
  "create_time": "2022-03-25T14:49:35.847247+08:00",
  "update_time": "2022-03-25T15:02:36.206753+08:00",
  "is_delete": false,
  "school_id": 1,
  "groups": [],
  "user_permissions": []
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|» id|integer|true|none|none|
|» password|string|true|none|none|
|» username|string|true|none|none|
|» work_id|string¦null|true|none|none|
|» icon|string¦null|true|none|none|
|» phone|string|true|none|none|
|» email|string¦null|true|none|none|
|» is_grade|integer|true|none|none|
|» is_super|integer|true|none|none|
|» is_active|boolean|true|none|none|
|» wechat|string¦null|true|none|none|
|» create_time|string|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» school_id|integer|true|none|none|

## POST 注册

POST /users/register/

> Body 请求参数

```json
{
  "username": "郝高阳",
  "password": "123",
  "school_id": "1",
  "phone": "13833916349",
  "sms_code": "935688"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 是 | 用户名|none|
|» password|body|string| 是 | 密码|none|
|» school_id|body|integer| 是 | 学校id|none|
|» phone|body|string| 是 | 手机|none|
|» sms_code|body|string| 是 | 验证码|none|
|» work_id|body|string| 否 | 工号|none|
|» email|body|string| 否 | 邮箱|none|
|» wechat|body|string| 否 | 微信号|none|
|» is_grade|body|integer| 否 | 是否年纪管理员|none|
|» is_super|body|integer| 否 | 是否超级管理员|none|

> 返回示例

> 成功

```json
{
  "id": 115,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTUsInVzZXJuYW1lIjoiXHU5MGRkXHU5YWQ4XHU5NjMzIiwiZXhwIjoxNjQ4Mjc3Mzc2LCJlbWFpbCI6bnVsbH0.3B3YkZKnSoHC4kdigcArxh2w3L6NR9Z0omra3vj2-i0",
  "password": "pbkdf2_sha256$150000$rC5D4gNJBQaH$Ka1SN9Tyr7WBFSOgLJYOKdp0/sY49V+cnuo78qRAeVI=",
  "last_login": null,
  "is_superuser": false,
  "username": "郝高阳",
  "work_id": null,
  "icon": null,
  "phone": "13833916349",
  "email": null,
  "is_grade": 0,
  "is_super": 0,
  "is_active": true,
  "wechat": null,
  "create_time": "2022-03-25T14:49:35.847247+08:00",
  "update_time": "2022-03-25T14:49:35.967958+08:00",
  "is_delete": false,
  "school_id": 1,
  "groups": [],
  "user_permissions": []
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|成功|Inline|

### 返回数据结构

状态码 **201**

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|» id|integer|true|none|none|
|» password|string|true|none|none|
|» username|string|true|none|none|
|» work_id|string¦null|true|none|none|
|» icon|string¦null|true|none|none|
|» phone|string|true|none|none|
|» email|string¦null|true|none|none|
|» is_grade|integer|true|none|none|
|» is_super|integer|true|none|none|
|» is_active|boolean|true|none|none|
|» wechat|string¦null|true|none|none|
|» create_time|string|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» school_id|integer|true|none|none|

## POST 登录

POST /users/login/

> Body 请求参数

```json
{
  "username": "测试4",
  "password": "123"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 是 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "user_id": 112,
  "username": "测试4",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTIsInVzZXJuYW1lIjoiXHU2ZDRiXHU4YmQ1NCIsImV4cCI6MTY0ODA1MzQ2MCwiZW1haWwiOm51bGx9.Wq_NuaVa5oCX6fHaoXk2JZhquR9hJBPkbMzaSz1NWM4"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|» user_id|integer|true|none|none|
|» username|string|true|none|none|
|» token|string|true|none|none|

# 数据模型


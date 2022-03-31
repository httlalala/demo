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

# Default

## GET 周次to时间

GET /week2date/

> Body 请求参数

```json
{
  "week": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» week|body|integer| 是 | 周次|none|

> 返回示例

> 成功

```json
"2022-03-28"
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|undefined|

## GET 时间to周次

GET /date2week/

> Body 请求参数

```json
{
  "date": "2022-04-12"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» date|body|string| 是 | 周次|"2022-04-23"|

> 返回示例

> 成功

```json
3
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|number|

# 数据模型


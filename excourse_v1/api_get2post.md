---
title: excourse_v1_fix v1.0.0
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

# excourse_v1_fix

> v1.0.0

# Default

## POST 周次to时间

POST /week2date/

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

## POST 时间to周次

POST /date2week/

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
|» date|body|string| 是 | 日期|2022-04-23|

> 返回示例

> 成功

```json
3
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|number|

# users

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

## GET 根据条件获取教师数据

GET /users/

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|page|query|string| 否 ||none|
|per_page|query|string| 否 ||none|
|username|query|string| 否 ||用户名|
|phone|query|string| 否 ||电话|
|Authorization|header|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 106,
      "password": "pbkdf2_sha256$150000$FRjEMT37CcZL$XLSG6awJNEGf1CNU/5yu8lEvfQu1J5kunSzxGNI9b80=",
      "last_login": null,
      "is_superuser": false,
      "username": "郝高阳",
      "work_id": null,
      "icon": null,
      "phone": "13833916349",
      "email": null,
      "is_grade": 1,
      "is_super": 1,
      "is_active": true,
      "wechat": null,
      "create_time": "2022-03-28T16:26:51.432963+08:00",
      "update_time": "2022-03-28T16:26:51.578129+08:00",
      "is_delete": false,
      "school_id": 1,
      "groups": [],
      "user_permissions": []
    }
  ]
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
|» count|integer|true|none|none|
|» next|string¦null|true|none|none|
|» previous|string¦null|true|none|none|
|» results|[object]|true|none|none|
|»» id|integer|false|none|none|
|»» password|string|false|none|none|
|»» last_login|null|false|none|none|
|»» is_superuser|boolean|false|none|none|
|»» username|string|false|none|none|
|»» work_id|null|false|none|none|
|»» icon|null|false|none|none|
|»» phone|string|false|none|none|
|»» email|null|false|none|none|
|»» is_grade|integer|false|none|none|
|»» is_super|integer|false|none|none|
|»» is_active|boolean|false|none|none|
|»» wechat|null|false|none|none|
|»» create_time|string|false|none|none|
|»» update_time|string|false|none|none|
|»» is_delete|boolean|false|none|none|
|»» school_id|integer|false|none|none|
|»» groups|[string]|false|none|none|
|»» user_permissions|[string]|false|none|none|

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

## POST 检查用户名是否可用

POST /users/check/

> Body 请求参数

```json
{
  "username": "张三"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "msg": "用户名可用"
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
|» msg|string|true|none|none|

# applications/管理员

## PUT 修改申请信息

PUT /applications/manager/{pk}/

> Body 请求参数

```json
{
  "target_course_id": 751,
  "handler_id": 106,
  "handle_time": "2022-03-28 22:00"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» target_course_id|body|integer| 否 | 目标课程id|none|
|» handler_id|body|integer| 否 | 处理人id|none|
|» handle_time|body|string| 否 | 处理时间|none|
|» cancel_reason|body|string| 否 | 拒绝原因|none|

> 返回示例

> 成功

```json
{
  "id": 4,
  "applicant_info": {
    "name": "美术",
    "week": 1,
    "weekday": 1,
    "order": 3,
    "grade": 1,
    "class_number": 1,
    "teacher_name": "窦婧",
    "teacher_phone": "11111141333"
  },
  "target_info": {
    "name": "音乐",
    "week": 1,
    "weekday": 4,
    "order": 5,
    "grade": 1,
    "class_number": 6,
    "teacher_name": "胡德勤",
    "teacher_phone": "11111106686"
  },
  "reason": "难受需要代课",
  "type": 1,
  "create_time": "2022-03-28T21:59:40.433557+08:00",
  "handle_time": "2022-03-28T22:00:00+08:00",
  "fail_time": "2022-03-28T16:07:33.657991+08:00",
  "applicant_confirm": 0,
  "solver_confirm": 0,
  "overdue": false,
  "update_time": "2022-03-28T23:37:43.879287+08:00",
  "is_delete": false,
  "cancel_reason": null,
  "applicant_course_id": 11,
  "target_course_id": 751,
  "handler_id": 106
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
|» applicant_info|object¦null|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» teacher_phone|string|true|none|none|
|» target_info|object¦null|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» teacher_phone|string|true|none|none|
|» reason|string|true|none|none|
|» type|integer|true|none|none|
|» create_time|string|true|none|none|
|» handle_time|string|true|none|none|
|» fail_time|string|true|none|none|
|» applicant_confirm|integer|true|none|none|
|» solver_confirm|integer|true|none|none|
|» overdue|boolean|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» cancel_reason|string¦null|true|none|none|
|» applicant_course_id|integer|true|none|none|
|» target_course_id|integer¦null|true|none|none|
|» handler_id|integer|true|none|none|

## GET 获取申请和历史

GET /applications/manager/

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|type|query|string| 是 ||substitution或history|
|page|query|string| 否 ||none|
|per_page|query|string| 否 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "applicant_info": {
        "name": "数学",
        "week": 1,
        "weekday": 1,
        "order": 1,
        "grade": 1,
        "class_number": 1,
        "teacher_name": "解金霞",
        "teacher_phone": "11111123485"
      },
      "target_info": null,
      "reason": "难受",
      "type": 1,
      "create_time": "2022-03-28T20:32:51.095695+08:00",
      "handle_time": null,
      "fail_time": "2022-03-28T16:07:32.443234+08:00",
      "applicant_confirm": 1,
      "solver_confirm": 1,
      "overdue": false,
      "update_time": "2022-03-28T23:18:15.517708+08:00",
      "is_delete": false,
      "cancel_reason": null,
      "applicant_course_id": 1,
      "target_course_id": null,
      "handler_id": null
    },
    {
      "id": 4,
      "applicant_info": {
        "name": "美术",
        "week": 1,
        "weekday": 1,
        "order": 3,
        "grade": 1,
        "class_number": 1,
        "teacher_name": "窦婧",
        "teacher_phone": "11111141333"
      },
      "target_info": null,
      "reason": "难受需要代课",
      "type": 1,
      "create_time": "2022-03-28T21:59:40.433557+08:00",
      "handle_time": null,
      "fail_time": "2022-03-28T16:07:33.657991+08:00",
      "applicant_confirm": 0,
      "solver_confirm": 0,
      "overdue": false,
      "update_time": "2022-03-28T21:59:40.433557+08:00",
      "is_delete": false,
      "cancel_reason": null,
      "applicant_course_id": 11,
      "target_course_id": null,
      "handler_id": null
    }
  ]
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
|» count|integer|true|none|none|
|» next|string¦null|true|none|none|
|» previous|string¦null|true|none|none|
|» results|[object]|true|none|none|

## POST 提交申请

POST /applications/manager/

> Body 请求参数

```json
{
  "applicant_course_id": 8,
  "reason": "看病",
  "type": 1,
  "target_course_id": 463
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» applicant_course_id|body|integer| 是 | 申请课程id|none|
|» reason|body|string| 是 | 申请原因|none|
|» type|body|integer| 是 | 申请类型|none|
|» target_course_id|body|integer| 是 | 目标课程id|none|

> 返回示例

> 成功

```json
{
  "id": 6,
  "applicant_info": {
    "name": "语文",
    "week": 3,
    "weekday": 1,
    "order": 2,
    "grade": 1,
    "class_number": 1,
    "teacher_name": "包冬璟",
    "teacher_phone": "11111136498"
  },
  "target_info": {
    "name": "英语阅读",
    "week": 3,
    "weekday": 3,
    "order": 4,
    "grade": 1,
    "class_number": 4,
    "teacher_name": "桑慧莲",
    "teacher_phone": "11111109888"
  },
  "reason": "看病",
  "type": 1,
  "create_time": "2022-03-28T23:48:53.759289+08:00",
  "handle_time": null,
  "fail_time": "2022-04-12T01:34:46.552201+08:00",
  "applicant_confirm": 0,
  "solver_confirm": 0,
  "overdue": false,
  "update_time": "2022-03-28T23:48:53.759289+08:00",
  "is_delete": false,
  "cancel_reason": null,
  "applicant_course_id": 8,
  "target_course_id": 463,
  "handler_id": null
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
|» applicant_info|object|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» teacher_phone|string|true|none|none|
|» target_info|object|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» teacher_phone|string|true|none|none|
|» reason|string|true|none|none|
|» type|integer|true|none|none|
|» create_time|string|true|none|none|
|» handle_time|string|true|none|none|
|» fail_time|string|true|none|none|
|» applicant_confirm|integer|true|none|none|
|» solver_confirm|integer|true|none|none|
|» overdue|boolean|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» cancel_reason|string¦null|true|none|none|
|» applicant_course_id|integer|true|none|none|
|» target_course_id|integer|true|none|none|
|» handler_id|integer|true|none|none|

# applications/教师

## GET 获取“我的”界面的申请数据

GET /applications/mine/

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|type|query|string| 是 ||target/applicant/history|
|page|query|string| 否 ||none|
|per_page|query|string| 否 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "applicant_info": {
        "name": "数学",
        "week": 5,
        "weekday": 1,
        "order": 1,
        "grade": 1,
        "class_number": 1,
        "teacher_name": "解金霞",
        "teacher_phone": "11111123485"
      },
      "target_info": null,
      "reason": "吃坏肚子了",
      "type": 0,
      "create_time": "2022-03-28T17:46:24.201752+08:00",
      "handle_time": null,
      "fail_time": "2022-03-28T16:07:32.757594+08:00",
      "applicant_confirm": 0,
      "solver_confirm": 0,
      "overdue": false,
      "update_time": "2022-03-28T17:46:24.201752+08:00",
      "is_delete": false,
      "cancel_reason": null,
      "applicant_course_id": 5,
      "target_course_id": null,
      "handler_id": null
    }
  ]
}
```

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "applicant_info": {
        "name": "数学",
        "week": 5,
        "weekday": 1,
        "order": 1,
        "grade": 1,
        "class_number": 1,
        "teacher_name": "解金霞",
        "teacher_phone": "11111123485"
      },
      "target_info": {
        "name": "语文",
        "week": 5,
        "weekday": 1,
        "order": 2,
        "grade": 1,
        "class_number": 1,
        "teacher_name": "包冬璟",
        "teacher_phone": "11111136498"
      },
      "reason": "吃坏肚子了",
      "type": 0,
      "create_time": "2022-03-28T17:46:24.201752+08:00",
      "handle_time": null,
      "fail_time": "2022-03-28T16:07:32.757594+08:00",
      "applicant_confirm": 0,
      "solver_confirm": 0,
      "overdue": false,
      "update_time": "2022-03-28T17:46:24.201752+08:00",
      "is_delete": false,
      "cancel_reason": null,
      "applicant_course_id": 5,
      "target_course_id": 10,
      "handler_id": null
    }
  ]
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
|» count|integer|true|none|数据总数|
|» next|string¦null|true|none|下一页|
|» previous|string¦null|true|none|上一页|
|» results|[object]|true|none|数据列表|
|»» id|integer|false|none|none|
|»» applicant_info|object|false|none|none|
|»»» name|string|true|none|none|
|»»» week|integer|true|none|none|
|»»» weekday|integer|true|none|none|
|»»» order|integer|true|none|none|
|»»» grade|integer|true|none|none|
|»»» class_number|integer|true|none|none|
|»»» teacher_name|string|true|none|none|
|»»» teacher_phone|string|true|none|none|
|»» target_info|null|false|none|none|
|»» reason|string|false|none|none|
|»» type|integer|false|none|none|
|»» create_time|string|false|none|none|
|»» handle_time|null|false|none|none|
|»» fail_time|string|false|none|none|
|»» applicant_confirm|integer|false|none|none|
|»» solver_confirm|integer|false|none|none|
|»» overdue|boolean|false|none|none|
|»» update_time|string|false|none|none|
|»» is_delete|boolean|false|none|none|
|»» cancel_reason|null|false|none|none|
|»» applicant_course_id|integer|false|none|none|
|»» target_course_id|null|false|none|none|
|»» handler_id|null|false|none|none|

## POST 提交申请

POST /applications/

> Body 请求参数

```json
{
  "type": 1,
  "reason": "吃坏肚子了",
  "applicant_course_id": 3
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» type|body|integer| 是 | 类型|none|
|» reason|body|string| 是 | 申请原因|none|
|» applicant_course_id|body|integer| 是 | 申请课程id|none|
|» target_course_id|body|string| 否 | 目标课程id|none|

> 返回示例

> 成功

```json
{
  "id": 5,
  "applicant_info": {
    "name": "美术",
    "week": 5,
    "weekday": 1,
    "order": 3,
    "grade": 1,
    "class_number": 1,
    "teacher_name": "窦婧",
    "teacher_phone": "11111141333"
  },
  "target_info": {
    "name": "语文",
    "week": 4,
    "weekday": 2,
    "order": 3,
    "grade": 1,
    "class_number": 1,
    "teacher_name": "包冬璟",
    "teacher_phone": "11111136498"
  },
  "reason": "吃坏肚子了",
  "type": 0,
  "create_time": "2022-03-28T23:21:52.359851+08:00",
  "handle_time": null,
  "fail_time": "2022-04-26T02:44:46.552201+08:00",
  "applicant_confirm": 0,
  "solver_confirm": 0,
  "overdue": false,
  "update_time": "2022-03-28T23:21:52.360849+08:00",
  "is_delete": false,
  "cancel_reason": null,
  "applicant_course_id": 15,
  "target_course_id": 44,
  "handler_id": null
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
|» applicant_info|object¦null|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» teacher_phone|string|true|none|none|
|» target_info|object¦null|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» teacher_phone|string|true|none|none|
|» reason|string|true|none|none|
|» type|integer|true|none|none|
|» create_time|string|true|none|none|
|» handle_time|string¦null|true|none|none|
|» fail_time|string|true|none|none|
|» applicant_confirm|integer|true|none|none|
|» solver_confirm|integer|true|none|none|
|» overdue|boolean|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» cancel_reason|string¦null|true|none|none|
|» applicant_course_id|integer|true|none|none|
|» target_course_id|integer¦null|true|none|none|
|» handler_id|integer¦null|true|none|none|

## PUT 修改申请信息

PUT /applications/{pk}/

> Body 请求参数

```json
{
  "solver_confirm": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» applicant_confirm|body|integer| 否 | 申请方是否确认|none|
|» solver_confirm|body|integer| 否 | 解决方是否确认|none|

> 返回示例

> 成功

```json
{
  "id": 2,
  "applicant_course_info": {
    "name": "数学",
    "week": 5,
    "weekday": 1,
    "order": 1,
    "grade": 6,
    "class_number": 7
  },
  "target_course_info": {
    "name": "班队活动",
    "week": 5,
    "weekday": 1,
    "order": 6,
    "grade": 6,
    "class_number": 7
  },
  "reason": "吃坏肚子了",
  "type": 0,
  "create_time": "2022-03-25T17:29:56.228443+08:00",
  "handle_time": null,
  "fail_time": "2022-04-21T16:40:00+08:00",
  "applicant_confirm": 1,
  "solver_confirm": 1,
  "overdue": false,
  "update_time": "2022-03-25T17:49:09.545261+08:00",
  "is_delete": false,
  "applicant_course_id": 5,
  "target_course_id": 30,
  "handler_id": null
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
|» applicant_course_info|object¦null|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|» target_course_info|object¦null|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|» reason|string|true|none|none|
|» type|integer|true|none|none|
|» create_time|string|true|none|none|
|» handle_time|string¦null|true|none|none|
|» fail_time|string|true|none|none|
|» applicant_confirm|integer|true|none|none|
|» solver_confirm|integer|true|none|none|
|» overdue|boolean|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|
|» applicant_course_id|integer|true|none|none|
|» target_course_id|integer¦null|true|none|none|
|» handler_id|integer¦null|true|none|none|

# schools

## PUT 修改某个学校的数据

PUT /schools/{pk}/

> Body 请求参数

```json
{
  "province": "河南省"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» province|body|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "id": 1,
  "province": "河南省",
  "city": "石家庄市",
  "region": "栾城区",
  "address": "人民大街111号",
  "name": "实验小学",
  "week_diff_first": 0,
  "week_diff_second": 0,
  "week_num": 20,
  "first_week_date": "2022-03-24T08:00:00+08:00",
  "create_time": "2022-03-22T20:40:05.995857+08:00",
  "update_time": "2022-03-25T15:16:52.535676+08:00",
  "is_delete": false
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
|» province|string|true|none|none|
|» city|string|true|none|none|
|» region|string|true|none|none|
|» address|string|true|none|none|
|» name|string|true|none|none|
|» week_diff_first|integer|true|none|none|
|» week_diff_second|integer|true|none|none|
|» week_num|integer|true|none|none|
|» first_week_date|string|true|none|none|
|» create_time|string|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|

## GET 获取某个学校的数据

GET /schools/{pk}/

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|

> 返回示例

> 成功

```json
{
  "id": 1,
  "province": "江苏省",
  "city": "无锡市",
  "region": "滨湖区",
  "address": "蠡湖大道1号",
  "name": "蒋王小学",
  "week_num": 5,
  "first_week_date": "2022-03-28T16:04:46.552201+08:00",
  "create_time": "2022-03-28T16:04:47.407663+08:00",
  "update_time": "2022-03-28T16:04:47.407663+08:00",
  "is_delete": false
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
|» province|string|true|none|none|
|» city|string|true|none|none|
|» region|string|true|none|none|
|» address|string|true|none|none|
|» name|string|true|none|none|
|» week_num|integer|true|none|none|
|» first_week_date|string|true|none|none|
|» create_time|string|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|

## PUT 修改某学校第一周时间

PUT /schools/firstweek/{pk}/

> Body 请求参数

```json
{
  "date": "2022-03-29"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|pk|path|string| 是 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» date|body|string| 是 | 日期|2022-02-02|

> 返回示例

> 成功

```json
{
  "id": 2,
  "province": "河北省",
  "city": "邢台市",
  "region": "桥东区",
  "address": "钢铁路1号",
  "name": "育才小学",
  "week_num": 20,
  "first_week_date": "2022-03-29T00:00:00+08:00",
  "create_time": "2022-03-29T00:09:47.291406+08:00",
  "update_time": "2022-03-29T00:19:42.470564+08:00",
  "is_delete": false
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
|» province|string|true|none|none|
|» city|string|true|none|none|
|» region|string|true|none|none|
|» address|string|true|none|none|
|» name|string|true|none|none|
|» week_num|integer|true|none|none|
|» first_week_date|string|true|none|none|
|» create_time|string|true|none|none|
|» update_time|string|true|none|none|
|» is_delete|boolean|true|none|none|

## GET 获取所有学校数据

GET /schools/

> 返回示例

> 成功

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "province": "河北省",
      "city": "石家庄市",
      "region": "栾城区",
      "address": "人民大街111号",
      "name": "实验小学",
      "week_diff_first": 0,
      "week_diff_second": 0,
      "week_num": 20,
      "first_week_date": "2022-03-24T08:00:00+08:00",
      "create_time": "2022-03-22T20:40:05.995857+08:00",
      "update_time": "2022-03-24T17:15:44.489662+08:00",
      "is_delete": false
    },
    {
      "id": 2,
      "province": "江苏省",
      "city": "无锡市",
      "region": "滨湖区",
      "address": "蠡湖大道1800号",
      "name": "江南大学",
      "week_diff_first": 0,
      "week_diff_second": 0,
      "week_num": 20,
      "first_week_date": null,
      "create_time": "2022-03-23T18:20:19.871977+08:00",
      "update_time": "2022-03-23T18:20:19.871977+08:00",
      "is_delete": false
    },
    {
      "id": 3,
      "province": "山西省",
      "city": "太原市",
      "region": "大同区",
      "address": "人民路100号",
      "name": "实验中学",
      "week_diff_first": 0,
      "week_diff_second": 0,
      "week_num": 20,
      "first_week_date": null,
      "create_time": "2022-03-23T21:11:25.997272+08:00",
      "update_time": "2022-03-23T21:11:25.997272+08:00",
      "is_delete": false
    }
  ]
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
|» count|integer|true|none|none|
|» next|string¦null|true|none|none|
|» previous|string¦null|true|none|none|
|» results|[object]|true|none|none|
|»» id|integer|true|none|none|
|»» province|string|true|none|none|
|»» city|string|true|none|none|
|»» region|string|true|none|none|
|»» address|string|true|none|none|
|»» name|string|true|none|none|
|»» week_diff_first|integer|true|none|none|
|»» week_diff_second|integer|true|none|none|
|»» week_num|integer|true|none|none|
|»» first_week_date|string¦null|true|none|none|
|»» create_time|string|true|none|none|
|»» update_time|string|true|none|none|
|»» is_delete|boolean|true|none|none|

# courses

## POST 获取可选课程数据

POST /courses/choices/{type}/

> Body 请求参数

```json
{
  "applicant_course_id": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|type|path|string| 是 ||0/1|
|page|query|string| 否 ||none|
|per_page|query|string| 否 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» applicant_course_id|body|integer| 是 | 申请课程id|none|
|» week|body|integer| 否 | 周次|不填代表当前日期对应的周次|

> 返回示例

> 成功

```json
{
  "count": 100,
  "next": "http://127.0.0.1:8000/courses/choices/0/?page=2&per_page=5",
  "previous": null,
  "results": [
    {
      "id": 116,
      "teacher_name": "包冬璟",
      "grade": 1,
      "class_number": 1,
      "name": "语文",
      "week": 1,
      "weekday": 5,
      "order": 3,
      "create_time": "2022-03-28T16:07:43.620724+08:00",
      "update_time": "2022-03-28T16:07:43.620724+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:43.620724+08:00",
      "end_time": "2022-03-28T16:07:43.620724+08:00",
      "teacher_id": 2,
      "class_id": 1
    },
    {
      "id": 41,
      "teacher_name": "包冬璟",
      "grade": 1,
      "class_number": 1,
      "name": "语文",
      "week": 1,
      "weekday": 2,
      "order": 3,
      "create_time": "2022-03-28T16:07:36.424113+08:00",
      "update_time": "2022-03-28T16:07:36.424113+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:36.424113+08:00",
      "end_time": "2022-03-28T16:07:36.424113+08:00",
      "teacher_id": 2,
      "class_id": 1
    },
    {
      "id": 96,
      "teacher_name": "张彬",
      "grade": 1,
      "class_number": 1,
      "name": "道德法治",
      "week": 1,
      "weekday": 4,
      "order": 4,
      "create_time": "2022-03-28T16:07:41.892001+08:00",
      "update_time": "2022-03-28T16:07:41.892001+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:41.892001+08:00",
      "end_time": "2022-03-28T16:07:41.892001+08:00",
      "teacher_id": 8,
      "class_id": 1
    },
    {
      "id": 101,
      "teacher_name": "王禹",
      "grade": 1,
      "class_number": 1,
      "name": "体育健康1",
      "week": 1,
      "weekday": 4,
      "order": 5,
      "create_time": "2022-03-28T16:07:42.325879+08:00",
      "update_time": "2022-03-28T16:07:42.325879+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:42.325879+08:00",
      "end_time": "2022-03-28T16:07:42.325879+08:00",
      "teacher_id": 4,
      "class_id": 1
    },
    {
      "id": 31,
      "teacher_name": "包冬璟",
      "grade": 1,
      "class_number": 1,
      "name": "语文",
      "week": 1,
      "weekday": 2,
      "order": 1,
      "create_time": "2022-03-28T16:07:35.561709+08:00",
      "update_time": "2022-03-28T16:07:35.561709+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:35.561709+08:00",
      "end_time": "2022-03-28T16:07:35.561709+08:00",
      "teacher_id": 2,
      "class_id": 1
    }
  ]
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
|» count|integer|true|none|none|
|» next|string¦null|true|none|none|
|» previous|string¦null|true|none|none|
|» results|[object]|true|none|none|
|»» id|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» create_time|string|true|none|none|
|»» update_time|string|true|none|none|
|»» is_delete|boolean|true|none|none|
|»» start_time|string|true|none|none|
|»» end_time|string|true|none|none|
|»» teacher_id|integer|true|none|none|
|»» class_id|integer|true|none|none|

## POST 获取课程数据

POST /courses/

> Body 请求参数

```json
{
  "school_id": 0,
  "grade": 0,
  "class_number": 0,
  "week": 0,
  "weekday": 0,
  "order": 0,
  "teacher_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|page|query|string| 否 ||none|
|per_page|query|string| 否 ||none|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» school_id|body|integer| 否 | 学校id|none|
|» grade|body|integer| 否 | 年级|none|
|» class_number|body|integer| 否 | 班级|none|
|» week|body|integer| 否 | 周次|none|
|» weekday|body|integer| 否 | 星期|none|
|» order|body|integer| 否 | 节次|none|
|» teacher_id|body|integer| 否 | 授课教师|none|

> 返回示例

> 成功

```json
{
  "count": 5565,
  "next": "http://127.0.0.1:8000/courses/?page=2&per_page=5",
  "previous": null,
  "results": [
    {
      "id": 1,
      "teacher_name": "解金霞",
      "grade": 1,
      "class_number": 1,
      "name": "数学",
      "week": 1,
      "weekday": 1,
      "order": 1,
      "create_time": "2022-03-28T16:07:32.443234+08:00",
      "update_time": "2022-03-28T16:07:32.443234+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:32.443234+08:00",
      "end_time": "2022-03-28T16:07:32.443234+08:00",
      "teacher_id": 1,
      "class_id": 1
    },
    {
      "id": 2,
      "teacher_name": "解金霞",
      "grade": 1,
      "class_number": 1,
      "name": "数学",
      "week": 2,
      "weekday": 1,
      "order": 1,
      "create_time": "2022-03-28T16:07:32.521519+08:00",
      "update_time": "2022-03-28T16:07:32.521519+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:32.521519+08:00",
      "end_time": "2022-03-28T16:07:32.521519+08:00",
      "teacher_id": 1,
      "class_id": 1
    },
    {
      "id": 3,
      "teacher_name": "解金霞",
      "grade": 1,
      "class_number": 1,
      "name": "数学",
      "week": 3,
      "weekday": 1,
      "order": 1,
      "create_time": "2022-03-28T16:07:32.599517+08:00",
      "update_time": "2022-03-28T16:07:32.599517+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:32.599517+08:00",
      "end_time": "2022-03-28T16:07:32.599517+08:00",
      "teacher_id": 1,
      "class_id": 1
    },
    {
      "id": 4,
      "teacher_name": "解金霞",
      "grade": 1,
      "class_number": 1,
      "name": "数学",
      "week": 4,
      "weekday": 1,
      "order": 1,
      "create_time": "2022-03-28T16:07:32.678317+08:00",
      "update_time": "2022-03-28T16:07:32.678317+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:32.678317+08:00",
      "end_time": "2022-03-28T16:07:32.678317+08:00",
      "teacher_id": 1,
      "class_id": 1
    },
    {
      "id": 5,
      "teacher_name": "解金霞",
      "grade": 1,
      "class_number": 1,
      "name": "数学",
      "week": 5,
      "weekday": 1,
      "order": 1,
      "create_time": "2022-03-28T16:07:32.757594+08:00",
      "update_time": "2022-03-28T16:07:32.757594+08:00",
      "is_delete": false,
      "start_time": "2022-03-28T16:07:32.757594+08:00",
      "end_time": "2022-03-28T16:07:32.757594+08:00",
      "teacher_id": 1,
      "class_id": 1
    }
  ]
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
|» count|integer|true|none|数据总数|
|» next|string¦null|true|none|下一页|
|» previous|string¦null|true|none|上一页|
|» results|[object]|true|none|数据列表|
|»» id|integer|true|none|none|
|»» teacher_name|string|true|none|none|
|»» grade|integer|true|none|none|
|»» class_number|integer|true|none|none|
|»» name|string|true|none|none|
|»» week|integer|true|none|none|
|»» weekday|integer|true|none|none|
|»» order|integer|true|none|none|
|»» create_time|string|true|none|none|
|»» update_time|string|true|none|none|
|»» is_delete|boolean|true|none|none|
|»» start_time|string|true|none|none|
|»» end_time|string|true|none|none|
|»» teacher_id|integer|true|none|none|
|»» class_id|integer|true|none|none|

# files

## GET 下载课程模板

GET /files/download/template/

> 返回示例

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 下载课表

POST /files/download/course/

> Body 请求参数

```json
{
  "is_application": 0,
  "week_start": 0,
  "week_end": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 否 ||none|
|body|body|object| 否 ||none|
|» is_application|body|integer| 是 | 是否下载申请表数据|none|
|» week_start|body|integer| 是 | 课表开始周次|none|
|» week_end|body|integer| 是 | 课表结束周次|none|

> 返回示例

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 更新（上传）课表

POST /files/upload/courses/

> Body 请求参数

```yaml
file: string
week_start: string

```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||none|
|body|body|object| 否 ||none|
|» file|body|string| 否 ||none|
|» week_start|body|string| 否 ||none|

> 返回示例

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 数据模型


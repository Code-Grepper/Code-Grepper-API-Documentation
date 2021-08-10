# Code Grepper

**Code Grepper** information, Bugs and Vulnerablities and tricks are posted here, Star this repo and visit frequently. Follow me(**Jareer**) on **[Code Grepper][Profile]**


## APIs

List Code Grepper APIs. Below is a table that shows what type of request does the API receive.

| Symbol | Type |
|---|---|
| 🟢 |  **`GET`** |
| 🔵 |  **`PUT`** |
| 🔴 |  **`POST`** |
| ⚪ |  **`DELETE`** |
| ⚫ |  **`OPTIONS`** |

### Application Pages

Application search API returns HTML/Text response.

```yaml
https://www.codegrepper.com/search.php?q=
```

```yaml
https://www.codegrepper.com/app/profile.php?id=98467
```

```yaml
https://www.codegrepper.com/profile/jareer
```

### Answers

saves an answer to the codegrepper website,

```yaml
https://www.codegrepper.com/api/save_answer.php 🔴
```

```yaml
https://www.codegrepper.com/api/save_comment.php 🔴
```

```yaml
https://www.codegrepper.com/api/update_answer.php 🔴
```

```yaml
https://www.codegrepper.com/api/get_answers_comments.php?aid=287391&u=98467 🟢
```

### User

```yaml
https://www.codegrepper.com/api/get_user_stats.php?uid=98467
```

Returns JSON data for a user's profile. Like `profile_image`, `fun_name`, `real_name`, `donate_link` etc.

```yaml
https://www.codegrepper.com/api/profile.php?id=98467 🟢
```

```yaml
https://www.codegrepper.com/api/follow.php?follow_user_id=98467&follow=1 🟢
```

### Teams

```yaml
https://www.codegrepper.com/api/add_team_members.php 🔴
```

### Settings

```yaml
https://www.codegrepper.com/api/update_extension_privacy.php 🔴
```

### Other

```yaml
https://www.codegrepper.com/api/send_feedback.php
```

```yaml
https://www.codegrepper.com/codeimages/for-loop-javascript.png 🟢
```

[Profile]: https://www.codegrepper.com/app/profile.php?id=98467

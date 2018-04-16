# Meeting Record Genie

## Google Document Add-on

### Usage (If add-on is already installed)

1. Open add-on: Google document > 外掛程式 > Meeting Record Genie > start.

![open add-on](https://i.imgur.com/nXjOYbf.jpg)

2. Select date and recorder.

![add-on](https://i.imgur.com/RSaVZsp.jpg)

3. Click '產生早會記錄' and links are created.

![file links](https://i.imgur.com/0WOc9Xn.jpg)

4. Your meeting record pdf is ready.

![pdf](https://i.imgur.com/qG0dQyg.jpg)

5. Here's a mail template for you.

![mail](https://i.imgur.com/Z5sNSdl.jpg)

### Google Document Format
Make sure you and your teammates follow the format to create the pdf correctly.

```
2018/04/16
Selina
進度：
Selina 昨天的進度 1。
Selina 昨天的進度 2。
預計：
Selina 今天的預計 1。

Diane
進度：
Diane 昨天的進度 1。
預計：
Diane 今天的預計 1。
Diane 今天的預計 2。

Jack
進度：
Jack 昨天的進度 1。
預計：
Jack 今天的預計 1。
Jack 今天的預計 2。
```

You could just add a new daily record above without deleting old ones. It helps genie to get old data whenever you need to re-generate previous meeting records.

### Installation
Add `google-doc-add-on/Sidebar.html` and `google-doc-add-on/Code.gs` to Google document > 工具 > 指令碼編輯器.

### Configuration
```javascript
// Sidebar.html
var CONFIG = {
  HOST: 'http://localhost:9876',
  HOST_HTTPS: 'https://localhost:9877',
  DEFAULT_START_TIME: '08:15',
  DEFAULT_END_TIME: '08:30',
  DEFAULT_LOC0: 'OO園區',
  DEFAULT_LOC1: 'OO辦公室',
  TEAM: 'OO小組',
  // Members which will appear in recorder list and document
  TEAM_MEMBERS: [
    'Selina',
    'Diane',
    'Jack',
    'Michael'
  ],
  MAIL_TO: 'group@mail.com',
  // Member pool
  MEMBERS: [
    { tw:'約翰', en: 'John', mail: 'john@mail.com' },
    { tw:'麥可', en: 'Michael', mail: 'michael@mail.com' },
    { tw:'傑克', en: 'Jack', mail: 'jack@mail.com' },
    { tw:'瑟琳娜', en: 'Selina', mail: 'selina@mail.com' },
    { tw:'黛恩', en: 'Diane', mail: 'diane@mail.com' },
    { tw:'蘿絲', en: 'Rose', mail: 'rose@mail.com' }
  ]
};
```


## Server

### Dependencies
Python 2.7
[Django 1.6](https://www.djangoproject.com/)
[django-extensions](https://github.com/django-extensions/django-extensions)

### Usage
Run with `startserver.sh` in the `server/` folder. The development server should be enough to handle the requests of a team.

You could deploy django server on Apache or Nginx if needed.

- It seems not necessary to use HTTPS certification.
- **WARNING:** The core part of building pdf from reStructuredText(rst) file is removed from this repository because it is not my contribution and might contain some classified information of the company.

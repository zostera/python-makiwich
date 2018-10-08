# Changelog


# 0.0.3 (2018-10-08)

 - Fix package by actually including the required files.

# 0.0.2 (2018-09-22)

  - Add django view, use with:

```python
from maki.contrib.django import maki_icon

path("maki_icon/<str:name>", maki_icon, name="maki_icon")
```

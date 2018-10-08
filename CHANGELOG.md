# Changelog

# 0.0.6 (2018-10-08)

 - 0.0.3, 0.0.4, 0.0.5 skipped
 - Fix package by actually including the required files.
 - Do not import version at install time to prevent importing dependencies before they could have been installed.
 - Serve icon images with proper content type.
 - Raise Http404 if symbol does not exist.


# 0.0.2 (2018-09-22)

  - Add django view, use with:

```python
from maki.contrib.django import maki_icon

path("maki_icon/<str:name>", maki_icon, name="maki_icon")
```

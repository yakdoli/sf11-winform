---
title: timezone.md
original_path: WinForms_Docs/99_Uncategorized/timezone.md
created_at: 2025-08-05
---








  









## TimeZone {#timezone style="tab-stops: 0pt"}

The Schedule appointment item's start and end times are set in the **Coordinated Universal Time (UTC)** format, while processing in controller as well as saving in the database. The appointment items are displayed with respect to this time zone.

When you change the time zone property, all appointment items move to the new time zone. For example, if you move from the Pacific Time zone to the Mountain Time zone, all of your appointments will be delayed by an hour. We can save the appointments with different time zones.

When you change time zones in local machines, the appointments timing does not change to reflect the new time zone by Schedule's TimeZone property.

[] 

Properties

Table 16: TimeZone - Properties

**[]** 


+---------------------+--------------------------------------------------------------------------+----------------------+-----------------------------------------------------+-------------+
| Property            | Description                                                              | Type of the property | Value it accepts                                    | Dependency  |
+=====================+==========================================================================+======================+=====================================================+=============+
| ShowTimeZonesButton | Used to set enable/disable the timezone button in the Appointment window | Boolean              | [True/False]                | NA          |
|                     |                                                                          |                      |                                                     |             |
|                     |                                                                          |                      |                                                     |             |
+---------------------+--------------------------------------------------------------------------+----------------------+-----------------------------------------------------+-------------+
| TimeZone            | Used to set timezone for Schedule                                        | Enum                 | [96 TimeZones are accepted] | NA          |
+---------------------+--------------------------------------------------------------------------+----------------------+-----------------------------------------------------+-------------+


 

More:






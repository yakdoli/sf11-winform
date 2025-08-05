---
title: animation4.md
original_path: WinForms_Docs/99_Uncategorized/animation4.md
created_at: 2025-08-05
---






#### Animation {#animation style="tab-stops: 0pt"}

This section describes the following:

[·      ]Animation Time for Changing the CalendarEdit Mode

[·      ]Animation Time for Month Navigation

**[]** 

Animation Time for Changing the CalendarEdit Mode

You can set the animation time for changing the mode of the CalendarEdit control, using the **ChangeModeTime** property. This dependency property sets the calendar mode changing animation time. It returns an integer value.

 

To set this property, use the following code.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<!\--][ Adding calendar with change mode time ][\--\>]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][ChangeModeTime][=]\"[10]\"[/\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| **[]**                                                              |
|                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                    |
|                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]          |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Setting calendar mode changing animation time]                   |
|                                                                                                                       |
| [calendarEdit.ChangeModeTime = 10;]                                               |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

 

Animation Time for Month Navigation

The time taken to navigate from one month to another month can be controlled using **FrameMovingTime** the property. This dependency property sets the value for month changing animation time. It returns an integer value.

 

To set this property, use the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\--][ Adding calendar with Frame moving time as 500 ][\--\>]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][FrameMovingTime][=]\"[500]\"[/\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| **[]**                                                              |
|                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                    |
|                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]          |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Setting the frame moving time]                                   |
|                                                                                                                       |
| [calendarEdit.FrameMovingTime = 500;]                                             |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

 

[]{#p46} 

[]{#related-topics}


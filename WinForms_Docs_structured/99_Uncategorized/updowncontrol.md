---
title: updowncontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\updowncontrol.md
created_at: 2025-07-03
---








  









## UpDown Control {#updown-control style="tab-stops: 0pt"}

[] 

[]{#p630}The UpDown control displays numeric values. Users can select any value by scrolling through the values by using the Increment and Decrement buttons of the UpDown control.

The features of the UpDown control include:

[·      ]Null Value

[·      ]Maximum and Minimum Value

[·      ]Maximum and Minimum Validation

[·      ]Culture

[·      ]Number Formatting

[·      ]Animation Speed

[·      ]Text Alignment

[·      ]Keyboard and Mouse support

 

Breaking Changes in the UpDown Control from Version 8.3 to Version 8.4

The event handler and event argument for the ValueChanging event have been changed in version 8.4. The changes are provided in the following tabulation:

 

Table 31: Changes in the UpDown Control from Version 8.3 to Version 8.4

+-----------------------+------------------------------------+---------------------------+
| Event Name            | Old Type                           | New Type                  |
+-----------------------+------------------------------------+---------------------------+
|                       | PropertyChangedCallback            | ValueChangingEventHandler |
|                       |                                    |                           |
| ValueChanging         |                                    |                           |
|                       +------------------------------------+---------------------------+
|                       | DependencyPropertyChangedEventArgs | ValueChangingEventArgs    |
+=======================+====================================+===========================+

 

The following properties are no longer used and will not make any changes in the UpDown control:

[·      ]CursorBackground

[·      ]CursorBorderBrush

[·      ]CursorWidth

[·      ]CursorBorderThickness

[·      ]CursorTemplate

[·      ]CursorVisible

[·      ]CursorPosition

[·      ]SelectionBrush

[·      ]AnimationShift

More:














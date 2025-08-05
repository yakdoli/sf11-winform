---
title: howtoremovetheheaderofxptaskbarboxinanxptaskbar.md
original_path: WinForms_Docs/99_Uncategorized/howtoremovetheheaderofxptaskbarboxinanxptaskbar.md
created_at: 2025-08-05
---






##### How to remove the header of XPTaskBarBox in an XPTaskBar {#how-to-remove-the-header-of-xptaskbarbox-in-an-xptaskbar style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

For this, you need to derive **XPTaskBarBox** class, and override **DetermineHeaderHeight** method as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [public][ [class] [CustomTaskBarbox] : [XPTaskBarBox]] |
|                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [    [public] CustomTaskBarbox()]                                                                                                                       |
|                                                                                                                                                                                                                  |
| [        : [base]()]                                                                                                                                    |
|                                                                                                                                                                                                                  |
| [    {]                                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [    }]                                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [    [protected] [override] [int] DetermineHeaderHeight([Graphics] g)]                |
|                                                                                                                                                                                                                  |
| [    {]                                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [        [return] 0; [// set the height as 0 here]]                                                                               |
|                                                                                                                                                                                                                  |
| [    }]                                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| [Public][ [Class] CustomTaskBarbox : [Inherits] XPTaskBarBox]                                                                                                  |
|                                                                                                                                                                                                                                                                                               |
| [    [Public] [Sub] [New]()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                               |
| [        [MyBase].New()]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| [    [End] [Sub]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                               |
| [    [Protected] [Overrides] [Function] DetermineHeaderHeight([ByVal] g [As] Graphics) [As] [Integer]] |
|                                                                                                                                                                                                                                                                                               |
| [        [Return] 0 [\' set the height as 0 here]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| [    [End] [Function]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| [End][ [Class]]                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p698} 

 

[]{#related-topics}


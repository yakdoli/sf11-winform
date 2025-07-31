---
title: definingthedisplayconditions.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingthedisplayconditions.md
created_at: 2025-07-03
---








  









### Defining the Display Conditions {#defining-the-display-conditions style="tab-stops: 0pt"}

Generic drop-downs support customizing the display conditions.

Properties

[] 


+---------------------+----------------------------------------------------------------+------------------+------------------+---------------+------------+
| Name                | Description                                                    | Type of property | Value it accepts | Default value | Dependency |
+---------------------+----------------------------------------------------------------+------------------+------------------+---------------+------------+
| InitiallyPopupShown | When set to True, it displays the pop up panel on page load.   | bool             | true/false       | false         | NA         |
|                     |                                                                |                  |                  |               |            |
|                     |                                                                |                  |                  |               |            |
+---------------------+----------------------------------------------------------------+------------------+------------------+---------------+------------+
| Text                | Defines the text to be displayed in the text box on page load. | string           | alphanumeric     | \"\"          | NA         |
|                     |                                                                |                  |                  |               |            |
|                     |                                                                |                  |                  |               |            |
+---------------------+----------------------------------------------------------------+------------------+------------------+---------------+------------+


[] 

 

Methods[]


+---------------------------+-----------------+-----------------------------+----------------------------------------------------------------+
| Method                    | Parameters      | Return type                 | Descriptions                                                   |
+---------------------------+-----------------+-----------------------------+----------------------------------------------------------------+
| InitiallyPopupShown(bool) | bool            | IMultiColumnDropDownBuilder | When set to True, it displays the pop up panel on page load.   |
|                           |                 |                             |                                                                |
|                           |                 |                             |                                                                |
|                           |                 |                             |                                                                |
|                           |                 |                             |                                                                |
+---------------------------+-----------------+-----------------------------+----------------------------------------------------------------+
| Text(string)              | string          | IMultiColumnDropDownBuilder | Defines the text to be displayed in the text box on page load. |
|                           |                 |                             |                                                                |
|                           |                 |                             |                                                                |
+---------------------------+-----------------+-----------------------------+----------------------------------------------------------------+


[] 

To open the panel on page load follow the steps below:

More:








---
title: tickmark1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tickmark1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### TickMark {#tickmark style="tab-stops: 0pt"}

 

This feature allows you to display the tick mark for the slider control.

+--------------------+---------------------------------------------+------------------+---------------------------------------------------------------------------------------------+----------------+
| Name               | Description                                 | Type of property | Value it accepts                                                                            | Dependency     |
+--------------------+---------------------------------------------+------------------+---------------------------------------------------------------------------------------------+----------------+
| EnableTickMark     | Used to enable the Tick Mark                | Bool             | True/false                                                                                  | NA             |
+--------------------+---------------------------------------------+------------------+---------------------------------------------------------------------------------------------+----------------+
| SliderTickPosition | Used to set the position for the TickMark   | Enum             | [TickPosition].BottomRight | EnableTickMark |
|                    |                                             |                  |                                                                                             |                |
|                    |                                             |                  | [TickPosition].Centre      |                |
|                    |                                             |                  |                                                                                             |                |
|                    |                                             |                  | [TickPosition].TopLeft     |                |
+--------------------+---------------------------------------------+------------------+---------------------------------------------------------------------------------------------+----------------+
| TickFrequency      | Used to set the interval for the tick marks | Int              | 0 to int MaxValue                                                                           | EnableTickMark |
+--------------------+---------------------------------------------+------------------+---------------------------------------------------------------------------------------------+----------------+

 

More:








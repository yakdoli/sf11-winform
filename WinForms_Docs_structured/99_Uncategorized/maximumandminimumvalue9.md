---
title: maximumandminimumvalue9.md
original_path: WinForms_Docs/99_Uncategorized/maximumandminimumvalue9.md
created_at: 2025-08-05
---






#### Maximum and Minimum Value {#maximum-and-minimum-value style="tab-stops: 0pt"}

MaxValue is the maximum value that can be set for the UpDown control and MinValue is the minimum value that can be set for the UpDown control.

 

Using MaxValue and MinValue

MaxValue and MinValue can be set for the UpDown control, as shown in the following code snippets.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][UpDown][ [Name][=\"upDown\"] [MaxValue][=\"100\" ][MinValue][=\"0\"/\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| [UpDown][ upDown = [new] [UpDown]();] |
|                                                                                                                                                                                                                |
| [upDown.MaxValue = 100;]                                                                                                                                 |
|                                                                                                                                                                                                                |
| [upDown.MinValue = 0;][]                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for Properties, and Events

Properties

Table36: Properties Table

  ---------- ----------------------------------------------------- -------------------- ----------- -----------------
  Property   Description                                           Type                 Data Type   Reference links
  MaxValue   Gets or sets the maximum value that can be entered.   DependencyProperty   double      Not applicable
  MinValue   Gets or sets the minimum value that can be entered.   DependencyProperty   double      Not applicable
  ---------- ----------------------------------------------------- -------------------- ----------- -----------------

 

Events

Table 37: Events Table

+-----------------+----------------------------------+-------------------------------------+-------------------------+-----------------+
| Event           | Description                      | Arguments                           | Type                    | Reference links |
+-----------------+----------------------------------+-------------------------------------+-------------------------+-----------------+
| MaxValueChanged | Occurs when MaxValue is changed. | DependencyObject and                | PropertyChangedCallback | Not applicable  |
|                 |                                  |                                     |                         |                 |
|                 |                                  | DependencyPropertyChangedEventArgs. |                         |                 |
+-----------------+----------------------------------+-------------------------------------+-------------------------+-----------------+
| MinValueChanged | Occurs when MinValue is changed. | DependencyObject and                | PropertyChangedCallback | Not applicable  |
|                 |                                  |                                     |                         |                 |
|                 |                                  | DependencyPropertyChangedEventArgs. |                         |                 |
+=================+==================================+=====================================+=========================+=================+

[] 

[]{#related-topics}


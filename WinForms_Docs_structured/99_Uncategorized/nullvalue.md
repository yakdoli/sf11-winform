---
title: nullvalue.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nullvalue.md
created_at: 2025-07-03
---






#### Null Value {#null-value style="tab-stops: 0pt"}

The Null Value feature enables the UpDown control to accept null values.

**[]** 

Using NullValue and UseNullOption

You can enter a null value in the UpDown control only if the UseNullOption is set to true. Also, you can specify a value to be displayed in the UpDown control when the value of the UpDown control is set to null by using the NullValue property.

NullValue can be set for the UpDown control, as shown in the following code snippets.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][UpDown][ [Name][=\"upDown\"] [UseNullOption][=\"true\" ][NullValue][=\"1\"/\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| [UpDown][ upDown = [new] [UpDown]();] |
|                                                                                                                                                                                                                |
| [upDown.UseNullOption = [true];]                                                                                                    |
|                                                                                                                                                                                                                |
| [upDown.NullValue = 2;]                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for Properties, and Events

Properties

Table 34: Properties Table

  --------------- ---------------------------------------------------------------------------------------------------------- -------------------- ----------- -----------------
  Property        Description                                                                                                Type                 Data Type   Reference links
  UseNullOption   Gets or sets the value that indicates whether to use the null value.                                       DependencyProperty   bool        Not applicable
  NullValue       Gets or sets a value to be displayed in the UpDown control when the value of the UpDown control is null.   DependencyProperty   double?     Not applicable
  --------------- ---------------------------------------------------------------------------------------------------------- -------------------- ----------- -----------------

 

Events

Table 35: Event Table

+----------------------+-------------------------------------------------+-------------------------------------+-------------------------+-----------------+
| Event                | Description                                     | Arguments                           | Type                    | Reference links |
+----------------------+-------------------------------------------------+-------------------------------------+-------------------------+-----------------+
| UseNullOptionChanged | Occurs when the UseNullOption value is changed. | DependencyObject and                | PropertyChangedCallback | Not applicable  |
|                      |                                                 |                                     |                         |                 |
|                      |                                                 | DependencyPropertyChangedEventArgs. |                         |                 |
+======================+=================================================+=====================================+=========================+=================+

[] 

[]{#related-topics}


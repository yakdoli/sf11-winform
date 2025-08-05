---
title: optionsinregularmode.md
original_path: WinForms_Docs/99_Uncategorized/optionsinregularmode.md
created_at: 2025-08-05
---






##### Options in Regular Mode {#options-in-regular-mode style="tab-stops: 0pt"}

[] 

ProgressBar control when used in WaitingMode, the following properties can be set.

[] 

Text

[] 

Text can be displayed on the control. To display the required text, set the **ProgressBarText** property to that text.

[] 


  ----------------- ----------------------------------------------------
  Property          Description
  ProgressBarText   Specifies the text to be displayed on the control.
  ----------------- ----------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                     |
| []                                                                 |
|                                                                                                                     |
| [ProgressBar1.ProgressBarText = [\"Loading page\...\"];] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.ProgressBarText = [\"Loading page\...\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Progress Value

[] 

The **TextStyle** property allows you to either display the progress value in percentage or in numerical value. To display the text make sure that the **TextVisible** property is enabled which controls the visibility of the text.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| ProgressPercentage                | Specifies the value, relative to which the control percentage value increases.                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| TextStyle                         | Specifies how to display the progress value. Default value is Percentage. The options included are as follows: |
|                                   |                                                                                                                |
|                                   | [·      ]Percentage                                                               |
|                                   |                                                                                                                |
|                                   | [·      ]Value                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| TextVisible                       | Gets/sets the boolean value, whether the progress bar text should be visible. Default value is true.           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                      |
| []                                                                  |
|                                                                                                                      |
| [ProgressBar1.TextStyle = [TextStyle].Value;]               |
|                                                                                                                      |
| [ProgressBar1.TextVisible = [TextVisible].True;]            |
|                                                                                                                      |
| [ProgressBar1.ProgressBarText = [\"Loading page\...\"];]  |
|                                                                                                                      |
| [ProgressBar1.ProgressStyle = [ProgressStyle].WaitingMode;] |
|                                                                                                                      |
| [ProgressBar1.Frequency = 10;]                                                   |
|                                                                                                                      |
| [ProgressBar1.ProgressPercentage = 100;]                                         |
+----------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.TextStyle = TextStyle.Value]                                     |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.TextVisible = TextVisible.True]                                  |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.ProgressBarText = [\"Loading page\...\"]] |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.ProgressStyle = ProgressStyle.WaitingMode]                       |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.Frequency = 10]                                                  |
|                                                                                                                                                                               |
| [Private][ ProgressBar1.ProgressPercentage = 100]                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Refreshing the control

[] 

The control can be updated every time after the specified **Frequency** interval. This updates and refreshes the content without postback.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                              |
|                                   |                                                                                                              |
| Property                          | Description                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| Frequency                         | Specifies the frequency in which the control should update itself without a postback. Default value is 1000. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
| []                   |
|                                                                       |
| [ProgressBar1.Frequency = 2000;]  |
+-----------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                               |
|                                                                                                                                |
| []                                                                            |
|                                                                                                                                |
| [Private][ ProgressBar1.Frequency = 2000] |
+--------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


---
title: settheintervalbywhichthenumericvalueswillbeincreasedordecreasedintheupdowncontrol.md
original_path: WinForms_Docs/99_Uncategorized/settheintervalbywhichthenumericvalueswillbeincreasedordecreasedintheupdowncontrol.md
created_at: 2025-08-05
---






#### Set the interval by which the numeric values will be increased or decreased in the UpDown control {#set-the-interval-by-which-the-numeric-values-will-be-increased-or-decreased-in-the-updown-control style="tab-stops: 0pt"}

The Step property is used to specify the interval to be incremented or decremented in the UpDown control when the repeat buttons are clicked. The Step value can be set for the UpDown control, as shown in the following code snippets.

In the following example, the Step value is set to 3 so that the value in the UpDown control will increase or decrease by 3 when users click the repeat buttons.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][UpDown][ Name][=\"upDown\"][ Step][=\"3\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            ][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        ][\</][ syncfusion][:][UpDown][\>]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| [UpDown][ upDown = [new] [UpDown]();] |
|                                                                                                                                                                                                                |
| [upDown.Step = 3;][]                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


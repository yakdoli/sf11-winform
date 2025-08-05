---
title: setthedisplaymode.md
original_path: WinForms_Docs/99_Uncategorized/setthedisplaymode.md
created_at: 2025-08-05
---








  









## Set the Display Mode {#set-the-display-mode style="tab-stops: 0pt"}

You can view the result of the report in both Chart and Grid. To view it in any one of the two, set the display mode by using the DisplayMode API as follows.

Code Snippet for DisplayMode settings:

 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| [//// To display the Client with both Chart and Grid (Default)\                                                              |
| this.OlapClient.DisplayMode = Syncfusion.Silverlight.Client.Olap.DisplayModes.Both;\                                         |
|  \                                                                                                                           |
| //// To display the Client only with Chart]                                              |
|                                                                                                                              |
| [this.OlapClient.DisplayMode = Syncfusion.Silverlight.Client.Olap.DisplayModes.ChartOnly;\                                   |
|  \                                                                                                                           |
| //// To display the Client only with Grid\                                                                                   |
| this.OlapClient.DisplayMode = Syncfusion.Silverlight.Client.Olap.DisplayModes.GridOnly;] |
|                                                                                                                              |
| []                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                            |
|                                                                                                                             |
| []                                                                                      |
|                                                                                                                             |
| [\'// To display the Client with both Chart and Grid (Default)]                         |
|                                                                                                                             |
| [Me.OlapClient.DisplayMode Syncfusion.Silverlight.Client.Olap.DisplayModes.Both;]       |
|                                                                                                                             |
| []                                                                                      |
|                                                                                                                             |
| [\'// To display the Client only with Chart]                                            |
|                                                                                                                             |
| [Me.OlapClient.DisplayMode = Syncfsion.Silverlight.Client.Olap.DisplayModes.ChartOnly;\                                     |
| \                                                                                                                           |
| ]                                                                                       |
|                                                                                                                             |
| [\'// To display the Client only with Grid]                                             |
|                                                                                                                             |
| [Me.OlapClient.DisplayMode = Syncfusion.Silverlight.Client.Olap.DisplayModes.GridOnly;] |
|                                                                                                                             |
| []                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


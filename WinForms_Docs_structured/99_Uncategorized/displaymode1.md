---
title: displaymode1.md
original_path: WinForms_Docs/99_Uncategorized/displaymode1.md
created_at: 2025-08-05
---








  









## Display Mode {#display-mode style="tab-stops: 0pt"}

The display is used to specify whether you want to view the output of the report in both Chart and Grid or in any one of them.  

There are three display Modes in OLAP Client, namely:

 

Both -- This will include both Chart and Grid for displaying the output of the report.

Chart -- This will contain only Chart for displaying the output of the report.

Grid -- This will contain only Grid for displaying the output of the report.

These display modes will increase the performance when you set the display mode to either Chart or Grid instead of both. It will increase the performance of the OLAP Client.

Code snippet for Changing the Display Mode:

 

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
+-----------------------------------------------------------------------------------------------------------------------------+

 

Use Case Scenarios

When users want to view reports only in Chart or Grid, they can set the corresponding display mode to exclude another control.

[]{#related-topics}


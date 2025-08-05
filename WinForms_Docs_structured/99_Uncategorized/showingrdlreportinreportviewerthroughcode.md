---
title: showingrdlreportinreportviewerthroughcode.md
original_path: WinForms_Docs/99_Uncategorized/showingrdlreportinreportviewerthroughcode.md
created_at: 2025-08-05
---








  









## Showing RDL Report in Report Viewer through Code {#showing-rdl-report-in-report-viewer-through-code style="tab-stops: 0pt"}

 

You can create a simple sample through code with Syncfusion WPF ReportViewer control by using the following steps.

 

1.   Create a new WPF application in VS2008/VS2010.

2.   To add related references to the created application, right-click on **References** and select **Add Reference**.

 

{border="0"}

Figure 13: Adding References

 


{border="0"}Note: The added references will be appeared under References folder.

 


{border="0"}

Figure 14: Added References

 

3.   Set Grid name in auto generated XAML of MainWindow.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][Window][ x][:][Class][=\"WpfApplication13.MainWindow\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [             [ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [             [ xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [       [ Title][=\" Mail Merge\"][ Height][=\"350\"][ Width][=\"525\"\>]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][Grid][ Name][=\"grid1\"\>][]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\</][Grid][\>][]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][Window][\>][]                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Add ReportViewer in MainWindow grid.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[  ]**[   [// ReportViewer control initialization]]                                                 |
|                                                                                                                                                                                                     |
| [                  Syncfusion.Windows.Reports.Viewer.ReportViewer reportViewer1 = [new] Syncfusion.Windows.Reports.Viewer.ReportViewer();] |
|                                                                                                                                                                                                     |
| [       ]                                                                                                                                                       |
|                                                                                                                                                                                                     |
| [                  [// Set ReportPath to view the Report in ReportViewer.]]                                                               |
|                                                                                                                                                                                                     |
| [                  reportViewer1.ReportPath=[@\"D:\\MailMerge.rdl\"];]                                                                  |
|                                                                                                                                                                                                     |
| [       ]                                                                                                                                                       |
|                                                                                                                                                                                                     |
| [                  [// Add ReportViewer in MainWindow grid]]                                                                              |
|                                                                                                                                                                                                     |
| [                  [this].grid1.Children.Add(reportViewer1);]                                                                              |
|                                                                                                                                                                                                     |
| [       ]                                                                                                                                                       |
|                                                                                                                                                                                                     |
| [                  [this].Loaded += (sender, arg) =\>]                                                                                     |
|                                                                                                                                                                                                     |
| [                      {]                                                                                                                                       |
|                                                                                                                                                                                                     |
| [                          [// To Render the Report in ReportViewer.]]                                                                    |
|                                                                                                                                                                                                     |
| [                          reportViewer1.RefreshReport();]                                                                                                      |
|                                                                                                                                                                                                     |
| [                      };]                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application. The following output will be displayed.

 

{border="0"}

Figure 15: Report Viewer Sample RDL demo

 

[]{#related-topics}


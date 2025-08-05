---
title: showingrdlcreportsinreportviewer1.md
original_path: WinForms_Docs/99_Uncategorized/showingrdlcreportsinreportviewer1.md
created_at: 2025-08-05
---








  









## Showing RDLC Reports in Report Viewer {#showing-rdlc-reports-in-report-viewer style="tab-stops: 0pt"}

 

You can show RDLC reports in Report Viewer by using following steps.

 

1.   Initialize Report Viewer control and set the **ReportPath** to load the RDLC reports from local machine.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                     |
|                                                                                                                                                                         |
| [// ReportViewer control initialization]                                                                               |
|                                                                                                                                                                         |
| [Syncfusion.Windows.Reports.Viewer.ReportViewer reportViewer1 = new Syncfusion.Windows.Reports.Viewer.ReportViewer();] |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| [// Set ReportPath to view the Report in ReportViewer.]                                                                |
|                                                                                                                                                                         |
| [      reportViewer1.ReportPath = @\"D:\\Company Sales.Rdlc\";]                                                        |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| [// Add ReportViewer in MainWindow grid]                                                                               |
|                                                                                                                                                                         |
| [this.grid1.Children.Add(reportViewer1);]                                                                              |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: To load the company sales report, you can use following installed sample location.

\<InstalledLocation\>\\Syncfusion\\Essential Studio\\\<Version Number\>\\ Common\\Data\\ReportTemplate\\Company Sales.rdl


 

2.   Set the **ProcessingMode** as Local to process a local report in Report Viewer.

 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                       |
|                                                                                                                                           |
| [// To render the report based on local Data Source]                                     |
|                                                                                                                                           |
| [reportViewer1.ProcessingMode = Syncfusion.Windows.Reports.Viewer.ProcessingMode.Local;] |
|                                                                                                                                           |
| []                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Set the **DataSources** to view the report in Report Viewer.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [reportViewer1.DataSources.Clear();]                                                                                                           |
|                                                                                                                                                                                                 |
| [reportViewer1.DataSources.Add(new Syncfusion.Windows.Reports.ReportDataSource { Name = \"Sales\", Value = new AdventureWorks().GetData() });] |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: AdventureWorks().GetData() information can be obtained from following location.

\<Installed Location\>\\Syncfusion\\Essential Studio\\\<Version Number\>\\ Reports\\WPF\\ReportViewer.WPF\\Samples\\Product Showcase\\Company Sales\\CS\\DataSource.cs


 

4.   Use **RefreshReport** method to render the RDLC report in Report Viewer.

 

+--------------------------------------------------------------------------------------------------+
| []                                              |
|                                                                                                  |
| [this.Loaded += (sender, arg) =\>]              |
|                                                                                                  |
| [{]                                             |
|                                                                                                  |
| [     // To Render the Report in ReportViewer.] |
|                                                                                                  |
| [     reportViewer1.RefreshReport();]           |
|                                                                                                  |
| [};][]      |
+--------------------------------------------------------------------------------------------------+

 

5.   Run the application. The following output displays.

 

{border="0"}

Figure 16: ReportViewer RDLC Sample

 

[]{#related-topics}


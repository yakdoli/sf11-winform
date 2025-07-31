---
title: loadandsavereport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadandsavereport1.md
created_at: 2025-07-03
---








  









### Load and Save report {#load-and-save-report style="tab-stops: 0pt"}

OLAP Client will allow us to create multiple reports and store them as XML files containing all the reports. Each XML file may contain any number of reports. Also, you can store the reports in Stream.

Steps to save and load a newly created report:

1.   Click New session to create a new session, else add a new report by clicking Add Report.

2.   Drag and drop the required elements in the required axis. By this axis, the element will be added to the current report. You can drag and drop any number of elements in any axis.

{border="0"}

 

Figure 21: Dragging and Dropping Elements from the Cube Dimension Browser to the Axis

3.   Once you finish the drag and drop of elements, save the current session.

4.   You can add any number of reports to the current report set.

5.   To add a report, click Add Report and provide a name for the new report.

 

{border="0"}

 

Figure 22: Adding a New Report to the Current Report Set

 

{border="0"}

 

Figure 23: Entering the Name for the New Report

 

6.   After creating the reports, save the current report set as an XML file by clicking the Save button in the OLAP Client toolbar.

 

{border="0"}

 

Figure 24: Saving the Created report Set as an XML File

{border="0"}

 

Figure 25: Saving the Report Set as an XML File by Providing the Name of the File

 

7.   To load a report, click the Load button in the OLAP Client toolbar. A file dialog window will appear. Choose the stored xml file to view.

 

{border="0"}

 

Figure 26: Loading the Existing Report Set (XML File)

 

 

{border="0"}

 

Figure 27: Loading the reports from the Saved XML File

 

 

{border="0"}

 

Figure 28: Loading the Existing Report Set (XML File)

 

 

{border="0"}

 

Figure 29: Loading the reports from the Saved XML File

 

Code snippet

Loading a Report from the file:

 

+------------------------------------------------------------------------------+
| **[\[C#\]]**                             |
|                                                                              |
| [//// To load xml report file\                                               |
| this.OlapClient.LoadReportDefinition();] |
|                                                                              |
| []                                       |
+------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------+
| **[\[VB\]]**                           |
|                                                                            |
| [  \' To load xml report file]         |
|                                                                            |
| [Me.OlapClient.LoadReportDefinition()] |
|                                                                            |
| []                                     |
+----------------------------------------------------------------------------+

 

Saving the Report:

 

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
| [//// To save the current session as an Xml file\                     |
| this.OlapClient.SaveReport();]    |
|                                                                       |
| []                                |
+-----------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------+
| **[\[VB\]]**                                   |
|                                                                                    |
| [\'To save the current session as an Xml file] |
|                                                                                    |
| [Me.OlapClient.SaveReport()]                   |
|                                                                                    |
| []                                             |
+------------------------------------------------------------------------------------+

 

Use Case Scenarios

Users can create a report and save it as an XML file for use in future. In an IT scenario, a user can create and save the report in some location and another user can load it and view it.

 

[]{#related-topics}


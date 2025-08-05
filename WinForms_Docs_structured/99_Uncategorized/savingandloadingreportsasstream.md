---
title: savingandloadingreportsasstream.md
original_path: WinForms_Docs/99_Uncategorized/savingandloadingreportsasstream.md
created_at: 2025-08-05
---








  









## Saving and loading report(s) as stream {#saving-and-loading-reports-as-stream style="tab-stops: 0pt"}

[]{#_Saving_report(s)_as}Saving report(s) as stream

GetReportStream() - By using this method, user can get the current report set as a stream which can be stored anywhere, for example, database.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                              |
| [Stream][ reportStream = [this].olapClient1.GetReportStream();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                     |
|                                                                                                                                                                                                      |
| [Dim][ reportStream [As] Stream = [Me].olapClient1.GetReportStream()] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_LoadReportStream}[]{#_LoadReportStream(_)} 

 

 

[]{#_Loading_report(s)_as}Loading report(s) as stream

LoadReportStream() - By using this method, user can load the report as a stream. This method will accept a stream format of the report as argument. By invoking this method the reports in the stream format will be populated in the report list as well as in chart/grid control.  The following code snippet will illustrate how to load the report in stream format.

 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                           |
| [this][.olapClient1.LoadReportStream(reportStream);] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                       |
|                                                                                                                                        |
| [Me][.olapClient1.LoadReportStream(reportStream)] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[]{#_AutoExecute}[[]]{.Heading4Char} 

 

Table 19: Methods

 


+--------------------+------------------------------------------------------------------+------------+-------------+-------------+----------------+
| Methods            | Description                                                      | Parameters | Type        | Return type | Reference link |
+--------------------+------------------------------------------------------------------+------------+-------------+-------------+----------------+
| GetReportStream()  | Used to get the current session of the report in stream format.  | \-         |             |             | \-             |
|                    |                                                                  |            |             |             |                |
|                    |                                                                  |            | Server side | Stream      |                |
+--------------------+------------------------------------------------------------------+------------+-------------+-------------+----------------+
| LoadReportStream() | The method is used to load the report which is in stream format. | Stream     |             | void        | \-             |
|                    |                                                                  |            |             |             |                |
|                    |                                                                  |            | Server side |             |                |
+--------------------+------------------------------------------------------------------+------------+-------------+-------------+----------------+


 

Sample Link

A sample demo is available at the following link:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapClient.Web\\Samples\\3.5\\OlapClient\\** **ReportsAsStreamDemo**

[]{#related-topics}


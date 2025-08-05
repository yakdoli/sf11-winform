---
title: getthereportsintheolapdatamanagerasastream.md
original_path: WinForms_Docs/03_Data_Binding/getthereportsintheolapdatamanagerasastream.md
created_at: 2025-08-05
---








  









## Get the reports in the OlapDataManager as a stream {#get-the-reports-in-the-olapdatamanager-as-a-stream style="tab-stops: 0pt"}

You can get the report collection in the OlapDataManager as a stream by using GetReportAsStream method. This method will return the current report collection of the OlapDataManager as a stream.

The following code snippet will explain obtaining the report as a stream:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [Stream][ reportStream = olapDataManager.GetReportAsStream();][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| [Dim][ reportStream [As] [Stream] = olapDataManager.GetReportAsStream()][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}


---
title: savethereportasxmlfile.md
original_path: WinForms_Docs/99_Uncategorized/savethereportasxmlfile.md
created_at: 2025-08-05
---








  









## Save the report as xml file {#save-the-report-as-xml-file style="tab-stops: 0pt"}

The user can save the current report set of OlapDataManager as an xml file for the future needsby using the SaveReport method.

The following code snippet will illustrate the saving of the current report set as an xml file:

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                         |
| []                                                                                                  |
|                                                                                                                                         |
| [olapDataManager.SaveReport([@\"C:\\SampleReport\\RevenueAnalysis.xml\"]);] |
|                                                                                                                                         |
| []                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                      |
|                                                                                                                                       |
| [       ]                                                                                         |
|                                                                                                                                       |
| [olapDataManager.SaveReport([\"C:\\SampleReport\\RevenueAnalysis.xml\"])] |
|                                                                                                                                       |
| []                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

For Silverlight:

 

You can save the current report of OlapDataManger as an xml file for their future use by serializing the report with **XmlSerializer**.

The following code snippet will illustrate the saving of the current report set as an xml file:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [private][ [void] SaveReport()\                                                                                                                                                          |
| {\                                                                                                                                                                                                                                                        |
|    [SaveFileDialog] dlg = [new] [SaveFileDialog]();\                                                                                                                                 |
|    dlg.Filter = [\"XML files (\*.xml)\|\*.xml\"];\                                                                                                                                                                                |
|  \                                                                                                                                                                                                                                                        |
|    [bool]? b = dlg.ShowDialog();\                                                                                                                                                                                                    |
|  \                                                                                                                                                                                                                                                        |
|    [if] (b.HasValue && b.Value)\                                                                                                                                                                                                     |
|    {\                                                                                                                                                                                                                                                     |
|       [using] ([Stream] stream = dlg.OpenFile())\                                                                                                                                                            |
|       {\                                                                                                                                                                                                                                                  |
|          System.Xml.Serialization.[XmlSerializer] serializer = [new] System.Xml.Serialization.[XmlSerializer]([typeof]([OlapReport]));\ |
|          serializer.Serialize(stream, [this].olapDataManager.CurrentReport);             \                                                                                                                                           |
|       }\                                                                                                                                                                                                                                                  |
|    }            \                                                                                                                                                                                                                                         |
| }]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] SaveReport()]                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [   [Dim] dlg [As] SaveFileDialog = [New] SaveFileDialog()]                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [   dlg.Filter = \"XML files (\*.xml)\|\*.xml\"]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [   [Dim] b [As] Nullable([Of] [Boolean]) = dlg.ShowDialog()]                                                                                     |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [   [If] b.HasValue [AndAlso] b.Value [Then]]                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [        [Using] stream [As] Stream = dlg.OpenFile()]                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [             [Dim] serializer [As] System.Xml.Serialization.XmlSerializer = [New] System.Xml.Serialization.XmlSerializer([GetType](OlapReport))] |
|                                                                                                                                                                                                                                                                           |
| [             serializer.Serialize(stream, [Me].olapDataManager.CurrentReport)]                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [        [End] [Using]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [   [End] [If]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


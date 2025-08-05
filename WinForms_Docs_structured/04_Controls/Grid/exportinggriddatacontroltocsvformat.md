---
title: exportinggriddatacontroltocsvformat.md
original_path: WinForms_Docs/04_Controls/Grid/exportinggriddatacontroltocsvformat.md
created_at: 2025-08-05
---








  









### Exporting GridDataControl to CSV Format {#exporting-griddatacontrol-to-csv-format style="tab-stops: 0pt"}

[] 

The **ExportToCSV** method of the **GridModelExportExtensions** class enables **GridDataControl** to easily be exported to CSV format.

First, the following .dll files must be added along with the default .dll files in the reference folder:

 

[·      ]Syncfusion.XlsIO.Base

[·      ]Syncfusion.XlsIO.WPF 

[·      ]Syncfusion.GridConverter.Wpf

[] 

The following code illustrates converting the entire content of GridDataControl to a CSV file.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                               |
|                                                                                                                                                                |
| **[]**                                                                                                                     |
|                                                                                                                                                                |
| [this][.gdc.Model.ExportToCSV([\"Sample.csv\"]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the output in Figure 1 will display.

[] 

[] 

{border="0"}

Figure 195: GridDataControl to be Exported

Exporting to CSV

Now, to export the file to CSV format, simply click Export to CSV; GridDataControl will then export data to a CSV file, as seen in Figure 2.

[] 

{border="0"}

Figure 196: Exported Grid Content In CSV format

[]{#p277} 

 

[]{#related-topics}


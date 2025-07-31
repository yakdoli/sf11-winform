---
title: throughvisualstudio7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughvisualstudio7.md
created_at: 2025-07-03
---








  





### Through Visual Studio {#through-visual-studio style="tab-stops: 0pt"}

Following are the steps to add the Spreadsheet control to a Silverlight application using VisualStudio.

 

1.   Create a new Silverlight application in Visual Studio.

2.   In Visual Studio Toolbox, click **Syncfusion Silverlight Toolbox** tab.

 

 

{border="0"}

Figure 10: ToolBox

 

3.   Drag **SpreadsheetControl** to the Designer area.

4.   Customize the properties of SpreadsheetControl using **Properties** window.

 


{border="0"} Note: To add the SpreadsheetRibbon control to your application, drag SpreadsheetRibbon to the Designer area and set the Spreadsheet contol as DataContext as shown the following code.


 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XMAL\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| [\<[syncfusion]:[SpreadsheetRibbon][ DataContext]=\"{[Binding][ ElementName]=spreadsheetControl1}\"/\>][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


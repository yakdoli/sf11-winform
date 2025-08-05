---
title: throughvisualstudio2.md
original_path: WinForms_Docs/99_Uncategorized/throughvisualstudio2.md
created_at: 2025-08-05
---








  









### Through Visual Studio {#through-visual-studio style="tab-stops: 0pt"}

Following are the steps to add the Spreadsheet control to WPF application using Visual Studio.

                                  

1.   Create a new WPF application in Visual Studio.

2.   In Visual Studio Toolbox, click **Syncfusion WPF Toolbox** tab.

 

{border="0"}

Figure 8: ToolBox

 

3.   Drag **SpreadsheetControl** to the Designer area.

4.   Customize the properties of SpreadsheetControl using **Properties** window.


{border="0"}Note: To add the SpreadsheetRibbon control to your application, drag SpreadsheetRibbon to the Designer area and set the Spreadsheet contol as a DataContext as shown the following code.


 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XMAL\]]**[]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [\<[syncfusion]:[SpreadsheetRibbon][ DataContext]=\"{[Binding][ ElementName]=spreadsheetControl1}\"/\>][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


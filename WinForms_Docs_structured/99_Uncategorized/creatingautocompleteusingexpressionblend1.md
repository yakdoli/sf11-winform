---
title: creatingautocompleteusingexpressionblend1.md
original_path: WinForms_Docs/99_Uncategorized/creatingautocompleteusingexpressionblend1.md
created_at: 2025-08-05
---






#### Creating AutoComplete using Expression Blend {#creating-autocomplete-using-expression-blend style="tab-stops: 0pt"}

The AutoComplete control provides full Blend support. Here are the step-by-step instructions to create a WPF application in Blend.

1.   Open Blend, On the **File** Menu click New Project. This opens the New Project dialog box.

[] 

{border="0"}

Figure 16: Create New project in Expression Blend

**[]** 

2.   In the Project type's panel, select WPF application and then click OK.

{border="0"}

Figure 17: Create New WPF Application in Expression Blend

 

3.   Add the following Reference with the sample project.

[·      ]Syncfusion.Tools.WPF.dll

[] 

4.   On the Window menu, select Assets. This opens the Assets Library dialog box. In the Search box, type AutoComplete. This displays the search results as shown below-.

 

{border="0"}

Figure 18: AutoComplete Displayed in Assets window

 

5.   Drag the AutoComplete control to the Design View.

 

{border="0"}

Figure 19: AutoComplete Drag & Drop from Asset window

 

6.   You can now customize the properties of the AutoComplete in the Properties Window.

 

{border="0"}

Figure 20: Properties Window

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][local][:][ProductSource][ [x][:][Key][=\"Src\"/\>]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][AutoComplete x][:][Name][=\"AutoComplete1\" ][Source][=\"Custom"][ [CustomSource][=\"{StaticResource Src}\"/\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [List][\<[String]\> ProductSource = [new] [List]\<[String]\>();] |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Diagram\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Gauge\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"GridView\"]);]                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Chart\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Business Intelligence\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Schedule\"]);]                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Grid\"]);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"DocIo\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"XlsIo\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [customSource.Add([\"Pdf\"]);]                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 21: AutoComplete Created Using Blend

**[]** 

[]{#related-topics}


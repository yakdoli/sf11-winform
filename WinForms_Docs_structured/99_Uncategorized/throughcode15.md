---
title: throughcode15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode15.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The MultiPage control allows you to create the page elements programmatically.

[] 

1.   Open a new ASP.NET Web application.

119.   In .cs file, add the following code snippet.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Load([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    [if] (!IsPostBack) AddPages(); ]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [private][ [void] AddPages()]                                                          |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    PageView essentialToolsPage=[new] PageView ();]                                                                                                    |
|                                                                                                                                                                                                                                  |
| [    HtmlImage et=[new] HtmlImage(); ]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [    et.Src=[\"./images/Tools.jpg\"]; ]                                                                                                               |
|                                                                                                                                                                                                                                  |
| [    essentialToolsPage.Controls.Add(et);]                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [                        ]                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [    PageView essentialGridPage=[new] PageView ();]                                                                                                     |
|                                                                                                                                                                                                                                  |
| [    HtmlImage eg=[new] HtmlImage(); ]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [    eg.Src=[\"./images/Grid.jpg\"];]                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [    essentialGridPage.Controls.Add(eg);]                                                                                                                                    |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [    PageView essentialGroupingPage=[new] PageView ();]                                                                                                 |
|                                                                                                                                                                                                                                  |
| [    HtmlImage egroup=[new] HtmlImage(); ]                                                                                                              |
|                                                                                                                                                                                                                                  |
| [    egroup.Src=[\"./images/Grouping.jpg\"];]                                                                                                         |
|                                                                                                                                                                                                                                  |
| [    essentialGroupingPage.Controls.Add(egroup);]                                                                                                                            |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [    MultiPage1.Controls.Add(essentialToolsPage);  ]                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [    MultiPage1.Controls.Add(essentialGridPage);  ]                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    MultiPage1.Controls.Add(essentialGroupingPage);  ]                                                                                                                      |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [    MultiPage1.SelectedIndex=1;  ]                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [If] ([Not] IsPostBack) [Then]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [        AddPages()]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [End] [If]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] AddPages()]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Dim] essentialToolsPage [As] PageView = [New] PageView()]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Dim] et [As] HtmlImage = [New] HtmlImage()]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [    et.Src = [\"./images/Tools.jpg\"]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [    essentialToolsPage.Controls.Add(et)]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Dim] essentialGridPage [As] PageView = [New] PageView()]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Dim] eg [As] HtmlImage = [New] HtmlImage()]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [    eg.Src = [\"./images/Grid.jpg\"]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                               |
| [    essentialGridPage.Controls.Add(eg)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Dim] essentialGroupingPage [As] PageView = [New] PageView()]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Dim] egroup [As] HtmlImage = [New] HtmlImage()]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [    egroup.Src = [\"./images/Grouping.jpg\"]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [    essentialGroupingPage.Controls.Add(egroup)]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [    MultiPage1.Controls.Add(essentialToolsPage)]                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

120.   In the HTML view, add the following code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [function] GoTo(index)]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    {]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [if](!(index \>= 0 && index \< \_sfMultiPage1.PageCount()))]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            alert([\'Invalid index: \'] + index);]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [return];]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        }]                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        \_sfMultiPage1.SetIndex(index);]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    }]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][script][\>]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][INPUT][ [type][=\"button\"] [onclick][=\"GoTo(0);\"] [value][=\"Essential Tools\"\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][INPUT][ [type][=\"button\"] [onclick][=\"GoTo(1);\"] [value][=\"Essential Grid\"\>]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][INPUT][ [type][=\"button\"] [onclick][=\"GoTo(2);\"] [value][=\"Essential Grouping\"\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

121.   Build and run the application.

[] 

{border="0"}

**[]** 

Figure 314: Programmatically created Multipage

 

[]{#related-topics}


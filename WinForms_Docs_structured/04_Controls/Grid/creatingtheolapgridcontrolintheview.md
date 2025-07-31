---
title: creatingtheolapgridcontrolintheview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\creatingtheolapgridcontrolintheview.md
created_at: 2025-07-03
---








  









### Creating the OlapGrid Control in the View {#creating-the-olapgrid-control-in-the-view style="tab-stops: 0pt"}

To create OlapGrid Control in View:

1.   Add the following code in the Index.aspx file:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Olap().OlapGrid([\"olapgrid\"],([OlapDataManager])ViewData\[[\"DataManager\"]\])] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [ [%\>]]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

It is important that, the \"id\" used in the FlatGrid.aspx file and in the HomeController.cs file should match in order to ensure binding of the properties to the control.

 

2.   Add two methods in HomeController ( one for loading the view and one for handling the grid paging/sorting actions)

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\<summary\>][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ Used to bind the Grid.][]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\</summary\>][]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\<returns\>][View page, displays the Grid][\</returns\>][]                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [public][ [ActionResult] Index()]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [     ViewData\[[\"DataManager\"]\] = [this].GetOlapDataManger([true]);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [ return][ View();]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\<summary\>][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ Paging/sorting Requests are mapped to this method. This method invokes the ][]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ HtmlActionResult from the Grid. The Required response is generated.][]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\</summary\>][]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\<param name=\"args\"\>][Contains paging properties ][\</param\>][]                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\<returns\>][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ HtmlActionResult, returns the data displayed on the Grid][]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [///][ ][\</returns\>][]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [public][ [ActionResult] Index(][OlapGridParams][ olapGridParams][)][] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [       return][ [new] [OlapGridHtmlResult](olapGridParams, [this].GetOlapDataManger([false]));]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [ }]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


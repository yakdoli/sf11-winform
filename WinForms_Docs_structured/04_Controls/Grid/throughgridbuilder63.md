---
title: throughgridbuilder63.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder63.md
created_at: 2025-08-05
---






#### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

1.  Create a model in the application (Refer to ).

2.  Create a strongly typed view (Refer to ).

3.  In the **view**, you can use its **Model** property in **Datasource()** to bind the data source. To use the QueryCellInfo feature for your grid you should use the **QueryCellInfo** property.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml[\]]]**                                                                                |
|                                                                                                                                                                                                                      |
| [\@{][\                                                                                                                                         |
| Html.MobSyncfusion().Grid\<Standings\>(\"grid\")]                                                                                                                   |
|                                                                                                                                                                                                                      |
| [                    .Datasource(Model).Caption(\"Admin:36 Items\")]                                                                                                |
|                                                                                                                                                                                                                      |
| [                    .ActionMode(MobActionMode.Server).EnablePaging()]                                                                                              |
|                                                                                                                                                                                                                      |
| [                    .Column(col =\>]                                                                                                                               |
|                                                                                                                                                                                                                      |
| [                       {]                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [                           col.Add(c =\> c.Team).HeaderText(\"Team\");]                                                                                            |
|                                                                                                                                                                                                                      |
| [                           col.Add(c =\> c.Won).HeaderText(\"W\");]                                                                                                |
|                                                                                                                                                                                                                      |
| [                           col.Add(c =\> c.Loss).HeaderText(\"L\");]                                                                                               |
|                                                                                                                                                                                                                      |
| [                           col.Add(c =\> c.Percent).HeaderText(\"PCT\");]                                                                                          |
|                                                                                                                                                                                                                      |
| [                           col.Add(c =\> c.L10).HeaderText(\"L10\");]                                                                                              |
|                                                                                                                                                                                                                      |
| [                       })]                                                                                                                                         |
|                                                                                                                                                                                                                      |
| [                .PageSettings(p =\> p.ShowPager(true).PageSize(12))]                                                                                               |
|                                                                                                                                                                                                                      |
| [                **.QueryCellInfo(cell=\>**]                                                                                                                        |
|                                                                                                                                                                                                                      |
| **[                 {]**                                                                                                                                            |
|                                                                                                                                                                                                                      |
| **[                     if (cell.TableCellType == MobGridTableCellType.RecordFieldCell \|\| cell.TableCellType == MobGridTableCellType.AlternateRecordFieldCell)]** |
|                                                                                                                                                                                                                      |
| **[                     {]**                                                                                                                                        |
|                                                                                                                                                                                                                      |
| **[                         if (cell.Column.MappingName == \"Won\")]**                                                                                              |
|                                                                                                                                                                                                                      |
| **[                         {]**                                                                                                                                    |
|                                                                                                                                                                                                                      |
| **[                             if (cell.Data.Won \>= 12)]**                                                                                                        |
|                                                                                                                                                                                                                      |
| **[                                 cell.HtmlAttributes\[\"style\"\] = \"color:white;background-color:#395b73;\";]**                                                |
|                                                                                                                                                                                                                      |
| **[                         }]**                                                                                                                                    |
|                                                                                                                                                                                                                      |
| **[                         if (cell.Column.MappingName == \"Loss\")]**                                                                                             |
|                                                                                                                                                                                                                      |
| **[                         {]**                                                                                                                                    |
|                                                                                                                                                                                                                      |
| **[                             if (cell.Data.Loss \<= 6)]**                                                                                                        |
|                                                                                                                                                                                                                      |
| **[                                 cell.HtmlAttributes\[\"style\"\] = \"color:#ac0c0c;background-color:Bisque;\";]**                                               |
|                                                                                                                                                                                                                      |
| **[                         }]**                                                                                                                                    |
|                                                                                                                                                                                                                      |
| **[                     }]**                                                                                                                                        |
|                                                                                                                                                                                                                      |
| **[                     })]**[.Render();]                                                                          |
|                                                                                                                                                                                                                      |
| [}][]                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                                |
| [\<%][=][Html.MobSyncfusion().Grid\<Standings\>(\"grid\")] |
|                                                                                                                                                                                                                                                |
| [                                   .Datasource(Model).Caption(\"Admin:36 Items\")]                                                                                                           |
|                                                                                                                                                                                                                                                |
| [           .ActionMode(MobActionMode.Server).EnablePaging()]                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [                       .Column(col =\>]                                                                                                                                                      |
|                                                                                                                                                                                                                                                |
| [                       {]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                |
| [                           col.Add(c =\> c.Team).HeaderText(\"Team\");]                                                                                                                      |
|                                                                                                                                                                                                                                                |
| [                           col.Add(c =\> c.Won).HeaderText(\"W\");]                                                                                                                          |
|                                                                                                                                                                                                                                                |
| [                           col.Add(c =\> c.Loss).HeaderText(\"L\");]                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                           col.Add(c =\> c.Percent).HeaderText(\"PCT\");]                                                                                                                    |
|                                                                                                                                                                                                                                                |
| [                           col.Add(c =\> c.L10).HeaderText(\"L10\");]                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [                       }).PageSettings(p =\> p.ShowPager(true).PageSize(12))]                                                                                                                |
|                                                                                                                                                                                                                                                |
| [             **.QueryCellInfo(cell=\>**]                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| **[                 {]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                                |
| **[                     if (cell.TableCellType == MobGridTableCellType.RecordFieldCell \|\| cell.TableCellType == MobGridTableCellType.AlternateRecordFieldCell)]**                           |
|                                                                                                                                                                                                                                                |
| **[                     {]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| **[                         if (cell.Column.MappingName == \"Won\")]**                                                                                                                        |
|                                                                                                                                                                                                                                                |
| **[                         {]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| **[                             if (cell.Data.Won \>= 12)]**                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| **[                                 cell.HtmlAttributes\[\"style\"\] = \"color:white;background-color:#395b73;\";]**                                                                          |
|                                                                                                                                                                                                                                                |
| **[                         }]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| **[                         if (cell.Column.MappingName == \"Loss\")]**                                                                                                                       |
|                                                                                                                                                                                                                                                |
| **[                         {]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| **[                             if (cell.Data.Loss \<= 6)]**                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| **[                                 cell.HtmlAttributes\[\"style\"\] = \"color:#ac0c0c;background-color:Bisque;\";]**                                                                         |
|                                                                                                                                                                                                                                                |
| **[                         }]**                                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| **[                     }]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| **[                     })]**[     [%\>]][]                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.  Set its data source and render the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [///][ ][\<summary\>]                                                     |
|                                                                                                                                                                                                                               |
| [        [///][ Used to bind the Grid.]]                                                                                                       |
|                                                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                                                          |
|                                                                                                                                                                                                                               |
| [        [///][ ][\<returns\>][View page, it displays the Grid][\</returns\>]] |
|                                                                                                                                                                                                                               |
| [       ][public][ [ActionResult] Index()]         |
|                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                  |
|                                                                                                                                                                                                                               |
| [            [var] data = [StandingsDetails].GetData();]                                                                        |
|                                                                                                                                                                                                                               |
| [            [return] View(data);]                                                                                                                      |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  Create a **QueryCellAction** handler as shown below.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| [\[[ChildActionOnly]\]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [        [public] [void] onQueryCellAction([GridTableCell]\<[Standings]\> cell)]                                                        |
|                                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [            [if] (cell.TableCellType == [MobGridTableCellType].RecordFieldCell \|\| cell.TableCellType == [MobGridTableCellType].AlternateRecordFieldCell)] |
|                                                                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [                [if] (cell.Column.MappingName == [\"Won\"])]                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    [if] (cell.Data.Won \>= 12)]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [                        cell.HtmlAttributes\[[\"style\"]\] = [\"color:white;background-color:#395b73;\"];]                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                [if] (cell.Column.MappingName == [\"Loss\"])]                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    [if] (cell.Data.Loss \<= 6)]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [                        cell.HtmlAttributes\[[\"style\"]\] = [\"color:#ac0c0c;background-color:Bisque;\"];]                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.  In order to work with sorting and paging actions, create a **Post** method for **Index** actions and bind the data source and **QueryCellAction** to the grid as shown in the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [  ///][ ][\<summary\>][]                                                          |
|                                                                                                                                                                                                                                                                            |
| [        [///][ Paging/sorting Requests are mapped to this method. This method invokes the MobHtmlActionResult]]                                                                            |
|                                                                                                                                                                                                                                                                            |
| [        [///][ from the grid. Required response is generated.]]                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [        [///][ ][\</summary\>]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]]                                       |
|                                                                                                                                                                                                                                                                            |
| [        [///][ ][\<returns\>]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [        [///][ MobHtmlActionResult returns the data displayed on the grid.]]                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [        [///][ ][\</returns\>]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [       ][\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [   [public] [ActionResult] Index([MobGridParams] args)]                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [   {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [   [var] data = [StandingsDetails].GetData();]                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [   [var] engine = data.MobGridActions\<[Standings]\>() [as ][MobGridHtmlActionResult]\<[Standings]\>;] |
|                                                                                                                                                                                                                                                                            |
| [            engine.GridModel.QueryCellInfo = onQueryCellAction;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [            [return] engine;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [   }]                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.  Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 60: Grid---QueryCellInfo

[]{#related-topics}


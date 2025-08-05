---
title: throughmobgridpropertiesmodel6.md
original_path: WinForms_Docs/04_Controls/Grid/throughmobgridpropertiesmodel6.md
created_at: 2025-08-05
---






#### Through MobGridPropertiesModel {#through-mobgridpropertiesmodel style="tab-stops: 0pt"}

1.  Create a model in the application (Refer to ).

2.  Add the following code in the **Index.cshtml** file to create the Grid control in the view.

 

**[View \[cshtml\]]**

 [@(][new][ [HtmlString](Html.MobSyncfusion().Grid\<[Standings]\>([\"grid\"], ([MobGridPropertiesModel]\<[Standings]\>)(ViewData\[[\"GridModel\"]\])).ToString())[)]  ]


**[View \[ASPX\]]** []

[   [\<%][=] Html.MobSyncfusion().Grid\<[Standings]\>([\"grid\"], ([MobGridPropertiesModel]\<[Standings]\>)(ViewData\[[\"GridModel\"]\]))]

[%\>][]

 

3.  Create a **MobGridPropertiesModel** object in the **Index** method. Assign grid properties in this model and pass the model from the **controller** to the **view** using the **ViewData** class as shown below:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                           |
| [public][ [ActionResult] Index()]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [            [MobGridPropertiesModel]\<[Standings]\> model = [new] [MobGridPropertiesModel]\<[Standings]\>()]                    |
|                                                                                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                           |
| [                DataSource = [StandingsDetails].GetData(),]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [                Caption = [\"Admin:36 Items\"],]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [                ActionMode= [MobActionMode].Server][]                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [            };]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [            model.Columns.Add([new] [MobGridColumn]\<[Standings]\>() { HeaderText=[\"Team\"], MappingName=[\"Team\"] });]       |
|                                                                                                                                                                                                                                                                                           |
| [            model.Columns.Add([new] [MobGridColumn]\<[Standings]\>() { HeaderText = [\"W\"], MappingName = [\"Won\"] });]       |
|                                                                                                                                                                                                                                                                                           |
| [            model.Columns.Add([new] [MobGridColumn]\<[Standings]\>() { HeaderText = [\"L\"], MappingName = [\"Loss\"] });]      |
|                                                                                                                                                                                                                                                                                           |
| [            model.Columns.Add([new] [MobGridColumn]\<[Standings]\>() { HeaderText = [\"PCT\"], MappingName = [\"Percent\"] });] |
|                                                                                                                                                                                                                                                                                           |
| [            model.Columns.Add([new] [MobGridColumn]\<[Standings]\>() { HeaderText = [\"L10\"], MappingName = [\"L10\"] });]     |
|                                                                                                                                                                                                                                                                                           |
| [            ViewData\[[\"GridModel\"]\] = model; [// pass the model from controller to view using ViewData.]]                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| [                model.QueryCellInfo = onQueryCellAction; ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.  Create a **QueryCellAction** handler as shown below.

 

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

 

5.  In order to work with paging and sorting actions, create a **Post** method for **Index** actions and bind the data source and **QueryCellAction** handler to the grid as shown in the following code.

[  ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
|  [///][ ][\<summary\>][]                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ sorting Requests are mapped to this method. This method invokes the MobHtmlActionResult]]                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ from the grid. Required response is generated.]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains sorting properties. ][\</param\>]]                                               |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ MobHtmlActionResult returns the data displayed on the grid.]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [        [///][ ][\</returns\>]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index([MobGridParams] args)]                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [            [var] data = [StandingsDetails].GetData();]                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            [var] engine = data.MobGridActions\<[Standings]\>() [as] [MobGridHtmlActionResult]\<[Standings]\>;] |
|                                                                                                                                                                                                                                                                                     |
| [            engine.GridModel.QueryCellInfo = onQueryCellAction;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| [            [return] engine;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.  Run the application. The grid will appear as shown below.

 

{border="0"}[]

Figure 61: Grid---QueryCellInfo

[]{#related-topics}

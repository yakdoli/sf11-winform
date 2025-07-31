---
title: throughgridbuilder46.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder46.md
created_at: 2025-07-03
---






##### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

The steps to enable the External From Edit Mode feature through **GridBuilder** are as follows:

1.   Create a model in the application.

2.   Create a strongly typed view. Add the **MicrosoftMvcValidation.debug.js** file in the master page.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][head][ [runat][=\"server\"\>]][]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\<][title][\>\<][asp][:][ContentPlaceHolder] [ID][=\"TitleContent\"] [runat][=\"server\"] [/\>\</][title][\>]][]                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [.........][]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][script][ [src][=\"][\<%][=] Url.Content(\"\~/Scripts/MicrosoftMvcValidation.debug.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]  ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][head][\>][]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   In the view, use the **Model** property in the **Datasource()** to bind the data source.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                  |
| [.Datasource(Model).ActionMode([ActionMode].JSON)]                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [.Caption([\"Orders\"])]                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [ \-\-\-\-\-\-\-\--]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [.Column(column =\>]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                  |
| [column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| [column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);]                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [})]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [\-\-\-\-\-\-\-\-\--]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [%\>]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Razor]**                                                                                                                                              |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\@{][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                              |
| [.Datasource(Model).ActionMode([ActionMode].JSON)]                                                                               |
|                                                                                                                                                                                              |
| [.Caption([\"Orders\"])]                                                                                                         |
|                                                                                                                                                                                              |
| [ \-\-\-\-\-\-\-\-\--]                                                                                                                                   |
|                                                                                                                                                                                              |
| [.Column(column =\>]                                                                                                                                     |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                        |
|                                                                                                                                                                                              |
| [column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                  |
|                                                                                                                                                                                              |
| [column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                |
|                                                                                                                                                                                              |
| [column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);]                                                                    |
|                                                                                                                                                                                              |
| [column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                         |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [})]                                                                                                                                                     |
|                                                                                                                                                                                              |
| [\-\-\-\-\-\-\-\-\--]                                                                                                                                    |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [}]                                                                                                                                  |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

4.   Essential Grid allows adding new records through grid toolbar items.

 

In this example, **AddNew**, **Edit**, **Delete**, **Save**, and **Cancel** buttons have been added in the toolbar items, as displayed below.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [\<%][=Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [       \-\-\-\-\-\--]                                                                                                                                    |
|                                                                                                                                                                                               |
| [.ToolBar(tools =\>]                                                                                                                                      |
|                                                                                                                                                                                               |
| [{]                                                                                                                                                       |
|                                                                                                                                                                                               |
| [  tools.Add([GridToolBarItems].AddNew)[// Toolbar item for inserting records.]]                            |
|                                                                                                                                                                                               |
| [.Add([GridToolBarItems].Edit)[// Toolbar item for editing records.]]                                       |
|                                                                                                                                                                                               |
| [.Add([GridToolBarItems].Delete)[// Toolbar item for deleting records.]]                                    |
|                                                                                                                                                                                               |
| [.Add([GridToolBarItems].Update)[// Toolbar item for saving changes.]]                                      |
|                                                                                                                                                                                               |
| [.Add([GridToolBarItems].Cancel);[// Toolbar item for canceling request.]]                                  |
|                                                                                                                                                                                               |
| [})]                                                                                                                                                      |
|                                                                                                                                                                                               |
| [\-\-\-\-\-\-\-\-\--]                                                                                                                                     |
|                                                                                                                                                                                               |
| [%\>][]                                                                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                          |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\@{][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [       \-\-\-\-\-\--]                                                                                                                                   |
|                                                                                                                                                                                              |
| [.ToolBar(tools =\>]                                                                                                                                     |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [  tools.Add([GridToolBarItems].AddNew)[// Toolbar item for inserting records.]]                           |
|                                                                                                                                                                                              |
| [.Add([GridToolBarItems].Edit)[// Toolbar item for editing records.]]                                      |
|                                                                                                                                                                                              |
| [.Add([GridToolBarItems].Delete)[// Toolbar item for deleting records.]]                                   |
|                                                                                                                                                                                              |
| [.Add([GridToolBarItems].Update)[// Toolbar item for saving changes.]]                                     |
|                                                                                                                                                                                              |
| [.Add([GridToolBarItems].Cancel);[// Toolbar item for canceling request.]]                                 |
|                                                                                                                                                                                              |
| [})]                                                                                                                                                     |
|                                                                                                                                                                                              |
| [\-\-\-\-\-\-\-\-\--]                                                                                                                                    |
|                                                                                                                                                                                              |
| [}][]                                                                                            |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

5.   Enable ExternalForm editing by using the **Editing** property and its sub-properties, as displayed below.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [\<%][=Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| **[       \-\-\-\-\-\--]**                                                                                                                                |
|                                                                                                                                                                                               |
| [.Editing(edit=\>{]                                                                                                                                       |
|                                                                                                                                                                                               |
| [edit.ExternalForm(ef =\>]                                                                                                                                |
|                                                                                                                                                                                               |
| [{]                                                                                                                                                       |
|                                                                                                                                                                                               |
| [ef.TargetID([\"ExternalEditForm\"]);]                                                                                            |
|                                                                                                                                                                                               |
| [                    ef.Position([ExternalFormPosition].TopRight);]                                                               |
|                                                                                                                                                                                               |
| [});]                                                                                                                                                     |
|                                                                                                                                                                                               |
| [// Specify the action method which will perform the update action.][]                                  |
|                                                                                                                                                                                               |
| [edit.AllowEdit([true], [\"OrderSave\"])]                                                                    |
|                                                                                                                                                                                               |
| [// Specify the action method which will perform the insert action.][]                                  |
|                                                                                                                                                                                               |
| [.AllowNew([true], [\"AddOrder\"])]                                                                          |
|                                                                                                                                                                                               |
| [// Specify the action method which will perform the delete action.][]                                  |
|                                                                                                                                                                                               |
| [.AllowDelete([true], [\"DeleteOrder\"]);]                                                                   |
|                                                                                                                                                                                               |
| [//Specify the grid edit mode.][]                                                                       |
|                                                                                                                                                                                               |
| [              edit.EditMode([GridEditMode].ExternalForm);]                                                                       |
|                                                                                                                                                                                               |
| [edit.ExternalModeEditorTemplate([\"OrderEditorTemplate\"]);]                                                                     |
|                                                                                                                                                                                               |
| [// Add primary key to primary key collections][]                                                       |
|                                                                                                                                                                                               |
| [edit.PrimaryKey(key =\> key.Add(p =\> p.OrderID));   ]                                                                                                   |
|                                                                                                                                                                                               |
| [})]                                                                                                                                                      |
|                                                                                                                                                                                               |
| [\-\-\-\-\-\-\--]                                                                                                                                         |
|                                                                                                                                                                                               |
| [%\>][]                                                                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                          |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\@{][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [       \-\-\-\-\-\--]                                                                                                                                   |
|                                                                                                                                                                                              |
| [.Editing(edit=\>{]                                                                                                                                      |
|                                                                                                                                                                                              |
| [edit.ExternalForm(ef =\>]                                                                                                                               |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [ ef.TargetID([\"ExternalEditForm\"]);]                                                                                          |
|                                                                                                                                                                                              |
| [                      ef.Position([ExternalFormPosition].TopRight);]                                                            |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [});]                                                                                                                                                    |
|                                                                                                                                                                                              |
| [// Specify the action method which will perform the update action.][]                                 |
|                                                                                                                                                                                              |
| [edit.AllowEdit([true], [\"OrderSave\"])]                                                                   |
|                                                                                                                                                                                              |
| [// Specify the action method which will perform the insert action.][]                                 |
|                                                                                                                                                                                              |
| [.AllowNew([true], [\"AddOrder\"])]                                                                         |
|                                                                                                                                                                                              |
| [// Specify the action method which will perform the delete action.][]                                 |
|                                                                                                                                                                                              |
| [.AllowDelete([true], [\"DeleteOrder\"]);]                                                                  |
|                                                                                                                                                                                              |
| [// Specify the grid edit mode.][]                                                                     |
|                                                                                                                                                                                              |
| [edit.EditMode([GridEditMode].ExternalForm);]                                                                                    |
|                                                                                                                                                                                              |
| [edit.ExternalModeEditorTemplate([\"OrderEditorTemplate\"]);]                                                                    |
|                                                                                                                                                                                              |
| [// Add primary key to primary key collections.][]                                                     |
|                                                                                                                                                                                              |
| [edit.PrimaryKey(key =\> key.Add(p =\> p.OrderID));   ]                                                                                                  |
|                                                                                                                                                                                              |
| [})]                                                                                                                                                     |
|                                                                                                                                                                                              |
| [\-\-\-\-\-\-\--]                                                                                                                                        |
|                                                                                                                                                                                              |
| [}][]                                                                                            |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [///][ Used for rendering the grid initially.][]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [///][ ][\</summary\>][]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>][] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [public][ [ActionResult] ExternalFormEdit()]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [      return][ View([OrderRepository].GetAllRecords());]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [public][ [ActionResult] ExternalFormEdit([PagingParams] args, [int]? OrderID, [GridEditMode]? GridMode)]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [RequestType][ currentRequest = ([RequestType])[Convert].ToInt32(args.RequestType);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [if][ (currentRequest == [RequestType].BeginEdit && GridMode == [GridEditMode].ExternalFormTemplate)]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [EditableOrder][ ord = ([EditableOrder])[OrderRepository].Select(OrderID);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [return][ PartialView([\"OrderEditorTemplate\"], ord);]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [else][ [if] (currentRequest == [RequestType].BeginAddNew && GridMode == [GridEditMode].ExternalFormTemplate)]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [return][ PartialView([\"OrderEditorTemplate\"], [new] [EditableOrder]());]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [else][]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [IEnumerable][ data = [OrderRepository].GetAllRecords();]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [return][ data.GridActions\<[EditableOrder]\>();]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}


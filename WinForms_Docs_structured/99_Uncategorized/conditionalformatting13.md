---
title: conditionalformatting13.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\conditionalformatting13.md
created_at: 2025-07-03
---








  









### Conditional Formatting {#conditional-formatting style="tab-stops: 0pt"}

This feature is used to format grid content based on some condition specified by the user.

1.  Create a model in the application (Refer to ).

2.  Add the following code in the **Index.cshtml** file to create the Grid control in the view.

 

**[View \[cshtml\]]**

 [@][{]

[Html.MobSyncfusion().Grid\<Order\>(\"grid\")]

[           .Datasource(Model).Caption(\"Orders\")]

[           .ActionMode(MobActionMode.Server).EnablePaging()]

[           .Column(col =\>]

[           {]

[               col.Add(c =\> c.OrderID).HeaderText(\"ID\");]

[               col.Add(c =\> c.CustomerID).HeaderText(\"CustomerID\");]

[               col.Add(c =\> c.Freight).HeaderText(\"Freight\").Format(\"{0:C}\");]

[               col.Add(c =\> c.ShipCountry).HeaderText(\"Country\");]

[           }).PageSettings(p =\> p.ShowPager(true)).Render();]

[}][  ][]


**[View \[ASPX\]]** \
\
[]

[   [\<%][=] ][Html.MobSyncfusion().Grid\<Order\>(\"grid\")]

[           .Datasource(Model).Caption(\"Orders\")]

[           .ActionMode(MobActionMode.Server).EnablePaging()]

[           .Column(col =\>]

[           {]

[               col.Add(c =\> c.OrderID).HeaderText(\"ID\");]

[               col.Add(c =\> c.CustomerID).HeaderText(\"CustomerID\");]

[               col.Add(c =\> c.Freight).HeaderText(\"Freight\").Format(\"{0:C}\");]

[               col.Add(c =\> c.ShipCountry).HeaderText(\"Country\");]

[           }).PageSettings(p =\> p.ShowPager(true))]

[] 

[%\>][]

 

3.  Create a **MobGridPropertiesModel** object in the **Index** method. Assign grid properties in this model and pass the model from the **controller** to the **view** using the **ViewData** class as shown below:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [public][ [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [             ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(120).ToList();]                                                                      |
|                                                                                                                                                                                                                                                                              |
| [            [MobGridPropertiesModel]\<[Order]\> model = [new] [MobGridPropertiesModel]\<[Order]\>();] |
|                                                                                                                                                                                                                                                                              |
| [            model.ConditionalFormats = [this].ConditionFormats;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"grid\"]\] = model;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [            [return] View(data);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.  Create the conditional format handler as below.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        [private] [Collection]\<[MobGridConditionalFormatDescriptor]\<[Order]\>\> ConditionFormats]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            [get]]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [MobGridDataCondition]\<[Order]\> condition1 = [new] [MobGridDataCondition]\<[Order]\>(c =\> c.Freight) { ConditionType = [MobGridDataConditionType].GreaterThan, Value = 30 };]                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [MobGridDataCondition]\<[Order]\> condition2 = [new] [MobGridDataCondition]\<[Order]\>(c =\> c.CustomerID) { ConditionType = [MobGridDataConditionType].Equals, Value = [\"BERGS\"] };] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [MobGridConditionalFormatDescriptor]\<[Order]\> cFormat = [new] [MobGridConditionalFormatDescriptor]\<[Order]\>();]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                cFormat.Name = [\"c4\"];]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                cFormat.ApplyStyleToColumn = [\"ShipCountry\"];]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                cFormat.Conditions.Add(condition1);]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [// cFormat.Conditions.Add(condition2);]]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                cFormat.Cell.HtmlAttributes\[[\"style\"]\] = [\"background-color: Bisque;Color:#ac0c0c;\"];]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [MobGridDataCondition]\<[Order]\> condition3 = [new] [MobGridDataCondition]\<[Order]\>(c =\> c.Freight) { ConditionType = [MobGridDataConditionType].LessThan, Value = 15 };]                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [MobGridConditionalFormatDescriptor]\<[Order]\> rowFormat = [new] [MobGridConditionalFormatDescriptor]\<[Order]\>();]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                rowFormat.Name = [\"condition1\"];]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                rowFormat.Conditions.Add(condition3);]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                rowFormat.Cell.HtmlAttributes\[[\"style\"]\] = [\"background-color: #395b73;color:white;\"];]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [Collection]\<[MobGridConditionalFormatDescriptor]\<[Order]\>\> cf = [new] [Collection]\<[MobGridConditionalFormatDescriptor]\<[Order]\>\>();]                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                cf.Add(cFormat);]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                cf.Add(rowFormat);]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                [return] cf;]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  In order to work with paging/sorting actions, create a **Post** method for **Index** actions and bind the data source and the conditional format handler to the grid as shown in the following code.

 

[  ]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [][]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [        [public] [ActionResult] Index([MobGridParams] args)]                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(120).ToList();]                                                                     |
|                                                                                                                                                                                                                                                                             |
| [            [var] engine = data.MobGridActions\<[Order]\>() [as] [MobGridHtmlActionResult]\<[Order]\>;] |
|                                                                                                                                                                                                                                                                             |
| [            engine.GridModel.ConditionalFormats = ConditionFormats;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [            [return] engine;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.  Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 62: Grid---Conditional Formatting

 

[]{#related-topics}

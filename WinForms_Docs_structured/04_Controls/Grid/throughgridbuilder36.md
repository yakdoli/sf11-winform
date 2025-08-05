---
title: throughgridbuilder36.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder36.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

To enable the localization feature using **GridBuilder**:

 

1.   Create a model in the application (Refer [[to ]]{.UGHyperlink}[Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink}[[)]]{.UGHyperlink}.

3.   Create a folder named **App_GlobalResources** in the application and create your own localization resource (.resx) file in this folder.

 

{border="0"}

Figure 264: App_GlobalResource Folder

**[]** 

**[]** 

In order to create a new localization resource file, download the default localization file from the following location, rename it, and then use Visual Studio to edit the values.

[] 

[[GridResource.zip]{.UGHyperlink}](http://help.syncfusion.com/support/grid_mvc/v8.3.0.20/UG/GridResource.zip)[]{.UGHyperlink}

[] 

The default English localization file is shown in the following screenshot:

 

{border="0"}

Figure 265: Resource File For English Localization

**[]** 

***[]*** 


{border="0"}Note: The name of the localization file should be in the format GridResource.\[culture\].resx. For example: \"GridLocalization.fr-FR.resx\"


[] 

1.   Create the Grid control in the view and configure its properties.

2.   There are two ways to specify the culture information, namely:

[] 

[·      ]Setting the **CurrentUICulture** property of the **CurrentThread** inside your **Action** method:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| [   [public] [ActionResult] Index()\                                                                                                                                                                                |
|    {\                                                                                                                                                                                                                                                            |
|              System.Threading.[Thread].CurrentThread.CurrentUICulture = [new] System.Globalization.[CultureInfo]([\"fr-FR\"]);] |
|                                                                                                                                                                                                                                                                  |
| [        [var] data = [new] [NorthwindDataContext]().Orders;\                                                                                                                                  |
|         [return] View(data);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Specifying the culture using the **Localize()** method:

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [ ][\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
|        .Datasource(Model)\                                                                                                                                                                                                                          |
|        .Caption([\"Orders\"])\                                                                                                                                                                                              |
|        .EnablePaging()\                                                                                                                                                                                                                             |
|        .EnableSorting()\                                                                                                                                                                                                                            |
|        .EnableFiltering()\                                                                                                                                                                                                                          |
|        .AutoFormat([Skins].Sandune)  \                                                                                                                                                                                      |
|        **.Localize([\"fr-FR\"])**[// Specify the culture code.    ]\                                                                                                                                  |
|        .Column( columns =\> {\                                                                                                                                                                                                                      |
|            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);\                                                                                                                                                        |
|            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                                                                  |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           \                                                                                                                                       |
|            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                                                                                                                |
|            columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                               |
|            })\                                                                                                                                                                                                                                      |
|        [%\>]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [ ][\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
|        .Datasource(Model)\                                                                                                                                                                                                                          |
|        .Caption([\"Orders\"])\                                                                                                                                                                                              |
|        .EnablePaging()\                                                                                                                                                                                                                             |
|        .EnableSorting()\                                                                                                                                                                                                                            |
|        .EnableFiltering()\                                                                                                                                                                                                                          |
|        .AutoFormat([Skins].Sandune)  \                                                                                                                                                                                      |
|        **.Localize([\"fr-FR\"])**[// Specify the culture code.    ]\                                                                                                                                  |
|        .Column( columns =\> {\                                                                                                                                                                                                                      |
|            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);\                                                                                                                                                        |
|            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                                                                  |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           \                                                                                                                                       |
|            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                                                                                                                |
|            columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                               |
|            }).Render();]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [       [}]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

3.   Set its data source and render the **View**.

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [        ][///][ ][\<summary\>][\ |
|         [///][ Used for rendering the grid initially.]\                                                                                                                                |
|         [///][ ][\</summary\>]\                                                                                                                                   |
|         [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]\                                         |
|         [public] [ActionResult] Index()\                                                                                                                                             |
|         {\                                                                                                                                                                                                                        |
|             [var] data = [new] [NorthwindDataContext]().Orders;\                                                                                                |
|             [return] View(data);\                                                                                                                                                                            |
|         }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| [   ]                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

4.   Run the application. The grid will appear as shown below:

[] 

{border="0"}

Figure 266: Grid With French Localization

 

Customization

 

If you want to customize the localization resource file folder path, then use the **LocalizationPath() ** method.

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [ ][\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
|        .Datasource(Model)\                                                                                                                                                                                                                          |
|        .Caption([\"Orders\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [       .Localize([\"fr-FR\"])[// Specify the culture code.  ]]                                                                                                   |
|                                                                                                                                                                                                                                                     |
| **[       ][.LocalizationPath([\"\~/App_LocalResources\"]) [// Specify the folder. ]]**                                            |
|                                                                                                                                                                                                                                                     |
| [       [%\>]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[   ]

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [ ][\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
|        .Datasource(Model)\                                                                                                                                                                                                                          |
|        .Caption([\"Orders\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [       .Localize([\"fr-FR\"])[// Specify the culture code.  ]]                                                                                                   |
|                                                                                                                                                                                                                                                     |
| **[        ][.LocalizationPath([\"\~/App_LocalResources\"]) [// Specify the folder. ]]**                                           |
|                                                                                                                                                                                                                                                     |
| [       .Render();        []]                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [}][]                                                                                                                                                   |
|                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[   ][]

[] 

[]{#related-topics}


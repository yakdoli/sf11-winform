---
title: throughgridbuilder35.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder35.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

In order to work with this feature please follow the steps below:

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view create the Grid control and configure its properties.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                [%\>]]                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml[\]]]**                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                .Render();]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [                [}]]                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Refer to the base CSS in [[Grid Built-in Skin]]{.underline}. Change this base class name and customize the skins as per your own styles. The CSS class structure should not be broken. All the subclass names should be the same as base styles. In this case you have to change the "Almond" skin to the "Greenish" skin (Refer to How to\>Grid Custom Skin\>CSS).

[] 

5.   Refer to the sprite image in the Sprite Image section. Generate your new image as per the same alignment and position as the images in the CSS class properly. In this case you have genereated a new sprite image for "Greenish" skins.

 

6.   Add the new custom CSS and sprite image in the application and add this custom CSS in the master page as demonstrated below:

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Site.Master\]]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\<][title][\>\<][asp][:][ContentPlaceHolder] [ID][=\"TitleContent\"] [runat][=\"server\"] [/\>\</][title][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            **[\<][link] [href][=\"][\<%][=] Url.Content(\"\~/Content/CustomCss/Syncfusion-Grid-Greenish.css\")[%\>][\"] [rel][=\"stylesheet\"]**]                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[        [type][=\"text/css\"] [/\>]]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ...............]                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ...............]                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][head][\>][]                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[\_Layout.cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    [\<][title][\>\<][asp][:][ContentPlaceHolder] [ID][=\"TitleContent\"] [runat][=\"server\"] [/\>\</][title][\>]]       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            **[\<][link] [href][=\"][@]Url.Content(\"\~/Content/CustomCss/Syncfusion-Grid-Greenish.css\")[\"] [rel][=\"stylesheet\"] [type][=\"text/css\"] [/\>]**] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ...............]                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ...............]                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][head][\>][]                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.   Specify the custom CSS class name using the **CustomCss()** method. In this case "**Syncfusion-Grid-Greenish**" is the custom CSS class name.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [        **                **]**[.CustomCss([\"Syncfusion-Grid-Greenish\"])]**                                                             |
|                                                                                                                                                                                                                                                            |
| [         [%\>]]                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\][]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [        **              **]**[.CustomCss([\"Syncfusion-Grid-Greenish\"])]**                                                               |
|                                                                                                                                                                                                                                                            |
| [                      .Render();]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [         [}]]                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 261: Grid with Custom Skin---Greenish

 

[]{#related-topics}


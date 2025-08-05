---
title: filtercustomization2.md
original_path: WinForms_Docs/99_Uncategorized/filtercustomization2.md
created_at: 2025-08-05
---






##### Filter Customization {#filter-customization style="tab-stops: 0pt"}

 

[·      ]To enable or disable filtering based on some condition, use the **AllowFiltering(bool)** method.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [ ][\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **      ** .ActionMode(ActionMode.JSON)\                                                                                                                                                                                                                                  |
|        .Caption([\"Orders\"])\                                                                                                                                                                                                                    |
|        .EnablePaging()\                                                                                                                                                                                                                                                   |
|        .EnableSorting()\                                                                                                                                                                                                                                                  |
| **       **.Filtering(filter =\>\                                                                                                                                                                                                                                         |
|            {\                                                                                                                                                                                                                                                             |
|                **filter.AllowFiltering([true]);\**                                                                                                                                                                                                   |
|            })]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [       [%\>]][]                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml\]]**[]                                                                                                                         |
|                                                                                                                                                                                                                                                                           |
| [ ][\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **      ** .ActionMode(ActionMode.JSON)\                                                                                                                                                                                                                                  |
|        .Caption([\"Orders\"])\                                                                                                                                                                                                                    |
|        .EnablePaging()\                                                                                                                                                                                                                                                   |
|        .EnableSorting()\                                                                                                                                                                                                                                                  |
| **       **.Filtering(filter =\>\                                                                                                                                                                                                                                         |
|            {\                                                                                                                                                                                                                                                             |
|                **filter.AllowFiltering([true]);\**                                                                                                                                                                                                   |
|            }).Render();[}]][]                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ][T]o enable or disable filter options for individual columns, use the **AllowFilter(bool)** method in column mapping.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                                  |
|                                                                                                                                                                                                            |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
|         .ActionMode(ActionMode.JSON)\                                                                                                                                                                      |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnableFiltering()\                                                                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                                                                         |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).**AllowFilter**([false]);\                                                                     |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            })\                                                                                                                                                                                             |
|        [%\>]][]                                                                            |
|                                                                                                                                                                                                            |
| []                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml\]]**[]                                                          |
|                                                                                                                                                                                                            |
| [ [\@{][ ]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
|         .ActionMode(ActionMode.JSON)\                                                                                                                                                                      |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnableFiltering()\                                                                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                                                                         |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).**AllowFilter**([false]);\                                                                     |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            }).Render();]                                                                                                                                               |
|                                                                                                                                                                                                            |
| [       [}]][]                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]To render the filter menu in a simple drop-down list, use the **FilterDropDownType()** method.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [ ][\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| \                                                                                                                                                                                                                                                                         |
|        .Caption([\"Orders\"])\                                                                                                                                                                                                                    |
|        .Filtering(filter =\>\                                                                                                                                                                                                                                             |
|            {\                                                                                                                                                                                                                                                             |
|                **filter.FilterDropDownType([FilterDropDownType].SimpleList);**\                                                                                                                                                                   |
|            })][]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [       [%\>]][]                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml\]]**[]                                                                 |
|                                                                                                                                                                                                                   |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| \                                                                                                                                                                                                                 |
|        .Caption([\"Orders\"])\                                                                                                                                                            |
|        .Filtering(filter =\>\                                                                                                                                                                                     |
|            {\                                                                                                                                                                                                     |
|                **filter.FilterDropDownType([FilterDropDownType].SimpleList);**\                                                                                                           |
|            }).Render();][]                                                                                                    |
|                                                                                                                                                                                                                   |
| [       [}]][]                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]Use the **Filtering()** method to add initial filters.

[] 

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                                  |
|                                                                                                                                                                                                            |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
|         .ActionMode(ActionMode.JSON)\                                                                                                                                                                      |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnablePaging()\                                                                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                                                                   |
| **       .Filtering(filter =\>\                                                                                                                                                                            |
|            {\                                                                                                                                                                                              |
|       filter.FilterDescriptors(descriptor =\>\                                                                                                                                                             |
|         {\                                                                                                                                                                                                 |
|         descriptor.Add(c =\> c.EmployeeID).FilterBy([FilterType].Equals).FilterValue(5);\                                                                                          |
|         });\                                                                                                                                                                                               |
|            })**][]                                                                                                     |
|                                                                                                                                                                                                            |
| [       .AutoFormat([Skins].Sandune)      \                                                                                                                                        |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                         |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            })\                                                                                                                                                                                             |
|        [%\>]][]                                                                            |
|                                                                                                                                                                                                            |
| []                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml\]]**[]                                                          |
|                                                                                                                                                                                                            |
| [ [\@{][ ]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
|         .ActionMode(ActionMode.JSON)\                                                                                                                                                                      |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnablePaging()\                                                                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                                                                   |
| **       .Filtering(filter =\>\                                                                                                                                                                            |
|            {\                                                                                                                                                                                              |
|       filter.FilterDescriptors(descriptor =\>\                                                                                                                                                             |
|         {\                                                                                                                                                                                                 |
|         descriptor.Add(c =\> c.EmployeeID).FilterBy([FilterType].Equals).FilterValue(5);\                                                                                          |
|         });\                                                                                                                                                                                               |
|            })**][]                                                                                                     |
|                                                                                                                                                                                                            |
| [       .AutoFormat([Skins].Sandune)      \                                                                                                                                        |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                         |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            }).Render();]                                                                                                                                               |
|                                                                                                                                                                                                            |
| [       [}]][]                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

[]{#related-topics}


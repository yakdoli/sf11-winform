---
title: featuresofpagingsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresofpagingsupport.md
created_at: 2025-07-03
---






##### Features of Paging Support {#features-of-paging-support style="tab-stops: 0pt"}

OnDemandPaging

The GridDataControl supports paging on demand by specifying queries in order to get the paged records from a database. The records are displayed only when it is required. This sample retrieves fifty records from a database and displays them. By this type we can fetch the data from the data source for the current page. No need to fetch whole data from the datasource. We can get high performance for millions of records.

 

Xaml

+------------------------------------------------------------------------------------+
| ```                                                   |
|    <sync:DataPagerExt x:Name="dataPager" Grid.Row="1" HorizontalAlignment="Center" |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  Width="720"  VerticalAlignment="Top" DisplayMode="FirstLastPreviousNextNumeric"   |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  AutoEllipsis="True"  PageSize="40"                                                |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|                       >                                                            |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  </sync:DataPagerExt>                                                              |
| ```                                                                                |
|                                                                                    |
| []                                             |
|                                                                                    |
| []                                             |
+------------------------------------------------------------------------------------+

 

C#

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [            pager.PageCount = 400;]                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            pager.IsPagingOnDemand = ][true][;]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            pager.OnDemandDataSourceLoad += ][new][ ][GridDataOnDemandPageLoadingEventHandler][(pager_OnDemandDataSourceLoad);]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ]                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ][void][ pager_OnDemandDataSourceLoad(][object][ sender, ][GridDataOnDemandPageLoadingEventArgs][ e)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][this][.grid.ItemsSource = Get_Data(e.PagedRows, e.PagedRows + e.MaximumRows);]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

ViewLevelPaging

ViewLevel Sorting, grouping and filtering is provided.

Xaml

+------------------------------------------------------------------------------------+
| ```                                                   |
|    <sync:DataPagerExt x:Name="dataPager" Grid.Row="1" HorizontalAlignment="Center" |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  Width="720"  VerticalAlignment="Top" DisplayMode="FirstLastPreviousNextNumeric"   |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  AutoEllipsis="True"  PageSize="40"                                                |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|                       >                                                            |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  </sync:DataPagerExt>                                                              |
| ```                                                                                |
|                                                                                    |
| []                                             |
|                                                                                    |
| []                                             |
+------------------------------------------------------------------------------------+

 

C#

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| [                            [var] item = [new] NorthwindOrders(1000);] |
|                                                                                                                                                       |
| [            [var] itemlist = [new] PagedCollectionView(item);]         |
|                                                                                                                                                       |
| [            pager.Source = itemlist;]                                                                            |
|                                                                                                                                                       |
| [            grid.ItemsSource = itemlist;]                                                                        |
|                                                                                                                                                       |
| [            grid.EnablePaging = [true];]                                                    |
|                                                                                                                                                       |
| [            grid.IsViewLevelPaging = [true];][]         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

 

SourceLevelPaging

Sorting, grouping and filtering are provided at the Source level.

Xaml

+------------------------------------------------------------------------------------+
| ```                                                   |
|    <sync:DataPagerExt x:Name="dataPager" Grid.Row="1" HorizontalAlignment="Center" |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  Width="720"  VerticalAlignment="Top" DisplayMode="FirstLastPreviousNextNumeric"   |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  AutoEllipsis="True"  PageSize="40"                                                |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|                       >                                                            |
| ```                                                                                |
|                                                                                    |
| ```                                                   |
|  </sync:DataPagerExt>                                                              |
| ```                                                                                |
|                                                                                    |
| []                                             |
|                                                                                    |
| []                                             |
+------------------------------------------------------------------------------------+

 

C#

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [            var][ item = [new] NorthwindOrders(1000);] |
|                                                                                                                                                                   |
| [            [var] itemlist = [new] PagedCollectionView(item);]                     |
|                                                                                                                                                                   |
| [            pager.Source = itemlist;]                                                                                        |
|                                                                                                                                                                   |
| [            grid.ItemsSource = itemlist;]                                                                                    |
|                                                                                                                                                                   |
| [            grid.EnablePaging = [true];]                                                                |
|                                                                                                                                                                   |
| [            grid.IsViewLevelPaging = [false];][]                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}


---
title: collectionviewsourcedatasource.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\collectionviewsourcedatasource.md
created_at: 2025-07-03
---






##### CollectionViewSource Data Source {#collectionviewsource-data-source style="tab-stops: 0pt"}

You can bind **CollectionViewSource** as a Chart Series Data Source to Chart. Chart listens to the changes in the source and gets updated automatically. The following code illustrates how to bind CollectionViewSource as data source to Chart.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][Window.Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][local][:][SalesinLocation][ x][:][Key][=\"saleslocation\"/\>]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][CollectionViewSource][ Source][=\"{][StaticResource][ saleslocation][}\"][ x][:][Key][=\"cvs\"][ [ \>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][CollectionViewSource.SortDescriptions][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][scm][:][SortDescription][ PropertyName][=\"LocationID\" /\>]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][CollectionViewSource.SortDescriptions][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][CollectionViewSource][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][Window.Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][sfchart:Chart][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][sfchart:ChartArea][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][sfchart][:][ChartSeries][ [ Name][=\"series1\"][ Label][=\"Sales\"][ Type][=\"Column\"] [DataSource][=\"{][Binding][ Source][={][StaticResource][ cvs][}}\"]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [BindingPathX][=\"LocationName\"][ BindingPathsY][=\"Sales\"/\>][  ]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][sfchart:ChartArea][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][sfchart:Chart][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                  |
|                                                                                                                                                                                                           |
| [// Namespace to be included for INotifyPropertyChanged interface.]                                                                                     |
|                                                                                                                                                                                                           |
| [using][ System.ComponentModel;]                                                                                     |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [// Namespace to be included for ObservableCollection.]                                                                                                 |
|                                                                                                                                                                                                           |
| [using][ System.Collections.ObjectModel;]                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [public][ [class] [Production] : INotifyPropertyChanged]                |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [    [private] [double] prodid;]                                                                                            |
|                                                                                                                                                                                                           |
| [    [private] [string] locationname;]                                                                                      |
|                                                                                                                                                                                                           |
| [    [private] [double] sales;]                                                                                             |
|                                                                                                                                                                                                           |
| [    [public] [event] PropertyChangedEventHandler PropertyChanged;]                                                         |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] Production()]                                                                                                                      |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] Production([double] prodid, [string] locationname, [double] sales)] |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [this].prodid = prodid;]                                                                                                                |
|                                                                                                                                                                                                           |
| [        [this].locationname = locationname;]                                                                                                    |
|                                                                                                                                                                                                           |
| [        [this].sales = sales;]                                                                                                                  |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] [override] [string] ToString()]                                                          |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [return] locationname.ToString();]                                                                                                      |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] [double] LocationID]                                                                                          |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [get] { [return] prodid; }]                                                                                        |
|                                                                                                                                                                                                           |
| [        [set]]                                                                                                                                  |
|                                                                                                                                                                                                           |
| [        {]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [            prodid = [value];]                                                                                                                  |
|                                                                                                                                                                                                           |
| [            OnPropertyChanged([\"ProdId\"]);]                                                                                                |
|                                                                                                                                                                                                           |
| [        }]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] [string] LocationName]                                                                                        |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [get] { [return] locationname; }]                                                                                  |
|                                                                                                                                                                                                           |
| [        [set]]                                                                                                                                  |
|                                                                                                                                                                                                           |
| [        {]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [            locationname = [value];]                                                                                                            |
|                                                                                                                                                                                                           |
| [            OnPropertyChanged([\"LocationName\"]);]                                                                                          |
|                                                                                                                                                                                                           |
| [        }]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] [double] Sales]                                                                                               |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [get] { [return] sales; }]                                                                                         |
|                                                                                                                                                                                                           |
| [        [set]]                                                                                                                                  |
|                                                                                                                                                                                                           |
| [        {]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [            sales = [value];]                                                                                                                   |
|                                                                                                                                                                                                           |
| [            OnPropertyChanged([\"Sales\"]);]                                                                                                 |
|                                                                                                                                                                                                           |
| [        }]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [protected] [void] OnPropertyChanged([string] info)]                                              |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        PropertyChangedEventHandler handler = PropertyChanged;]                                                                                                      |
|                                                                                                                                                                                                           |
| [        [if] (handler != [null])]                                                                                          |
|                                                                                                                                                                                                           |
| [        {]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [            handler([this], [new] PropertyChangedEventArgs(info));]                                                        |
|                                                                                                                                                                                                           |
| [        }]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [}]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [class][ [SalesinLocation] : ObservableCollection\<[Production]\>]   |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [    [public] SalesinLocation() : [base]()]                                                                                 |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [Random] rand = [new] [Random]([DateTime].Now.Millisecond);]    |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](101, [\"UK\"], 9));]                                             |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](102, [\"Germany\"], 3));]                                        |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](103, [\"USA\"], 40));]                                           |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](104, [\"Japan\"], 15));]                                         |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](105, [\"China\"], 7));            ]                              |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](106, [\"India\"], 10));            ]                             |
|                                                                                                                                                                                                           |
| [        Add([new] [Production](107, [\"France\"], 10));]                                        |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [}]                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates how a Chart Series is associated to the Chart by using CollectionViewSource data source.

[] 

{border="0"}

Figure 58: Chart Series bound to CollectionViewSource Data Source

 

See Also

[ ]{.UGHyperlink}

[]{.UGHyperlink}

[ ]{.UGHyperlink}

[ ]{.UGHyperlink}

[ ]{.UGHyperlink}

[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#p29} 

 

[]{#related-topics}


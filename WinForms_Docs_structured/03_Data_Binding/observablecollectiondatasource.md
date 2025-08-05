---
title: observablecollectiondatasource.md
original_path: WinForms_Docs/03_Data_Binding/observablecollectiondatasource.md
created_at: 2025-08-05
---






##### ObservableCollection Data Source {#observablecollection-data-source style="tab-stops: 0pt"}

Essential Chart provides support to bind data to an **ObservableCollection** or **INotifyCollectionChanged** collection. Also, the chart automatically gets updated when any changes are made to the data source.

 

The following code illustrates how to bind an ObservableCollection as data source to Chart.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][Window.Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [  \<][local:Sports][ ][x:Key][=][\"[sportinterest]\"[/\>]]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][Window.Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][sfchart:ChartSeries][ ][DataSource][=][\"[{StaticResource sportinterest}]\"[ ][Type][=]\"[Column]\" [BindingPathX][=]\"[SportName]\"[ ][BindingPathsY][=]\"[Interest]\"[/\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [// Namespace to be included for INotifyPropertyChanged interface.]                                                                                                       |
|                                                                                                                                                                                                                             |
| [using][ System.ComponentModel;]                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Namespace to be included for ObservableCollection.]                                                                                                                   |
|                                                                                                                                                                                                                             |
| [using][ System.Collections.ObjectModel;]                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [class] [Sport] : INotifyPropertyChanged]                                       |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [private][ [int] sportid;]                                                                                        |
|                                                                                                                                                                                                                             |
| [private][ [string] sportname;]                                                                                   |
|                                                                                                                                                                                                                             |
| [private][ [double] interest;]                                                                                    |
|                                                                                                                                                                                                                             |
| [public][ [event] PropertyChangedEventHandler PropertyChanged;]                                                   |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ Sport()]                                                                                                                     |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ Sport([int] sportid, [string] sportname, [double] interests)] |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [this][.sportid = sportid;]                                                                                                            |
|                                                                                                                                                                                                                             |
| [this][.sportname = sportname;]                                                                                                        |
|                                                                                                                                                                                                                             |
| [this][.interest = interests;]                                                                                                         |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [override] [string] ToString()]                                                    |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [return][ sportname.ToString();]                                                                                                       |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [int] SportID]                                                                                          |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [get][ { [return] sportid; }]                                                                                     |
|                                                                                                                                                                                                                             |
| [set]                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [sportid = [value];]                                                                                                                                               |
|                                                                                                                                                                                                                             |
| [OnPropertyChanged([\"SportID\"]);]                                                                                                                             |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [string] SportName]                                                                                     |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [get][ { [return] sportname; }]                                                                                   |
|                                                                                                                                                                                                                             |
| [set]                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [sportname = [value];]                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [OnPropertyChanged([\"SportName\"]);]                                                                                                                           |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [double] Interest]                                                                                      |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [get][ { [return] interest; }]                                                                                    |
|                                                                                                                                                                                                                             |
| [set]                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [interest = [value];]                                                                                                                                              |
|                                                                                                                                                                                                                             |
| [OnPropertyChanged([\"Interest\"]);]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [protected][ [void] OnPropertyChanged([string] info)]                                        |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [PropertyChangedEventHandler handler = PropertyChanged;]                                                                                                                                |
|                                                                                                                                                                                                                             |
| [if][ (handler != [null])]                                                                                        |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [handler([this], [new] PropertyChangedEventArgs(info));]                                                                                      |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [public][ [class] [Sports] : ObservableCollection\<[Sport]\>]     |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [public][ Sports() : [base]()]                                                                                    |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](101, [\"Golf\"], 9));]                                                                          |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](102, [\"Soccer\"], 40));]                                                                       |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](103, [\"Hockey\"], 10));]                                                                       |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](104, [\"Rugby\"], 7));]                                                                         |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](105, [\"Shuttle\"], 3));]                                                                       |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](106, [\"Cricket\"], 15));]                                                                      |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](107, [\"Baseball\"], 6));]                                                                      |
|                                                                                                                                                                                                                             |
| [Add([new] [Sport](108, [\"Tennis\"], 10));]                                                                       |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [}  ]                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates how a Chart Series is associated to the Chart by using ObservableCollection data source.

[] 

{border="0"}

Figure 57: ChartSeries bound to ObservableCollection Data Source

[] 

See Also

[[]]{.underline}

[ ]{.UGHyperlink}

[ ]{.UGHyperlink}

[ ]{.UGHyperlink}

[]{.UGHyperlink}

[ ]{.UGHyperlink}

 

[]{#p28} 

 

[]{#related-topics}


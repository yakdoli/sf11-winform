---
title: usinglinqresultsasdatasourcedatabinding.md
original_path: WinForms_Docs/03_Data_Binding/usinglinqresultsasdatasourcedatabinding.md
created_at: 2025-08-05
---








  









### Using LINQ results as Data Source Data Binding {#using-linq-results-as-data-source-data-binding style="tab-stops: 0pt"}

[] 

LINQ results can be directly assigned to the Data Source property for a Chart Series.

[] 

The following lines of code describe how to assign LINQ result to the Data Source property of a Chart Series.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [private][ [IList]\<[Car]\> CreateDataToSeries()]                                                                            |
|                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      IList][\<[Car]\> carlist = [new] [List]\<[Car]\>();]                  |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car A\"], 36700, 200, 28));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car B\"], 23970, 170, 23));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car C\"], 34675, 160, 22));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car D\"], 44950, 180, 36));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car E\"], 74950, 150, 18));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car F\"], 37300, 190, 25));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car G\"], 40765, 200, 26));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car H\"], 23799, 150, 22));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car I\"], 49400, 160, 29));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      carlist.Add([new] [Car]([\"Car J\"], 25149, 200, 22));]                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      return][ carlist;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [private][ [void] BindSource()]                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      IList][\<[Car]\> data = CreateDataToSeries().Where(s =\> s.Price \> 35000).ToList(); ]                                                     |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].Series\[0\].DataSource = data;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].Series\[0\].BindingPathX = [\"Name\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].Series\[0\].BindingPathsY = [new] [List]\<[string]\>() { [\"Price\"] };]                                  |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].PrimaryAxis.LabelsSource = data;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].PrimaryAxis.ContentPath = [\"Name\"];]                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].PrimaryAxis.PositionPath = [\"Name\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [      MyChart.Areas\[0\].LoadArea();]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [public][ [class] [Car]]                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [      public][ [string] Name]                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [      {]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [            get][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [            set][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [      }]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [      public][ [double] Price]                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [      {]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [            get][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [            set][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [      }]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [      public][ [double] MaximumSpeed]                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [      {]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [            get][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [            set][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [      }]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [      public][ [double] Mileage]                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| [      {]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [            get][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [            set][;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [      }]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [      public][ Car([string] name, [double] price, [double] maxspeed, [double] mileage)] |
|                                                                                                                                                                                                                                                                   |
| [      {]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [            this][.Name = name;]                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [            this][.Price = price;]                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [            this][.MaximumSpeed = maxspeed;]                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [            this][.Mileage = mileage;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| [      }]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image illustrates the Chart with series associated by using LINQ results.

[] 

{border="0"}

Figure 14: LINQ results Data Binding

[]{#related-topics}


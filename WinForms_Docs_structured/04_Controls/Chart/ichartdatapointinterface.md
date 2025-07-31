---
title: ichartdatapointinterface.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\ichartdatapointinterface.md
created_at: 2025-07-03
---






##### IChartDataPoint interface {#ichartdatapoint-interface style="tab-stops: 0pt"}

IChartDataPoint interface is a point that contains the information about the data of the chart series, X and Y coordinates of the point, and the segment. The IChartDataPoint interface objects can be initialized internally based on the ChartPoint and the object input by the user.

 

Properties

The following table lists the properties of the IChartDataPoint interface.

 

Table 1: Properties of IchartDataPoint


  --------------- ----------------------------------------------------------------------------------------------- --------------
  Property name   Description                                                                                     Data Type
  X               Represents the X value of the DataPoint.                                                        Double
  Y               Represents the Y value of the DataPoint.                                                        Double
  ParentSegment   Represents the parent segment of the DataPoint.                                                 ChartSegment
  Visible         Sets the visibility of the DataPoint.                                                           Bool
  Item            Includes X,Y and custom values to represent the point.                                          Object
  Label           Value represnts the ContentPath.                                                                String
  IsEmpty         Indicates whether the point is empty.                                                           Bool
  Values          Value array should be used to represent the range of Y values that correspond to one X value.   Double
  EmptyPoint      Value indicates the Empty Point.                                                                Bool
  --------------- ----------------------------------------------------------------------------------------------- --------------


[] 

Following are the code that describes the IChartDataPoint interfaces.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [class][ [CustomPoint] : [IChartDataPoint]]                                                                             |
|                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        [public] CustomPoint([double] X, [double] Y)]                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [this].X = X;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            [this].Y = Y;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            [this].Values = [new] [double]\[\] { Y };]                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [        [public] [double] X { [get]; [set]; }]                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [public] [double] Y { [get]; [set]; }]                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [public] [double]\[\] Values { [get]; [set]; }]                                                                             |
|                                                                                                                                                                                                                                                              |
| [        [public] [bool] IsEmpty { [get]; [set]; }]                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        [public] [bool] EmptyPoint { [get]; [set]; }]                                                                               |
|                                                                                                                                                                                                                                                              |
| [        [public] [string] Label { [get]; [set]; }]                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        [public] [bool] Visible { [get]; [set]; }]                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        [public] [object] StringItem { [get]; [set]; }]                                                                             |
|                                                                                                                                                                                                                                                              |
| [        [public] [ChartSegment] ParentSegment { [get]; [set]; }]                                                                 |
|                                                                                                                                                                                                                                                              |
| [        [public] [object] Item { [get]; [set]; }]                                                                                   |
|                                                                                                                                                                                                                                                              |
| [     ]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        [public] [object] Clone()]                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [CustomPoint] customPoint = [new] [CustomPoint]([this].X, [this].Y);]                        |
|                                                                                                                                                                                                                                                              |
| [            [//\...]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            [// Filling proper fields.]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [            [//\...]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            [return] customPoint;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [        [public] [void] Dispose()]                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [    [// Custom collection strongly typed as CustomPoint that implements IChartData.]]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [    [class] [CustomChartPointsCollection] : [ObservableCollection]\<[CustomPoint]\>, [IChartData]] |
|                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        [public] [new] [IChartDataPoint] [this]\[[int] index\]]                                             |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [get] { [return] [base]\[index\]; }]                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [        [public] [ChartValueType] XValueType { [get]; [set]; }]                                                                  |
|                                                                                                                                                                                                                                                              |
| [        #region][ IDisposable Members]                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\<summary\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [        [///][ Clean up any resources being used.]]                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        [public] [void] Dispose()]                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [           ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        #endregion]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [    }][}]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [  [//Using classes]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [//\...]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            [//Creating a new chart1 with area and series.]]                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [            [//\...]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            [CustomChartPointsCollection] customCollection = [new]]                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [            [CustomChartPointsCollection]();]                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            customCollection.Add([new] [CustomPoint](1, 3));]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            customCollection.Add([new] [CustomPoint](2, 5));]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            customCollection.Add([new] [CustomPoint](3, 2));]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            customCollection.Add([new] [CustomPoint](4, 8));]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            chart1.Areas\[0\].Series\[0\].Data = customCollection;]                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[]{#related-topics}


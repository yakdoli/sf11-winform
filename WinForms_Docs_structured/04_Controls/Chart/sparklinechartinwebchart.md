---
title: sparklinechartinwebchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\sparklinechartinwebchart.md
created_at: 2025-07-03
---








  









### Sparkline Chart in Web Chart {#sparkline-chart-in-web-chart style="tab-stops: 0pt"}

A Sparkline control is a type of information graphic characterized by its small size, high data density and light weight. It presents trends and [variations in a very condensed manner. ]

[The Sparkline does not contain an axis scale and gives a high-level overview of changes to data over time.]

 

Presently, Syncfusion SparkLine control supports three types of Sparklines and the Sparkline control must be bound to a data source. It supports a variety of data source such as DataTable and any component that implements the interface IEumerable, ICollection, IList.

• Line

• Column

• Win-Loss

 

**Use Case Scenarios**

A Sparkline can display a trend based on adjacent data in a clear and compact graphical representation. The purpose of the Sparkline is to quickly see the data range difference with high density data and it is represented in lightweight graphical representation. You can use it as per your requirement.

The following screenshot shows three types of Sparkline charts (line, column and win-loss) which are drawn inside the grid control cell, based on row values.

{border="0"}

Figure 86: Sparkline control in RealTime

 

Where do I find Samples?

To access a Sparkline sample Demo:

1.   Open the Syncfusion Dashboard.

2.   Select User Interface.

3.   Click the **Windows Forms** drop-down list and select **Explore Samples**.

4.   Navigate to **Chart.Windows** -\> **Samples** -\> **2.0** -\> **SparklineChart**.

 

Tables for Properties, Methods, and Events

Properties

+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| Property                        | Description                                                                          | Type        | Data Type   | Reference links |
+=================================+======================================================================================+=============+=============+=================+
| Type[ ] | Specifies the types of spark lines.                                                  | NA          | NA          | NA              |
|                                 |                                                                                      |             |             |                 |
|                                 | • Line                                                                               |             |             |                 |
|                                 |                                                                                      |             |             |                 |
|                                 | • Column                                                                             |             |             |                 |
|                                 |                                                                                      |             |             |                 |
|                                 | • WinLoss                                                                            |             |             |                 |
|                                 |                                                                                      |             |             |                 |
|                                 | By default, it is set to Line type.                                                  |             |             |                 |
+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| Source                          | Gets or sets the data source for sparkline data points                               | NA          | NA          | NA              |
+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| LineStyle                       | Customizes the styles of Line sparkline                                              | NA          | NA          | NA              |
+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| ColumnStyle                     | Customizes the styles of Column and Winloss sparklines                               | NA          | NA          | NA              |
+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| Markers                         | Enables the markers support to sparkline                                             | NA          | NA          | NA              |
+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+
| BackInterior                    | Customizes the background color of the control. By default, it is set to White color | NA          | NA          | NA              |
+---------------------------------+--------------------------------------------------------------------------------------+-------------+-------------+-----------------+

 

Methods

 

  Method          Description                                       Parameters   Type   Return Type   Reference links
  --------------- ------------------------------------------------- ------------ ------ ------------- -----------------
  GetHighPoint    Gets the highest point value from the sparkline   NA           NA     Void          NA
  GetLowPoint     Gets the lowest point value from the sparkline    NA           NA     Void          NA
  GetStartPoint   Gets the start point value from the sparkline     NA           NA     Void          NA
  GetEndPoint     Gets the end point value from the sparkline       NA           NA     Void          NA

More:








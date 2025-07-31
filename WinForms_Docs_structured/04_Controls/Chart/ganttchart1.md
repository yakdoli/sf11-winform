---
title: ganttchart1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\ganttchart1.md
created_at: 2025-07-03
---






#### Gantt Chart {#gantt-chart style="tab-stops: 0pt"}

 

A Gantt chart is a graphical representation of the duration of tasks against the progression of time. In a Gantt chart, each task takes up one row. The expected time for each task is represented by a horizontal bar for which the left end marks the expected beginning of the task and right end marks the expected completion of the task. Tasks may run sequentially, parallel, or sometimes tasks may overlap.

You could use another series to represent the completed portion of the different tasks. This new series will contain data points with their start values coinciding with the start values of the data points from the previous series and the end value based on the fraction of the work that has been completed on the task. This way you can get a quick reading of a project's progress by drawing a vertical line through the chart on the current date.                               

Gantt chart can be created in two ways namely:

[·      ]Builder

[·      ]ChartModel

**[]** 

Chart Details

 


+------------------------------+----------------------------------------------------------------+
| Details                                                                                       |
+------------------------------+----------------------------------------------------------------+
| Number of Y values per point | 2 (1st is the beginning value and the 2nd is the ending value) |
+------------------------------+----------------------------------------------------------------+
| Number of Series             | One or more                                                    |
+------------------------------+----------------------------------------------------------------+
| Cannot be Combined with      | Pie chart, Bar chart, Polar chart, and Radar chart.            |
+------------------------------+----------------------------------------------------------------+


[] 

More:








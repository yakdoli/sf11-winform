---
title: supportforlabelreadability.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportforlabelreadability.md
created_at: 2025-07-03
---








  









## Support for Label Readability {#support-for-label-readability style="tab-stops: 0pt"}

 

OLAP Chart provides support to either resize the chart to fit within the view area or enable scroll bar while expanding the labels. This enables you to set the label readable.

 

Use Case Scenarios

You can resize the content, if you want to view the entire content in the view area. While resizing the content, it may become illegible due to size. To avoid this you can enable scrollbar.

 

Properties

Table 32: Property Table


  ----------------------- -------------------------------------------------- ------------- --------------- ---------------------
  **Property**            **Description**                                    **Type**      **Data Type**   **Reference links**
  ForceLabelReadability   Resize the control to fit within the view area.    Server side   Boolean         NA
  ----------------------- -------------------------------------------------- ------------- --------------- ---------------------


[] 

Setting Label Readability

You can enable scrollbar or resize the content using the *ForceLabelReadability* property. To enable scrollbar, set this to true. By default this is set to true. To resize the content, set this to false.

 

The following code illustrates how to enable scrollbar:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                      |
|                                                                                                                                                                                                              |
| [this][.OlapClient1.OlapChart.ForceLabelReadability = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                           |
|                                                                                                                                                                                                            |
| [Me][.OlapClient1.OlapChart.ForceLabelReadability = [True] ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 55: ScrollBar Enabled

 

The following code illustrates how to resize the content:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                       |
|                                                                                                                                                                                                               |
| [this][.OlapClient1.OlapChart.ForceLabelReadability = [false];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                        |
| [Me][.OlapClient1.OlapChart.ForceLabelReadability = [False]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 56: Content Resized

 

Sample Link

To view the samples:

7.   Open **Syncfusion Dashboard**.

8.   Click **BI \> ASP.NET**.

9.   Click **Run Samples**.

10.  Navigate to **OlapChart \> Zooming and Scrolling \> Zooming and Scrolling Demo**.

 

 

 

[]{#related-topics}


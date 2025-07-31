---
title: customizetheappearance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\customizetheappearance.md
created_at: 2025-07-03
---






#### Customize the Appearance {#customize-the-appearance style="tab-stops: 0pt"}

Essential Grid provides support to display horizontal and vertical lines and customize the grid line color.

 

**Displaying Horizontal Lines**

You can display horizontal lined using the *DisplayHorizontalLines*property.

The following code illustrates how to display horizontal lines in GridControl:

 

  ----------------------------------------------------------------------------------------------------------
  [gridControl1.DisplayHorizontalLines = [true];]
  ----------------------------------------------------------------------------------------------------------

 

 

The following code illustrates how to display horizontal lines in GridDataBoundGrid:

 

  ----------------------------------------------------------------------------------------------------------------------------
  [gridDataBoundGrid.DisplayHorizontalLines = [true];]
  ----------------------------------------------------------------------------------------------------------------------------

 

The following code illustrates how to display horizontal lines in GridGrouping control:

  ------------------------------------------------------------------------------------------------------------------
  [gridGroupingControl1.DisplayHorizontalLines = [true];]
  ------------------------------------------------------------------------------------------------------------------

 

 

**Displaying Vertical Lines**

You can display vertical lined using the *DisplayVerticalLines* property.

The following code illustrates how to display vertical lines in GridControl:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  [gridControl1][.DisplayVerticalLines = [true];]
  -----------------------------------------------------------------------------------------------------------------------------------------------------------

 

The following code illustrates how to display vertical lines in GridDataBoundGrid:

  --------------------------------------------------------------------------------------------------------------------------
  [gridDataBoundGrid.DisplayVerticalLines = [true];]
  --------------------------------------------------------------------------------------------------------------------------

 

 

The following code illustrates how to display vertical lines in GridGrouping control:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [gridGroupingControl1][.DisplayVerticalLines = [true];]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

**Customizing Grid Line Color**

 

You can customize grid line color using the *GridLineColor* property.

The following code illustrates how to display vertical lines in GridControl:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  [gridControl1][.GridLineColor = [Color].Red;]
  ------------------------------------------------------------------------------------------------------------------------------------------------------------

 

 

The following code illustrates how to customize grid line color in GridDataBoundGrid:

 

  ---------------------------------------------------------------------------------------------------------------------------
  [gridDataBoundGrid.GridLineColor = [Color].Red;]
  ---------------------------------------------------------------------------------------------------------------------------

 

The following code illustrates how to customize grid line color in GridGrouping control:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [gridGroupingControl1][.GridLineColor = [Color].Red;]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------

**                                                                                                             **

[]{#related-topics}


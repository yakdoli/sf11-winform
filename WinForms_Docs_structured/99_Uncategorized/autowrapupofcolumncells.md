---
title: autowrapupofcolumncells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autowrapupofcolumncells.md
created_at: 2025-07-03
---








  









## Auto Wrap-Up of Column Cells {#auto-wrap-up-of-column-cells style="tab-stops: 0pt"}

This feature helps you view content more easily than conventional methods in a grid. This is because content that exceeds the space in a particular cell can be resized to fit in the cell and can be carried over to the next line.\
You can resize the content in cells using the following settings:

[·      ]**ClipContent:** This property depends on the **AllowAutoWrap** property---it is only enabled when **AllowAutoWrap** is enabled. When you choose to clip content, you will not be able to resize the column width beyond the minimum limit (this is because the **AllowAutoWrap** property is enabled. However, if this property is disabled, **ClipContent** will also be disabled)

[·      ]**ResizeToFit:** This property allows you to choose if you want the column width accommodate the content automatically.

 

Use Case Scenario

This helps the user to see the content in one cell without having to scroll sideways to view the entire content. This allows easy viewing since content is carried to the next line.

 

Appearance and Structure

The following figures illustrate the appearance and structure of the auto wrap feature and its settings:

 

{border="0"}

Figure 283: Grid with AutoWrap Enabled in the Highlighted Column

 

 

{border="0"}

Figure 284: Grid with ClipContent and ResizeToFit Enabled


{border="0"}Notes:



***[·    ]***ClipContent is only enabled when AutoWrap is enabled.

***[·    ]***ResizeToFit doesn't depend on the AutoWrap property.


 

Where do I find the installed samples?

Steps to launch installed samples:

To view the samples:

1.   Open the sample browser and select **ASP.NET MVC** from the left-hand panel.

2.   Click **Run samples** to launch the ASP.NET MVC sample browser.

3.   Select **Grid** from the product icons in the bottom-left of the screen.

4.   Select **Rows and Columns\>AutoWrap Column Cells** to launch the sample.

 

More:








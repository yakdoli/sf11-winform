---
title: olapreportserialization1.md
original_path: WinForms_Docs/99_Uncategorized/olapreportserialization1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## OlapReport Serialization {#olapreport-serialization style="tab-stops: 0pt"}

This feature enables the user to save additional settings along the OLAP information in an OlapReport and load them whenever required.

The following are the appearance settings that a user can save and load during the runtime in an OlapChart and OlapGrid.

OlapChart:

[·      ]Appearance

[·      ]Legend position

[·      ]Series color types

[·      ]Skin for chart

OlapGrid:

[·      ]Freeze headers

[·      ]Show Tooltip

[·      ]Header and Value cell settings

[·      ]Appearance

 

Use Case Scenarios

The user can maintain the Chart and/or the Grid appearance settings with its OLAP data through an OlapReport.

The following image shows a serialized Chart and Grid appearance settings in an XML format:

{border="0"}

Figure 60 Serialized XML File

 

Properties

Table 1: Properties Table


  ---------------- --------------------------------------------- ------ ------------------------ -----------------
  Property         Description                                   Type   Data Type                Reference links
   ChartSettings   Gets or  sets the chart appearance settings   CLR    ChartApperanceSettings   \-
  GridSettings     Gets or sets the Grid appearance settings     CLR    GridAppearanceSettings   \-
  ---------------- --------------------------------------------- ------ ------------------------ -----------------


[] 

Sample Link

The user can find samples in the following locations:

*For OlapChart*

**SystemDrive:\\Users\\\<user_name\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\\<version_number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Serialization\\Serialization Demo**

*For OlapGrid*

**SystemDrive:\\Users\\\<user_name\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\\<version_number\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Serialization\\Serialization Demo**

[]{#related-topics}


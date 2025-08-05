---
title: communicatetheolapcontrolwiththebase.md
original_path: WinForms_Docs/99_Uncategorized/communicatetheolapcontrolwiththebase.md
created_at: 2025-08-05
---








  









## Communicate the OLAP control with the base {#communicate-the-olap-control-with-the-base style="tab-stops: 0pt"}

Each and every control has an **OlapDataManager** property. Through this property, the control sends and receives information to and from the base.

Below steps explains how to load data in an OLAP control:

1.   Give the connection information and **OlapReport** to the **OlapDataManager**.

2.   Assign this **OlapDataManager** to the control's **OlapDataManager** property.

3.   By invoking the control's **DataBind()** method virtually when setting the value for the OlapDataManager property, the data processing will begin and the output is displayed in the Control.

[]{#related-topics}


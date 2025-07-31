---
title: scrollsupport2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollsupport2.md
created_at: 2025-07-03
---






#### Scroll Support {#scroll-support style="tab-stops: 0pt"}

MenuAdv allows users to scroll through the submenu items so that all the items of the submenu are visible even if the submenu crosses the vertical boundary. The Scroll support can be enabled by setting the IsScrollEnabled property to true. If the IsScrollEnabled property is set to false, users will not be able to scroll through the submenu items and the items that cross the vertical boundary will not be visible.

[] 

{border="0"}

Figure 731: Scroll Support

 

Use Case Scenarios

MenuAdv will be very useful in the case of adding more number of items to the single MenuItemAdv and the size of the submenu crosses the vertical boundary.

**[]** 

Using the Scroll Support in an Application

If the value of the IsScrollEnabled property is set to true, users can scroll through the submenu items by using the TopScrollButton, BottomScrollButton, and  mouse wheel. If the value of the IsScrollEnabled property is set to false, users will not be able to scroll through the submenu items.

 

 

[] 

**[]** 

Properties

The property for the Scroll support is described in the following tabulation:

[] 

Table 69: Property Table

  ----------------- ------------------------------------------ -------------------- ------------ -----------------
  Property          Description                                Type                 Data Type    Reference links
  IsScrollEnabled   Gets or sets IsScrollEnabled of MenuAdv.   DependencyProperty   bool(true)   
  ----------------- ------------------------------------------ -------------------- ------------ -----------------

**[]** 

Sample Link

WPF Sample Browser-\> Tools -\> MenuAdv -\> MenuAdv Demo

 

 

[]{#related-topics}


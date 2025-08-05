---
title: propertiesmethodsandevents5.md
original_path: WinForms_Docs/99_Uncategorized/propertiesmethodsandevents5.md
created_at: 2025-08-05
---






##### Properties, Methods, and Events {#properties-methods-and-events style="tab-stops: 0pt"}

**[]** 


  -------------- ----------------------------------------------- ------------ ---------------------- ------------------ --------------------------------------------------
  Property       Description                                     Type         Type of the property   Value it accepts   Any other dependencies/sub-properties associated
  AllowSorting   Used to enable sorting in MultiColumnDropDown   ServerSide   Boolean                True/false         NA
  ActionMode     Used to set ActionMode either JSON or Server    ServerSide   String                 JSON/Server        AllowSorting
  ItemTemplate   Used to set the template element ID.            ServerSide   String                 Any string         ActionMode
  -------------- ----------------------------------------------- ------------ ---------------------- ------------------ --------------------------------------------------


 

Methods

 


+----------------------------+-----------------+-----------------------------+---------------------------------------------------+
| Method                     | Arguments       | Return type                 | Description                                       |
+----------------------------+-----------------+-----------------------------+---------------------------------------------------+
| AllowSorting (Boolean)**** | Boolean         | IMultiColumnDropDownBuilder | Used to enable the Sorting in MultiColumnDropDown |
|                            |                 |                             |                                                   |
|                            |                 |                             |                                                   |
+----------------------------+-----------------+-----------------------------+---------------------------------------------------+
| ActionMode(String)         | String          | IMultiColumnDropDownBuilder | Used to set ActionMode either JSON or Server      |
|                            |                 |                             |                                                   |
|                            |                 |                             |                                                   |
+----------------------------+-----------------+-----------------------------+---------------------------------------------------+
| ItemTemplate(String)       | String          | IMultiColumnDropDownBuilder | Used to set the Template element ID.              |
+----------------------------+-----------------+-----------------------------+---------------------------------------------------+


 

**Sample Link**

To access the samples:

[[1.   ]]{.UGHyperlink}Go to **Grid MVC Demos** in the sample browser. Refer to [Installation and Deployment\>Samples and Location]{.UGHyperlink}[[.]]{.UGHyperlink}[]{.UGHyperlink}

2.   Select the **MultiColumnDropDown** on left side **Accordion**

3.   Select the **Core Features** demo to view the **MultiColumnDropDown** full-fledged demo.

 

[]{#related-topics}


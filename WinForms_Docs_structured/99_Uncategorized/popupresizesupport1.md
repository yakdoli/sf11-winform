---
title: popupresizesupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\popupresizesupport1.md
created_at: 2025-07-03
---






#### Popup Resize Support {#popup-resize-support style="tab-stops: 0pt"}

AutoComplete allows you to resize the drop-down list popup using the **CanResizePopup** property. If this property is set as True the thumb will be shown in the right bottom corner of the drop-down list which adjusts the height and the width of the popup at runtime. If this property is set as False, the visibility of the thumb will be collapsed and you will not be able to resize the popup at runtime.

 

**Adding Popup Resizing Support to an Application**

You can use **CanResizePopup** property to attain this functionality by setting the value as True.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete1\"][ ][CanResizePopup [=\"true\"]][ /\>][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                               |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]       |
|                                                                                                                                                                                               |
| [autoComplete1][.][ CanResizePopup ][= true;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Properties

Table 16: Properties Table for Popup Resize


  ---------------- --------------------------------------------------------------- -------------------- ----------- -----------------
  Property         Description                                                     Type                 Data Type   Reference links
  CanResizePopup   Gets or sets the value of CanResizePopup in the AutoComplete.   DependencyProperty   bool        
  ---------------- --------------------------------------------------------------- -------------------- ----------- -----------------


[] 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}


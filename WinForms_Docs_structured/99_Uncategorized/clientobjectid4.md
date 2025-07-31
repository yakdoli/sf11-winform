---
title: clientobjectid4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientobjectid4.md
created_at: 2025-07-03
---






##### ClientObjectID {#clientobjectid style="tab-stops: 0pt"}

[] 

The ClientObjectID can be used to access the control\'s object model on the client-side.

ClientObjectID can be effectively used to refer the control\'s objects when used with MasterPages and UserControls. By default, a client object id is computed by concatenating \'\_sf\' and the control\'s **ID** property. However, in the case of hosting the control in a MasterPage or UserControl, the computed client object id is very unintuitive. To make things simpler, you can specify a custom value on this property and access the client-side object model using that value.

[] 


+-----------------------------------+------------------------------------------------------------------------+
|                                   |                                                                        |
|                                   |                                                                        |
| Property                          | Description                                                            |
+-----------------------------------+------------------------------------------------------------------------+
| ClientObjectID                    | Specifies the user defined id for accessing the object on client-side. |
+-----------------------------------+------------------------------------------------------------------------+


[] 

The ClientObjectID can be set programmatically as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                        |
| []                                                                    |
|                                                                                                                                        |
| [multiSelectionDropDown1.ClientObjectID = [\"Custom ID\"];] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| []                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [Private][ multiSelectionDropDown1.ClientObjectID = [\"Custom ID\"]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}


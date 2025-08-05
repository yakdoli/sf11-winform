---
title: miscellaneousproperties.md
original_path: WinForms_Docs/99_Uncategorized/miscellaneousproperties.md
created_at: 2025-08-05
---






##### [Miscellaneous Properties] {#miscellaneous-properties style="tab-stops: 0pt"}

[] 

Read-Only Mode

[] 

The **Editable** property lets you render the control in a read-only mode.

[] 


  ---------- ---------------------------------------------------------------------------------
  Property   Description
  Editable   Gets / sets the boolean value determining the edit mode. Default value is True.
  ---------- ---------------------------------------------------------------------------------


[] 

Programmatically the Editable property can be set as follows.

[  ]

+----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                               |
|                                                                                                                |
| []                                            |
|                                                                                                                |
| [RichTextEditor1.Editable = [false];] |
+----------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                         |
|                                                                                                                                                                                          |
| []                                                                                                                      |
|                                                                                                                                                                                          |
| [Private][ RichTextEditor1.Editable = [False]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientObjectID

[] 

The client object id can be used to access the control on and only on the client side. By default the client object corresponding to this control will be provided a default object id based on the control\'s id in the aspx page. However, in scenarios where this object is hosted within a MasterPage or in a UserControl, the id generated automatically is usually less intuitive. In such scenarios, use the **ClientObjectId** to specify a custom id for the client object.

[] 


  ---------------- ------------------------------------------------------------------------
  Property         Description
  ClientObjectID   Specifies the user defined id for accessing the object on client side.
  ---------------- ------------------------------------------------------------------------


[] 

Programmatically the ClientObjectID can be set as follows.

[  ]

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                                |
| []                                                            |
|                                                                                                                                |
| [RichTextEditor1.ClientObjectID = [\"Custom ID\"];] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Private][ RichTextEditor1.ClientObjectID = [\"Custom ID\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


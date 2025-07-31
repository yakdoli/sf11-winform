---
title: loadingindicatorandclientobjectid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadingindicatorandclientobjectid.md
created_at: 2025-07-03
---






##### Loading indicator and ClientObjectID {#loading-indicator-and-clientobjectid style="tab-stops: 0pt"}

[] 

Loading Indicator

[] 

During the loading process of the data by retrieving from the server, a loading indicator can be displayed to indicate the data processing. This loading indicator can be set by enabling the **ShowLoadingIndicatorOnCallback** property.

[] 


  -------------------------------- ---------------------------------------------------------------------
  Property                         Description
  ShowLoadingIndicatorOnCallback   Specifies whether to display the loading indicator during callback.
  -------------------------------- ---------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                          |
| [PercentTextBox1.][ShowLoadingIndicatorOnCallback][ = [\"Custom ID\"];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ PercentTextBox1.][ShowLoadingIndicatorOnCallback][ = [\"Custom ID\"]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

ClientObjectID

[] 

The client object id can be used to access the control only on client side. **ClientObjectId** can effectively be used to refer the control\'s objects when used with User controls, Master pages and Callback controls. This client id can be effectively used in such scenarios instead of the default id with which the control have to be denoted, thereby eliminating any such ambiguity with the references.

[] 


+-----------------------------------+------------------------------------------------------------------------+
|                                   |                                                                        |
|                                   |                                                                        |
| Property                          | Description                                                            |
+-----------------------------------+------------------------------------------------------------------------+
| ClientObjectID                    | Specifies the user defined id for accessing the object on client side. |
+-----------------------------------+------------------------------------------------------------------------+


[] 

Programmatically the ClientObjectID can be set as follows.

[  ]

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                               |
| []                                                           |
|                                                                                                                               |
| [CallBackPanel1.ClientObjectID = [\"Custom ID\"];] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                         |
| []                                                                                                                                     |
|                                                                                                                                                                                                         |
| [Private][ CallBackPanel1.ClientObjectID = [\"Custom ID\"]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


---
title: tabprimitiveclickevent.md
original_path: WinForms_Docs/99_Uncategorized/tabprimitiveclickevent.md
created_at: 2025-08-05
---






#### TabPrimitiveClick Event {#tabprimitiveclick-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs before the NavigationButton click.

 

**Event Data**

 

This Event Handler receives an argument of type **TabPrimitiveClickEventArgs** containing data related to this event. The following TabPrimitiveClickEventArgs properties provide information specific to this event.

[] 


  -------------- ----------------------------------------------------------------------
  Members        Description
  Cancel         Gets / sets a value indicating whether the event should be canceled.
  TabPrimitive   Gets the primitive that gets clicked.
  -------------- ----------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [private][ [void] tabControlAdv4_TabPrimitiveClick([object] sender, Syncfusion.Windows.Forms.Tools.[TabPrimitiveClickEventArgs] e)] |
|                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [if][(e.TabPrimitive.Name == [\"CustomAbout\"])]                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [DemoCommon.[AboutForm] ab=[new] DemoCommon.[AboutForm]( [AppDomain].CurrentDomain.GetAssemblies());]                                                           |
|                                                                                                                                                                                                                                                                                         |
| [ab.ShowDialog();]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [//This event can be canceled using the code given below.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [e.Cancel = [true];]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [//This code displays the primitive that gets clicked during this event.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [Console][.Write([\"TabPrimitiveClick:\"] + e.TabPrimitive.ToString());]                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] tabControlAdv4_TabPrimitiveClick([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.TabPrimitiveClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [If][ e.TabPrimitive.Name = [\"CustomAbout\"] [Then]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ ab [As] DemoCommon.AboutForm = [New] DemoCommon.AboutForm(AppDomain.CurrentDomain.GetAssemblies)]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [ab.ShowDialog()]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [If]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\'this event can be canceled using the code given below.]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\'This code displays the primitive that gets clicked during this event.]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Console][.Write([\"TabPrimitiveClick:\"] + e.TabPrimitive.ToString())]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p883} 

[]{#related-topics}


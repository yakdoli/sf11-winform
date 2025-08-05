---
title: providepersistenceidevent.md
original_path: WinForms_Docs/99_Uncategorized/providepersistenceidevent.md
created_at: 2025-08-05
---






##### ProvidePersistenceID Event {#providepersistenceid-event style="tab-stops: 0pt"}

 

  This event lets you specify a unique ID to distinguish the persistence information of different instances of the Form type.

[] 

Event Data

**[]** 

The event handler receives an argument of type ProvidePersistenceIDEventArgs containing data related to this event. The following ProvidePersistenceIDEventArgs property provides information specific to this event.

[] 


  --------------- -------------------------------
  Member          Description
  PersistenceID   Lets you specify a unique ID.
  --------------- -------------------------------


**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Lets you specify a unique ID used to distinguish the persistence information of different]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                          |
| [//instances of the Form type.]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| [protected void ][DockingManager_ProvidePersistenceID(][object ][sender,Syncfusion.Windows.Forms.ProvidePersistenceIDEventArgs e)] |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Provide Persistence ID Event has been raised\");]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [Syncfusion.Windows.Forms.Tools.DockingManager dm = sender ][as ][DockingManager;]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                          |
| [Console.WriteLine(\"Host control name = \"+dm.HostControl.Name.ToString());]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                          |
| [//The docking state stores in a place named as that Host control name.]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                          |
| [e.PersistenceID=dm.HostControl.Name.ToString();]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\'Lets you specify a unique ID used to distinguish the persistence information of different]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\'instances of the Form type.]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Protected][ [Sub] DockingManager_ProvidePersistenceID([ByVal] sender [As] [Object], [ByVal] e [As]Syncfusion.Windows.Forms.ProvidePersistenceIDEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Provide Persistence ID Event has been raised\"])]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ dm [As] Syncfusion.Windows.Forms.Tools.DockingManager = [CType](ConversionHelpers.AsWorkaround(sender, [GetType](DockingManager)), DockingManager)]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Host control name = \"] + dm.HostControl.Name.ToString)]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\'The docking state stores in a place named as that Host control name.]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [e.PersistenceID = dm.HostControl.Name.ToString]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}


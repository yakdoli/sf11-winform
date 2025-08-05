---
title: initializecontrolonloadevent.md
original_path: WinForms_Docs/99_Uncategorized/initializecontrolonloadevent.md
created_at: 2025-08-05
---






##### InitializeControlOnLoad Event {#initializecontrolonload-event style="tab-stops: 0pt"}

[] 

The InitializeControlOnLoad event occurs when the DockingManager is not able to locate a control during a LoadDockState call.

[] 

Event Data

**[]** 

The event handler receives an argument of type InitializeControlOnLoadEventArgs containing data related to this event. The following InitializeControlOnLoadEventArgs property provides information specific to this event.

[] 


  ------------- -----------------------------------
  Member        Description
  ControlName   The Name property of the control.
  ------------- -----------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [protected void ][DockingManager_InitializeControlOnLoad(][object ][sender,] |
|                                                                                                                                                                                                                                                                                    |
| [InitializeControlOnLoadEventArgs args)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [Console.WriteLine(\"InitializeControlOnLoad Event is Raised for the Control :]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                    |
| [\" +args.ControlName);]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [DockingManager dockingmgr = sender ][as ][DockingManager;]                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [switch ][(args.ControlName)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [case ][\"Suite Logo\":]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [this][.ActivateSuiteLogoControl(dockingmgr, ][false][);]                    |
|                                                                                                                                                                                                                                                                                    |
| [break][;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [case ][\"Suite Info\":]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [this][.ActivateSuiteInfoControl(dockingmgr, ][false][);]                    |
|                                                                                                                                                                                                                                                                                    |
| [break][;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [case ][\"Tools Info\":]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [this][.ActivateToolsInfoControl(dockingmgr, ][false][);]                    |
|                                                                                                                                                                                                                                                                                    |
| [break][;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [case ][\"Tools Logo\":]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [this][.ActivateToolsLogoControl(dockingmgr, ][false][);]                    |
|                                                                                                                                                                                                                                                                                    |
| [break][;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [case ][\"Grid Logo\":]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [this][.ActivateGridLogoControl(dockingmgr, ][false][);]                     |
|                                                                                                                                                                                                                                                                                    |
| [break][;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [case ][\"Grid Info\":]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [this][.ActivateGridInfoControl(dockingmgr, ][false][);]                     |
|                                                                                                                                                                                                                                                                                    |
| [break][;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Protected][ [Sub] DockingManager_InitializeControlOnLoad([ByVal] sender [As] [Object], [ByVal] args [As] InitializeControlOnLoadEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine([\"InitializeControlOnLoad Event is Raised for the Control : \"] + args.ControlName)]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ dockingmgr [As] DockingManager = [CType](ConversionHelpers.AsWorkaround(sender, [GetType](DockingManager)), DockingManager)]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Select][ [Case] args.ControlName]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ [\"Suite Logo\"]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ActivateSuiteLogoControl(dockingmgr, [False])]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' break ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ [\"Suite Info\"]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ActivateSuiteInfoControl(dockingmgr, [False])]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' break ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ [\"Tools Info\"]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ActivateToolsInfoControl(dockingmgr, [False])]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' break ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ [\"Tools Logo\"]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ActivateToolsLogoControl(dockingmgr, [False])]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' break ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ [\"Grid Logo\"]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ActivateGridLogoControl(dockingmgr, [False])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' break ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ [\"Grid Info\"]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ActivateGridInfoControl(dockingmgr, [False])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' break ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Select]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}


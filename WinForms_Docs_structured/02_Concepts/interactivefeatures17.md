---
title: interactivefeatures17.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\interactivefeatures17.md
created_at: 2025-07-03
---






#### Interactive Features {#interactive-features style="tab-stops: 0pt"}

A basic requirement in creating any WPF application that uses our DockingManager control, is the ability to set a window as an active window. DockingManager\'s ActiveWindow property can be used for this. ActiveWindow is an element, which returns a window object that is currently focused. To set a window as active, use the following code.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<!\--Adding Docking Manager\--\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        ][\<][syncfusion][:][DockingManager][ AutoHideAnimationMode][=\"Fade\"][ Name][=\"DockingManager\"][ Loaded][=\"DockingManager_Loaded\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            ][\<!\--Adding Children for the Docking Manager control with state as Dock and a side in dock mode as left\--\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            ][\<][StackPanel][ syncfusion][:][DockingManager.State][=\"Dock\"][ Name][=\"Element One\"][]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [             [ syncfusion][:][DockingManager.SideInDockedMode][=\"Left\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            ][\<][StackPanel][ syncfusion][:][DockingManager.State][=\"Dock\"][ Name][=\"Element Two\"][]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [             [ syncfusion][:][DockingManager.SideInDockedMode][=\"Right\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        ][\</][syncfusion][:][DockingManager][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [//Setting the active window, giving the name of the children element as the parameter for the Activate Window.][] |
|                                                                                                                                                                                                                                            |
| [DockingManager.ActivateWindow([\"Name of the Window\"]);]                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event

 


  ----------------------- -------------------------------------------
  Event                   Description
  OnActiveWindowChanged   Handled when an active window is changed.
  ----------------------- -------------------------------------------


[] 

Method

 


  ------------------ ---------------------------------------------------------
  Method             Description
  OnActivateWindow   This method is called when an active window is changed.
  ------------------ ---------------------------------------------------------


 

Retrieving an Active Window from **DockingManager**

 

Sometimes, you need to identify an active window to perform some operations at run time. For this, create an object for the **FrameWorkElement** and set the **DockingManager** active window to it. Now the **FrameWorkElement** object returns the active window.

 

The following code snippet explains how to retrieve the **Active** window from the **Docking Manager** control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                       |
|                                                                                                                                                                                               |
| [//Checking the active window as null or not.][]                    |
|                                                                                                                                                                                               |
| [if][ (DockingManager1.ActiveWindow != [null])] |
|                                                                                                                                                                                               |
| [{]                                                                                                                                     |
|                                                                                                                                                                                               |
| [    [//Setting the Frameworkelement object with the Docking Manager\'s active window]]                           |
|                                                                                                                                                                                               |
| [    [FrameworkElement] ffelement = DockingManager1.ActiveWindow;]                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                      |
|                                                                                                                                                                                               |
| [    [//Returning the active window]]                                                                             |
|                                                                                                                                                                                               |
| [    [return] ffelement;]                                                                                          |
|                                                                                                                                                                                               |
| [}]                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Where, the \'ffelement\' returns the active window.

 

You can also iterate through all the child elements of the DockingManager control, and get the active window to perform the actions, if any. This behavior is demonstrated in the following example on a button click event.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [// Handles the Click event of the dockingactivewindow control.][]                                            |
|                                                                                                                                                                                                                                         |
| [        [private] [void] dockingactivewindow_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [            [//Getting the sender as Docking Manager]]                                                                                                     |
|                                                                                                                                                                                                                                         |
| [            DockingManager1 = sender [as] DockingManager;]                                                                                                  |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [            [//Iterating through the children of the Docking Manager control]]                                                                             |
|                                                                                                                                                                                                                                         |
| [            [foreach] ([FrameworkElement] felement [in] DockingManager1.Children)]                             |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                [//Checking the active window]]                                                                                                            |
|                                                                                                                                                                                                                                         |
| [                [if] (ffelement == DockingManager1.ActiveWindow)]                                                                                           |
|                                                                                                                                                                                                                                         |
| [                {]                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [                    [//Do the actions here]]                                                                                                               |
|                                                                                                                                                                                                                                         |
| [                }]                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

More:


















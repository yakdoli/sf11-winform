---
title: folderbrowserevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\folderbrowserevent.md
created_at: 2025-07-03
---






##### FolderBrowser Event {#folderbrowser-event style="tab-stops: 0pt"}

[]{#p499}[] 

A detailed explanation about the FolderBrowserCallback event is given in the following section.

[] 


  ----------------------- -------------------------------------------------------------------------------------------------------------
  FolderBrowser Event     Description
  FolderBrowserCallback   The event occurs when an event within the Folder Browser Dialog triggers a call to the validation callback.
  ----------------------- -------------------------------------------------------------------------------------------------------------


 

[]{#p500} 

###### 3.3.7.1.4.1 FolderBrowserCallback Event {#folderbrowsercallback-event style="tab-stops: 0pt"}

[] 

The event occurs when an event within the folder browser dialog triggers a call to the validation callback. The event handler receives an argument of type **FolderBrowserCallbackEventArgs**.

 

The following FolderBrowserCallbackEventArgs[ ]members provide information specific to this event.

 


  ------------------------------- ------------------------------------------------------------------------------------------
  Members                         Description
  Dismiss                         Specifies whether the dialog is either dismissed or retained depending upon this value.
  FolderBrowserCallbackSetState   Gets / sets the Folder Browser dialog\'s state.
  BrowseCallbackText              Gets / sets the contextual string based upon the FolderBrowserCallbackSetState property.
  FolderBrowserMessage            Returns a value indentifying the event.
  Path                            Returns valid or invalid folder name.
  Window                          Returns window handle of browser dialog box.
  ------------------------------- ------------------------------------------------------------------------------------------


[] 

It can be handled when browser validation is required.

 

This handler is functionally equivalent to the **Win32 BrowseCallbackProc** callback function.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [private][ [void] folderBrowser1_BrowseCallback([object] sender, Syncfusion.Windows.Forms.[FolderBrowserCallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [// We can log the events and Folder Browser Message to the Label control.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                       |
| [this][.label1.Text = [String].Format([\"Event: {0}, Path: {1}\"], e.FolderBrowserMessage, e.Path);]                                             |
|                                                                                                                                                                                                                                                                                       |
| [if][ (e.FolderBrowserMessage == FolderBrowserMessage.ValidateFailed)]                                                                                                                           |
|                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [e.Dismiss = e.Path != [\"NONE\"];]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] folderBrowser1_BrowseCallback([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.FolderBrowserCallbackEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [\' We can log the events and Folder Browser Message to the Label control.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.label1.Text = [String].Format([\"Event: {0}, Path: {1}\"], e.FolderBrowserMessage, e.Path)]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [If][ e.FolderBrowserMessage = FolderBrowserMessage.ValidateFailed [Then]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [e.Dismiss = e.Path \<\> [\"NONE\"]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}


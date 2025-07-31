---
title: spacesandtabs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\spacesandtabs.md
created_at: 2025-07-03
---








  









### Spaces and Tabs {#spaces-and-tabs style="tab-stops: 0pt"}

 

Edit Control supports text operations with tabs and spaces by using the APIs discussed in this section.

 

Essential Edit controls the insertion of tabs using the **UseTabs** property, which lets you specify whether a tab (or an equivalent number of spaces) needs to be inserted, when the TAB key is pressed in the Edit Control. Similarly, tab stops can also be inserted.

 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| UseTabs                           | Specifies whether tab symbol is allowed or spaces should be used instead.                                           |
|                                   |                                                                                                                     |
|                                   |                                                                                                                     |
|                                   |                                                                                                                     |
|                                   | Setting this property to True, allows you to insert tabs, whereas setting it to False, allows you to insert spaces. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| UseTabStops                       | Gets / sets value that indicates whether tab stops should be used.                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| TabStopsArray                     | Gets / sets an array of tab stops.                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [this][.editControl1.UseTabs = [true];]                                                          |
|                                                                                                                                                                                                            |
| [this][.editControl1.UseTabStops = [true];]                                                      |
|                                                                                                                                                                                                            |
| [this][.editControl1.TabStopsArray = [new] [int]\[\] { 8, 16, 24, 32, 40};] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [Me][.editControl1.UseTabs = [True]]                                                           |
|                                                                                                                                                                                                          |
| [Me][.editControl1.UseTabStops = [True];]                                                      |
|                                                                                                                                                                                                          |
| [Me][.EditControl1.TabStopsArray = [New] [Integer]() {8, 16, 24, 32, 40}] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Specifying Tab Size**

 

The size of the tab can be specified by using the below given property.

 


  ----------------------- -------------------------------
  Edit Control Property   Description
  TabSize                 Specifies tab size in spaces.
  ----------------------- -------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                                         |
| []                                                                    |
|                                                                                                                         |
| [// Size of the tab in terms of space.]                               |
|                                                                                                                         |
| [this][.editControl1.TabSize = 8;] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                   |
|                                                                                                                      |
| []                                                                 |
|                                                                                                                      |
| [\' Size of the tab in terms of space.]                            |
|                                                                                                                      |
| [Me][.editControl1.TabSize = 8] |
+----------------------------------------------------------------------------------------------------------------------+

 

**TAB key Functionality**

 

The **TransferFocusOnTab** property allows you to specify, if the Edit Control should process the TAB key as a text input, or transfer the focus to the next control (by the order of TabIndex property value) on the Form or the User Control hosting the Edit Control.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [// Insert tabs into the EditControl as text input. ]                                                       |
|                                                                                                                                                               |
| [this][.editControl1.TransferFocusOnTab = [false];] |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [// Transfer focus to the next control.]                                                                    |
|                                                                                                                                                               |
| [this][.editControl1.TransferFocusOnTab = [true];]  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Insert tabs into the EditControl as text input.]                                                       |
|                                                                                                                                                              |
| [this][.editControl1.TransferFocusOnTab = [False]] |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Transfer focus to the next control.]                                                                   |
|                                                                                                                                                              |
| [this][.editControl1.TransferFocusOnTab = [True]]  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**TAB key Functionality on Selected Text**

[] 

The below given methods can be used convert the spaces in a selected region into tabs and vice versa. Tab symbols can also be added, inserted or removed from selected text.

 


  ------------------------- ------------------------------------------------------------------------------------
  Edit Control Method       Description
  TabifySelection           Lets you convert the spaces in the selected region into equivalent number of tabs.
  UntabifySelection         Lets you convert the tabs in the selected region into equivalent number of spaces.
  AddTabsToSelection        Adds leading tab symbol to the selected lines, or just inserts the tab symbol.
  RemoveTabsFromSelection   Removes leading tab symbol (or its spaces equivalent) from selected lines.
  ------------------------- ------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                       |
| [// Covert spaces to tabs.]                                                         |
|                                                                                                                                       |
| [this][.editControl1.TabifySelection();]         |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [// Converts tabs to spaces.]                                                       |
|                                                                                                                                       |
| [this][.editControl1.UntabifySelection();]       |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [// Add or insert leading tab symbol to selected lines.]                            |
|                                                                                                                                       |
| [this][.editControl1.AddTabsToSelection();]      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [// Remove leading tab symbol from selected lines.]                                 |
|                                                                                                                                       |
| [this][.editControl1.RemoveTabsFromSelection();] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                 |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [\' Covert spaces to tabs.]                                                      |
|                                                                                                                                    |
| [Me][.editControl1.TabifySelection()]         |
|                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                    |
| [\' Converts tabs to spaces. ]                                                   |
|                                                                                                                                    |
| [Me][.editControl1.UntabifySelection()]       |
|                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                    |
| [\' Add or insert leading tab symbol to selected lines.]                         |
|                                                                                                                                    |
| [Me][.editControl1.AddTabsToSelection()]      |
|                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                    |
| [\' Remove leading tab symbol from selected lines.]                              |
|                                                                                                                                    |
| [Me][.editControl1.RemoveTabsFromSelection()] |
+------------------------------------------------------------------------------------------------------------------------------------+

[]{#p40}**[]** 

**[]** 

 

More:






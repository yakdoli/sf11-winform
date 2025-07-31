---
title: localizationsupport6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\localizationsupport6.md
created_at: 2025-07-03
---








  









## Localization Support {#localization-support style="tab-stops: 0pt"}

Localization is the process of making your application multi-lingual, by formatting content according to cultures. This involves configuring the application for a specific language. Culture is the combination of language and location (e.g. En-US is the culture for English spoken in  United States; En-GB is the culture for English spoken in  Great Britain). Syncfusion Tools allows you to set custom resource through the Resx file. You can simply give the string values in the resource file for a specific culture and set the culture in the application. The given string values will be set to the Tools controls, which does not affect the Code Block.

[] 

Use Case Scenario

The Essential Tools WPF controls can be localized according to the native language. It thus helps you to use the Tools controls more effectively. 

 

Properties, Methods and Events Tables

 

**Properties**

*[]* 

*[]* 

Table 14: Syncfusion.Tools.Wpf Localization Property Table


+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Property                                           | Description                                                                                            | Type            | Data Type       |
+====================================================+========================================================================================================+=================+=================+
| AddItem[]                 | Sets the string for Add button content in Ribbon QAT customization dialog window                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| AddToQAT[]                | Sets the string for the AddToQAT context menu item in Ribbon                                           | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| AutoHide[]                | Sets the string for AutoHide context menu item in Docking Manager                                      | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| AwlButtonTooltipText[]    | Sets the string for the ToolTip of Auto Hide button in Docking Manager                                 | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| BackText[]                | Sets the string for the Back button content in Wizard control.                                         | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Buttons[]                 | Sets the string for Group Bar Buttons   Menu Item                                                      | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Cancel[]                  | Sets the string for the Cancel button content in Ribbon QAT customization dialog window                | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CancelText[]              | Sets the string for the Cancel button content in Wizard control.                                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Choose[]                  | Sets the string for Choose commands in Ribbon QAT customization dialog window.                         | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CloseAllButThis[]         | Sets the string for CloseAllButThis context menu item in Docking Manager and Document Container        | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CloseButtonTooltipText[]  | Sets the string for ToolTip of Close button in Docking Manager                                         | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CloseTooltip[]            | Sets the string for the ToolTip of Close button in Ribbon Window                                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ContextMenuButton                                  | Sets the string for the ToolTip of Content Menu button in Docking Manager                              | static          | string          |
|                                                    |                                                                                                        |                 |                 |
| TooltipText[]             |                                                                                                        |                 |                 |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CustomizeQAT[]            | Sets the string for Customize the Quick Access Toolbar Text in Ribbon                                  | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CustomizeQATContextMenu[] | Sets the string for the CustomizeQAT context menu item in Ribbon                                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Dockable                                           | Sets the string for the Dockable context menu item in Docking Manager                                  | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Document                                           | Sets the string for the Document context menu item in Document Container                               | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| FinishText                                         | Sets the string for the Finish button content in Wizard control                                        | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| FloatButtonTooltipText                             | Sets the string for the ToolTip of Float button in Docking Manager                                     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Floating                                           | Sets the string for the Floating context menu item in Docking Manager                                  | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemAddItem                               | Sets the string for the Add Item context menu item in Group Bar                                        | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemAddTab                                | Sets the string for the Add Tab context menu item in Group Bar                                         | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemCopy                                  | Sets the string for the Copy context menu item in Group Bar                                            | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemCut                                   | Sets the string for the Cut context menu item in Group Bar                                             | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemDeleteItem                            | Sets the string for the Delete Item context menu item in Group Bar                                     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemDeleteTab                             | Sets the string for the Delete Tab context menu item in Group Bar                                      | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemListView                              | Sets the string for the List View context menu item in Group Bar                                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemMoveDown                              | Sets the string for the Move Down context menu item in Group Bar                                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemMoveUp                                | Sets the string for the Move Up context menu item in Group Bar                                         | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemPaste                                 | Sets the string for the Paste context menu item in Group Bar                                           | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemRenameItem                            | Sets the string for the Rename Item context menu item in Group Bar                                     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemRenameTab                             | Sets the string for the Rename Tab context menu item in Group Bar                                      | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemSortAsc                               | Sets the string for the Sort Asc context menu item in Group Bar                                        | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| GroupbarMItemSortDec                               | Sets the string for the Sort Dec context menu item in Group Bar                                        | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| HelpText                                           | Sets the string for the Help button content in Wizard control.                                         | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Hide                                               | Sets the string for Hide context menu item in Docking Manager                                          | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MaximizeRibbon                                     | Sets the string for the Maximize the Ribbon caption.                                                   | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MaximizeTooltip                                    | Sets the string for the ToolTip of Maximize button in Ribbon Window                                    | static          | String          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIClose                                           | Sets the string for the Close context menu item in Document Container                                  | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIDockable                                        | Sets the string for the MDIDockable context menu item in Document Container                            | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIDocument                                        | Sets the string for the MDIDocument context menu item in Document Container                            | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIFloating                                        | Sets the string for the MDIFloating context menu item in Document Container                            | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIMaximize                                        | Sets the string for the Maximize context menu item in Document Container                               | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIMinimize                                        | Sets the string for the Minimize context menu item in Document Container                               | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIMove                                            | Sets the string for the Move context menu item in Document Container                                   | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIResize                                          | Sets the string for the Resize context menu item in Document Container                                 | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MDIRestore                                         | Sets the string for the Restore context menu item in Document Container                                | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MenuItemCancel                                     | Sets the string for the Cancel context menu item in Document Container                                 | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MinimizeRibbon                                     | Sets the string for the MinimizeRibbon context menu item in Ribbon                                     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MinimizeTooltip                                    | Sets the string for the ToolTip of Minimize button in Ribbon Window                                    | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Modify                                             | Sets the string for the Modify button content in Ribbon QAT customization dialog window                | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MoveToNextTabGroup                                 | Sets the string for MoveToNextTabGroup context menu item in Docking Manager and Document Container     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| MoveToPreviousTabGroup                             | Sets the string for MoveToPreviousTabGroup context menu item in Docking Manager and Document Container | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| NewHorizontalTabGroup                              | Sets the string for NewHorizontalTabGroup context menu item in Docking Manager and Document Container  | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| NewTabgroup                                        | Sets the string for NewTabgGroup context menu item in Docking Manager and Document Container           | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| NewVerticalTabGroup                                | Sets the string for NewVerticalTabGroup context menu item in Docking Manager and Document Container    | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| NextText                                           | Sets the string for the Next button content in Wizard control                                          | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Ok                                                 | Sets the string for the OK button content in QAT Customization dialog window in Ribbon                 | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Options                                            | Sets the string for the Options property                                                               | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QAT                                                | Sets the string for Quick Access Toolbar Text in QAT customization dialog window in Ribbon             | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATAllCommandsCaption                              | Sets the string for All Commands Text in the Combo box of QAT customization dialog window in Ribbon    | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATDuplicateAlert                                  | Sets the string for the Duplicate QAT item Alert message in QAT customization dialog window in Ribbon  | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATMoreCommands                                    | Sets the string for More Commands context menu item in QAT dropdown in Ribbon                          | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATResetContent                                    | Sets the string for the Reset QAT message in QAT customization dialog window in Ribbon                 | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATResetTitle                                      | Sets the string for the Reset QAT window Title in QAT customization dialog window in Ribbon            | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATRibbonMenuCaption                               | Sets the string for Ribbon Menu Text in the Combo box of QAT customization dialog window in Ribbon     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATShowAbove                                       | Sets the string for More Commands context menu item in QAT dropdown in Ribbon                          | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATShowBelow                                       | Sets the string for More Commands context menu item in QAT dropdown in Ribbon                          | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| QATTabCaption                                      | Sets the string for Tab Text, which is used in the combo box in Ribbon QAT customization dialog window | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| RemoveFromQAT                                      | Sets the string for Remove from Quick Access Toolbar context menu item in Ribbon                       | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| RemoveItem                                         | Sets the string for Remove button content in Ribbon QAT customization dialog window                    | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Reset                                              | Sets the string for Reset button content in Ribbon QAT customization dialog window                     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| RestoreTooltip                                     | Sets the string for the ToolTip of Restore button in Ribbon Window                                     | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Showfewerbuttons                                   | Sets the string for Group Bar Showfewerbuttons  Menu Item                                              | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Showmorebuttons                                    | Sets the string for Group Bar Showmorebuttons   Menu Item                                              | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ShowQATBelow                                       | Sets the string for Show QAT Below Check box of QAT customization dialog window in Ribbon              | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Tabbed                                             | Sets the string for Tabbed context menu item in Docking Manager                                        | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| TabClose                                           | Sets the string for Close context menu\                                                                | static          | string          |
|                                                    | item in Docking Manager and Document Container                                                         |                 |                 |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| TabCloseAll                                        | Sets the string for CloseAll context menu item in Docking Manager and Document Container               | static          | string          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------+-----------------+


**[]** 

[] 

Table 15: Syncfusion.Shared.Wpf Localization Property Table


  Property                                         Description                                                               Type     Data Type
  ------------------------------------------------ ------------------------------------------------------------------------- -------- -----------
  AccessCalendarText[]    Sets the string for the Calendar Text in DateTimeEdit                     static   string
  AccessClockText[]       Sets the string for the Clock Text in DateTimeEdit                        static   string
  AccessEmptyDateText[]   Sets the string for the Empty Date  Text in DateTimeEdit                  static   string
  AccessTodayText[]       Sets the string for the Today Text in Calendar                            static   string
  AccessWatchText[]       Sets the string for the Watch Text in DateTimeEdit                        static   string
  CloseTooltip[]          Sets the string for the ToolTip of Close button in Chromeless Window      static   string
  MaximizeTooltip[]       Sets the string for the ToolTip of Maximize button in Ribbon Window       static   string
  MinimizeTooltip[]       Sets the string for the ToolTip of Minimize button in Chromeless Window   static   string
  RestoreTooltip[]        Sets the string for the ToolTip of Restore button in Chromeless Window    static   string
  TodayLabel[]            Sets the string for the Today Label in DateTimeEdit                       static   string


 

Adding Localization to an Application

The following steps explain the implementation of Localization support in applications. 

 

Creating an Application

Create a WPF application and add Tools controls.  

 

Creating a Resource File

To create a Resource file:

1.   Create a folder named **Resources** in the application.

2.   Create a resource file (Resx file) and name it Syncfusion.Tools.Wpf\<*your culture info name*\>.resx E.g. Syncfusion.Tools.Wpf.fr-FR.resx

[] 

In case you used Shared dll controls in the applciation, then create one more Resx file Syncfusion.Shared.Wpf\<*your culture info name*\>.resx

Eg: Syncfusion.Shared.Wpf.fr-FR.resx

[] 

Use the prescribed naming convention as it is mandatory. The following screenshot explains the addition of a Resource file to the application.

[] 

{border="0"}

Figure 646: Adding a Resource File to the Application

**[]** 

[] 

3.   Enter the "Name" and "Value" in the Resource file.

The String Property names used in Tools.Wpf controls are given in the Properties table. This is explained in the following screenshot.

{border="0"}

Figure 647: Screenshot of the filled String Resources (Tools.Wpf)

[] 

The String Property names used in Shared.Wpf controls are given in the Properties table. This is explained in the following screenshot.

[] 

[{border="0"}]

Figure 648: Screenshot of the filled String Resources (Shared.Wpf)[]

*[]* 

[] 

Setting the Culture Information in the Application

The culture information should be set in the application before the InitializeComponent() method is called. Now, the application is set to French Culture info. The following code snippet explains the implementation of this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                      |
| [System.Threading.[Thread].CurrentThread.CurrentUICulture =   [new] System.Globalization.[CultureInfo]([\"fr-FR\"]);][ ][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

**[]** 

{border="0"}

Figure 649: Localization Support

 

 

[]{#related-topics}


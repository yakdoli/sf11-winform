---
title: commandbarspackage.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\commandbarspackage.md
created_at: 2025-07-03
---








  









## []CommandBars Package {#commandbars-package style="tab-stops: 0pt"}

 

The Essential Tools **CommandBar** implements a framework for creating and hosting ToolBars, ReBars and StatusBars similar to those that are found in the Visual Studio .NET and Office XP user interfaces.

[] 

The three main classes of the CommandBar framework are **CommandBarController**, **CommandBar** and **ControlBar**.

[] 

[·      ]The **CommandBarController** component serves as a form scope controller for the CommandBar and ControlBar hosted on a form and provides the required design time support and API for creating and working with the CommandBars and ControlBars.

[·              ]

[·      ]A **CommandBar**, similar to the Win32 / MFC ControlBars, is purely a container control that is responsible only for it\'s layout state.

[·              ]

[·      ]A **ControlBar** enables application developers to add dockable / floatable controls to their form\'s toolbar layout. A common example of a ControlBar is the task pane window found in the Microsoft Office 2003 product suite. Refer to the \'Detached ControlBars\' topic under the Menus Package which has explained the ControlBar in detail.

[] 


 Note:


1.   The CommandBar framework should be used directly in an application only when there is no requirement for XP style menus and toolbars. Refer to the Essential Tools Menus Package for implementing XP style menus and toolbars.

 

2.   ReBar controls act as containers for child controls. They contain one or more bands, and each band can have any combination of a gripper bar, a bitmap, a text label, and many more controls. ReBar control is also called as CoolBar. This control is not included in the .NET framework. It is available only in the VB 6.0 and MFC framework.

[] 

 

More:












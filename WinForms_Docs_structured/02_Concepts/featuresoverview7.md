---
title: featuresoverview7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresoverview7.md
created_at: 2025-07-03
---








  









### Features Overview {#features-overview style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

[] 

The TabbedMDI framework contains the TabbedMDIManager control with features to create rich user applications.

[] 

Features

[] 

[·      ]**Styles -** TabbedMDI supports wide range of Tab Styles and Window Styles. Windows in the TabbedMDI framework can be arranged in four different styles such as horizontal, vertical, cascade and inside the client area of the parent form. It also provides advanced features to set the styles for the DropDown Menus and Context Menus.

 

[·      ]**Tab Alignment** - Aligns the Tabs to the Top, Left, Right or Bottom using the Alignment property. To access this property, the TabControlAdded event is used.

[] 

[·      ]**Tab Groups[ ]-** [[Tab Groups]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Tab_Groups) are resizable exactly as in the Visual Studio .NET IDE. The number and layout of the Tab Groups can be restricted and controlled.

 

[·      ]**MDI List** - The list of MDIChild Forms in the application can be retrieved by using a single property. Also the Menu Item or ToolStrip Menu Item to which the list should be added can be specified.

[] 

[·      ]**Button Settings[ - ]**Options to add [[DropDown]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_DropDown_Button) and [[Close buttons]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Close_Button) are available. Close buttons can be displayed individually for each tab. The color of the close button can be set according to the needs of the user. It also provides options to close tabs on clicking the middle button of the mouse.

 

[·      ]**Appearance Settings -[ ]**User Controls, Images and Icons can be added to the Tabs. Options are provided to customize the tab\'s text and image and control the tab\'s image size.

 

Themed tabs can be displayed using the[ ]**ThemesEnabled**[ ]property.

[] 

[·      ]**Context Menu** **[- ]**[[Context Menu]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Context_Menu)[ ]{.UGHyperlink}Items of the Tabs can be customized. Customized Bar Items can be added to the default context menu by accessing the ParentBarItem instance through the **contextMenuItem.Items.Add(baritem)** property.

[] 

[·      ]**Automatic State Persistence -** TabbedMDI provides full state persistence support. The TabbedMDIManager automatically persists Tab Groups and Tab Group Sizes for use across application invocations.

 

[·      ]**Serialization Support** - Provides[ ][[serialization support]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Serialization_support) to save and load the Tab States.

 

[·      ]**Tooltip Support** - Tooltips can be enabled for individual Tabs.

[] 

See Also

**[]** 

[[Concepts and Features]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Concepts_and_Features_8)[, ][[Creating TabbedMDIManager]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Creating_TabbedMDIManager)[]

 

 

 

[]{#p900} 

[]{#related-topics}


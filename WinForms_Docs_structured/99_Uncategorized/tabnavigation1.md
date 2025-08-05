---
title: tabnavigation1.md
original_path: WinForms_Docs/99_Uncategorized/tabnavigation1.md
created_at: 2025-08-05
---








  









### TabNavigation {#tabnavigation style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabControlAdv provides an easy way to navigate through tabs. Setting **TabPrimitives** (previously, NavigationControl) allows the users to move to the next or previous tab / page and easily traverse to the first / last tab.

 

TabPrimitives are more flexible, which provides a [[CloseButton]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_CloseButton_Settings) to close tabs and a DropDown that pops-up with a list of all the available TabPages from which the user can choose from.

 

The Visible property must be set to True to display the tabprimitives added to the control.

 

**SwitchPagesForDialogKeys** property available for the TabControlAdv specifies if the control should switch tabpages on pressing Ctrl+Tab or Ctrl+Shift+Tab.

 

The **TabPrimitiveHost** property allows to customize the navigation and close buttons by defining it through the **TabPrimitives** Property Collection. The tabprimitives can be added and each primitive can be assigned with the type to be used, which includes primitives to traverse to the First / Previous / Next / LastTab, Next / PreviousPage and Close / DropDown options.

[] 

{border="0"}

**[]** 

Figure 1051: TabControls with TabNavigation, PageNavigation, DropDown and Close Primitives

 

 

 

 

[]{#related-topics}


---
title: appearance58.md
original_path: WinForms_Docs/02_Concepts/appearance58.md
created_at: 2025-08-05
---






#### Appearance {#appearance style="tab-stops: 0pt"}

 

This property allows you to control the appearance of the grouping grid at design time as well as at run time. You can change the overall appearance of the grid and also the appearance of each element in the grid by setting this property.

 

**Appearance** contains a list of **GridStyleInfo** properties as seen in the following graphic. A **GridStyleInfo** object contains many properties such as **BackColor**, **Font** and **CellType** which defines the look and behavior of a grid cell. Each of these properties identifies a particular set of cells that make up a Grid Grouping control.

[] 

{border="0"}

**[]** 

*[Figure ][316][: Appearance Properties]*

[] 

To understand exactly what is going on here, let\'s consider three of these GridStyleInfo properties: **AnyCell**, **AnyRecordFieldCell** and **AnyAlternateRecordFieldCell**. Say we set **AnyCell.BackColor** = Color.LightBlue. This will color any grid cell light blue.

[] 


{border="0"}Note:[ ]If you are using a Themed Operating system, like Windows XP, turn the GridGroupingControl.ThemesEnabled property off so that the theme coloring does not affect things like header cell buttons. Otherwise, this will interfere with illustrating the concepts we are trying to communicate in this section.


[] 

Next if we set **AnyRecordFieldCell.BackColor** = Color.Azure, we will see the color of any record field cell change to azure. If we then set **AnyAlternateRecordFieldCell.BackColor** = Color.LightGreen, we will see alternate records being displayed with a green background. Below is a picture illustrating the look of the grid after setting each property in order.

 

There is an inheritance hierarchy that is associated with the **Appearance** properties. The general rule is that, if present, the more specific property takes precedence over the less specific property. This means that AnyCell.BackColor is overridden by setting the AnyRecordFieldCell.BackColor which, is again overridden by setting even more specific AnyAlternatingRecordFieldCell.BackColor.

[] 

{border="0"}

[] 

*[Figure ][317][: Property Inheritance At Work]*

 

[]{#p447} 

 

More:




















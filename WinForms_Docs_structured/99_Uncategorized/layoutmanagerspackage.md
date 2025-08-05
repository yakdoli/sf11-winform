---
title: layoutmanagerspackage.md
original_path: WinForms_Docs/99_Uncategorized/layoutmanagerspackage.md
created_at: 2025-08-05
---








  









## Layout Managers Package {#layout-managers-package style="tab-stops: 0pt"}

[] 

A **Layout Manager** is a component that manages the position of the Child controls in a Parent Container control. Container control is a control on which Child controls are dropped or for which the layout is designed. The Layout Manager sets the location and size of all the components based on a predefined set of constraints.

 

Layout Manager package provides users a comprehensive set of Layout Managers that help to manage advanced layouts on a form and the components will provide all the common layout capabilities for your Containers. The various Layout Managers included are as follows:

 

BorderLayout

[] 

BorderLayout is a Layout Manager which allows arranging and layout the Child controls along the borders and at the center, just like .NET framework\'s built-in docking support.

[] 

CardLayout

[] 

A CardLayout is a Layout Manager that is applied to a Container, and components are added to the layout in a particular form and not between different forms.

[] 

FlowLayout

[] 

FlowLayout is a Layout Manager which allows arranging the Child components horizontally or vertically in a specific order, based on the settings.

[] 

GridLayout

[] 

GridLayout is a Layout Manager that arranges the Child controls in a grid like fashion, containing rows and columns.

[] 

GridBagLayout

[] 

GridBagLayout is a Layout Manager that arranges the Child controls in a virtual grid of rows and columns. But, unlike the GridLayout, the size of the columns and rows can vary and the Child controls may span more than one cell.

[] 

Why Layout Manager?

[] 

When you develop a simple application, you can arrange the controls within a Container control without any helper control, just by arranging them in a particular order. But it will be difficult when you layout a large number of controls in the application. The problem will arise when new controls are added or existing controls are removed, reordered or appearance settings are changed, or any control or form is resized. It will be a real pain to maintain such a layout. In addition, this approach does not provide built-in support for multiple layouts.

[] 

See Also

[] 

More:
















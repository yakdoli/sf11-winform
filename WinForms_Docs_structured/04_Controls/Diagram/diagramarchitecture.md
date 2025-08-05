---
title: diagramarchitecture.md
original_path: WinForms_Docs/04_Controls/Diagram/diagramarchitecture.md
created_at: 2025-08-05
---








  









## Diagram Architecture {#diagram-architecture style="tab-stops: 0pt"}

[] 

The following is a general description about the important classes of Diagram Silverlight. These classes form the base of the control.

[] 

Diagram Control

**\**
The Diagram control is the base class, which contains the view and the model. It receives user input and translates it into actions on the model and view. It also implements symbol palette and scrolling, and enables horizontal and vertical scrollbars when the size of the view exceeds the size of the window.\
\
\

Diagram Model

**\**
A model represents data for an application and contains the logic for adding, accessing, and manipulating the data. Nodes and connectors are added to the Diagram Control using the **Model** property. A predefined layout can be applied using the **LayoutType** property of the DiagramModel, or the position of the nodes can be manually specified.\
\

\
Diagram View

**\**
The view obtains data from the model and presents them to the user. It typically manages the overall layout of the data obtained from the model.\
\
Apart from presenting the data, view also handles navigation between the items, and some aspects of item selection. The views also implements basic user interface features, such as rulers, and drag-and-drop.

\
A view can be constructed without a model, but a model must be provided before it can display useful information. Views can also render additional visual information that does not exist inside the model such as bounding boxes and grids. These additional view-specific objects are referred to as decorators, because they provide additional visual aids and window dressing to the view; but they are not actually a part of the model.\
\
\

Diagram Page

**\**
The DiagramPage is just a container to hold the objects (nodes and connectors) added through the model .The DiagramView uses the page to display the diagram objects. As mentioned before, the view implements several basic user interface features like rulers and grids. Therefore a page is just a container to hold the graphical objects added through the model and the DiagramView uses it to display the objects.

[] 

SymbolPalette:

 

The Symbol Palette control displays node shapes and allows a user to drag and drop symbols onto diagrams. It supports grouping and filtering symbols. It allows users to classify items as groups, so they can be navigated easily. Also, custom shapes can be added to the Symbol Palette.

 

SymbolPaletteGroup:

 

A SymbolPalette group is a collection of SymbolPalette items. It is used to group the items in the SymbolPalette control based on classifications provided. The SymbolPalette group can be added to the SymbolPalette using the SymbolGroups property.

 

SymbolPaletteFilter:

**[]** 

A Symbol Palette filter can be added to the Symbol Palette control, using the **SymbolFilters** property, so that only the desired Symbol Palette groups get displayed.

**[]** 

SymbolPaletteItem:

**[]** 

Symbol Palette items are contained in the Symbol Palette group. A Symbol Palette item does not restrict users to the type of content that can be added to it. A Symbol Palette item can be a text box, combo box, image, button, and so on.

**[]** 

[] 

Horizontal / Vertical Ruler:

[] 

Rulers display the coordinates of elements on the diagram page. At any point, the ruler value always indicates the exact coordinates of the page and its elements.

[] 

{border="0"}

Figure 8: Diagram Page[]

[] 

[]{#related-topics}


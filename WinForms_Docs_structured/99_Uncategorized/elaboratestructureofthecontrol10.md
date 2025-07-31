---
title: elaboratestructureofthecontrol10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\elaboratestructureofthecontrol10.md
created_at: 2025-07-03
---








  









## Elaborate Structure Of the Control {#elaborate-structure-of-the-control style="tab-stops: 0pt"}

[] 

The controls associated with the Essential Diagram are illustrated in the below image.

[] 

{border="0"}

[] 

Figure 5: Diagram Windows Controls

[] 

Document Explorer

[] 

Document Explorer control allows you to visualize the details of the various objects that are added onto the diagram control at run-time. The layers will be listed under the Layers node and other objects like shapes, links, lines and text editor will be listed under Nodes node.

[] 

Overview Control

[] 

Overview Control provides a perspective view of a diagram model, and allows users to dynamically pan and zoom diagrams. The Overview Control facilitates a perspective view of the diagram. The control features a viewport window that can be moved and / or resized using the mouse to modify the diagrams\' origin and magnification properties at run-time.

[] 

The features of this control are demonstrated in one of our installation samples which is available in the following location.

[] 

**..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Diagram.Windows\\Samples\\2.0\\Getting Started\\OverView**

[] 

Property Editor

[] 

The Property Editor in Essential Diagram displays properties of the currently selected object or objects in the diagram. It is a Windows Forms control that can be added to the Visual Studio .NET Toolbox. It also allows users to set or modify the various properties of the objects or the model. The Property Editor provides an easy interface to set and view the various property settings.

[] 

Palette GroupBar and GroupView

[] 

The **PaletteGroupBar** control provides a way for users to drag and drop symbols onto a diagram. It is based on the Syncfusion Essential Tools GroupBar control. Each symbol palette loaded in the PaletteGroupBar occupies a panel that can be selected by a bar button. The bar button is labeled with the name of the symbol palette. The symbols in the palette are shown as icons that can be dragged and dropped onto the diagram. This control allows users to add symbols to a palette, and save or load the palette whenever necessary. It provides a way to classify and maintain symbols.

[] 

The **PaletteGroupView** control provides an easy way to serialize a symbol palette to and from the resource file of a form. At design-time, users can attach a symbol palette to a PaletteGroupView control in the form. Selecting the PaletteGroupView and clicking the **Palette** property in the Visual Studio .NET Properties window will open a standard Open File dialog, which allows the user to select a symbol palette file that has been created with the Symbol Designer.

[] 


{border="0"}[Note][:][ ]The properties of these diagram controls are discussed in the Supported Controls topic.


 

[]{#p12} 

[] 

[]{#related-topics}


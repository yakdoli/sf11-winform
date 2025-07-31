---
title: featuresummary1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresummary1.md
created_at: 2025-07-03
---








  









## Feature Summary[] {#feature-summary style="tab-stops: 0pt"}

[] 

The important features of Essential Diagram are listed below.

[] 

[·      ]Retained-mode interface for 2D interactive graphics.

[·      ]Hierarchical node structure supporting nesting.

[·      ]Clearly separates data, presentation and user interaction into separate models, views and controller components.

[·      ]Supports extending model, view and controller components.

[·      ]Provides mix and match model, view and controller components for custom functionality.

[·      ]Supports Matrix Transformations: Translate (Move), Rotate and Scale.

[·      ]Shape nodes are the graphical objects that can be drawn onto the diagram area by activating one of several drawing tools such as the RectangleTool, RoundRectTool, EllipseTool, LineTool, PolylineTool, OrthogonallineTool, BezierTool, CurveTool, ArcTool and PolygonTool.

[·      ]DecoratorShape can be added at the head and tail of Connectors. The shapes include arrows, circles, diamonds, crosses, squares and custom decorators.

[·      ]**Diagram Export**: Essential Diagram offers capabilities to export the diagram representation into various formats. The formats include Bitmaps with support for multiple formats, enhanced metafiles and SVG files.

[·      ]**Text Nodes**: Essential Diagram supports rendering Textnodes and RichTextnodes, and offers full text formatting through sufficient properties.

[·      ]Text editing and text rotation are also supported.

[·      ]Group[ ]nodes[ ]are the Containers for child nodes and are extended with text labels.

[·      ]Link nodes are directional symbols with two connection ports.

[·      ]Command Architecture provides Undo / Redo operations with Macro commands.

[·      ]Grouping / UnGrouping of nodes can be supported by sufficient APIs.

[·      ]Layer is a collection of nodes that share a common set of default properties and the same Z-order relative to other layers.

[·      ]Hit testing is supported.

[·      ]**Coordinate Conversion**: a view is set inside a window and has bounds that are measured in device coordinates

[·      ]Essential Diagram renders the node in coordinates that are apt to the Model coordinates through Matrix conversions. Several methods are available to achieve the required coordinate conversions.

[·      ]Zooming, scrolling, and panning are supported and can be achieved using sufficient interactive diagram tools.

[·      ]**Grid**: the drawing area of the Diagram control can be rendered with Grid lines or points and the nodes drawn could also be snapped to Grid.

[·      ]**Units**: Real-world logical units (e.g. Metric units, English units).

[·      ]**Automatic Line Routing and Line Bridging**: while a link is drawn between two nodes by enabling the LineRoutingEnabled property of that link and the diagram view, if any other node is found in between them, the line will be automatically re-routed around those nodes

[·      ]Enabling the LineBridging property, will make the links jump over as per their Z-order priority.

[·      ]**Editing Line Segments**: the line segments between the lines can be edited interactively.

[·      ]**Print and Print Preview**: the PrintDialog class enables the user to set the printer to be used, and allows to define the pages and the number of copies that should be printed, while the PrintPreviewDialog class provides an overview of the document, i.e., of the appearance as to how the document will appear when printed which is shown or invoked by using the ShowDialog method.

[·      ]**Headers and Footers**: Essential Diagram features support for the addition of culture specific headers and footers for a diagram.

[·      ]PaletteGroupBar[ ]control is a WinForm control that can be added to the Visual Studio .NET toolbox, displays list symbols in a symbol palette as icons, allows user to drag symbols onto diagrams, supports multiple symbol palettes at a time, has a user interface similar to Microsoft Outlook bar, and it is implemented based on the Syncfusion GroupBar and GroupView controls.

[·      ]PropertyEditor[ ]control is a WinForm control that can be added to the Visual Studio .NET toolbox, allows users to view and edit the properties of one or more nodes in a diagram, and it is implemented based on the Microsoft .NET PropertyGrid control.

[·      ]Symbol Designer is a utility for creating palettes of symbols and highly advanced symbols.

[·      ]The control is known for its best features of being highly customizable and extensible. Customization has been made easier, and custom UI tools can be easily created and registered.

[·      ]Visio-Like symbol creation is supported by importing Visio stencil files (\*.vss files).

[·      ]Layout Managers define the base class for creating custom layout managers that enable the positioning of diagram nodes and abstracting the layout algorithm from the rest of the diagram data.

[·      ]Built-in serialization support for loading and saving diagrams.

[·      ]Diagram interactivity through Client-Side Image Maps, JavaScript and Server-Side events.

[·      ]Session State Management used to maintain the values that need to be persisted for the duration of a user\'s session.

[·      ]View State Management persists the state across the postback calls.

[·      ]Essential Diagram for ASP.NET integrates AJAX technology to a deeper level, and allows for optimized transfers between the client and server to provide a smooth interaction experience when loading a large set of nodes into the Diagram.

[·      ]Client-Side Node Interaction: you can get the diagram node information easily through client-side scripting.

[·      ]Also, there is improved selection behavior of irregular shapes by optimizing the hit-test algorithm on the client-side. Selected Nodes list can also be accessed through the client-side script.

[]{#related-topics}


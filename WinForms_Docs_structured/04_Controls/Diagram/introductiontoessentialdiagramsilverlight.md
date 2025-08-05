---
title: introductiontoessentialdiagramsilverlight.md
original_path: WinForms_Docs/04_Controls/Diagram/introductiontoessentialdiagramsilverlight.md
created_at: 2025-08-05
---








  









## Introduction to Essential Diagram Silverlight {#introduction-to-essential-diagram-silverlight style="tab-stops: 0pt"}

Essential Diagram Silverlight is an extensible and high-performance diagramming framework for Silverlight applications. It can be used by the developers who want to develop Microsoft Visio-like interactive graphics and diagramming applications. It stores graphical objects in a node graph and renders those objects on the screen. 

 

*** ***A node graph is a structure consisting of nodes connected to each other by lines referred to as edges.

 

Essential Diagram supports both vector and raster graphics on the drawing surface.

****** A raster (bitmap) image uses a grid of individual pixels where each pixel can be a different color or shade. Bitmaps are composed of pixels.

Vector graphics use mathematical relationships between points and the paths connecting them to describe an image. Vector graphics are composed of paths.

 

Essential Diagram Silverlight lets the user to create interactive diagrams easily. 

 

Real World Scenarios

[] 

Essential Diagram Silverlight finds its application in various fields; some of them are listed below:

[] 

[·      ]Essential Diagram Silverlight can be effectively used to create process flow diagrams and flow charts. The connectors with a label depict the process flow from one level to another.

 



Figure 1: Flow Chart[]

[] 

[·      ]Essential Diagram Silverlight employs automatic layout algorithms to layout the nodes automatically in a tree structure. This kind of setting is typically useful in creating Organizational Layout and for data binding purposes.

[] 



Figure 2: Organizational Layout[]

[] 

[·      ]Essential Diagram Silverlight allows the user to create Swim lane diagrams, which groups a set of sub processes in a visual manner, by arranging them in lanes. Nodes can be manually placed to create swim lanes.The process in each lane may then be described using the nodes and the flow can be depicted using the connections as illustrated in the following diagram.

[] 



Figure 3: Swin Lane Diagram[]

[] 

[·      ]Essential Diagram Silverlight allows creating a Data Flow Diagram (DFD), which is a graphical representation of the \"flow\" of data through an information system. DFDs can also be used for the visualization of data processing

[] 



Figure 4: Data Flow Diagram[]

***[]*** 

[] 

Key Features

[] 

The following are the key features of Essential Diagram Silverlight:

[] 

[·      ]**Nodes -** Nodes are graphical objects that can be drawn on the page by selecting them from the Symbol Palette and dropping them on the page.

[] 

[·      ]**Transformations** - The following transformations are provided:

[·    ]Translate: Ability to move the nodes.

[·    ]Rotate: Ability to rotate the nodes.

[·    ]Scale: Ability to resize the nodes.

 

[·      ]**Groups and Ungroup -** Essential Diagram Silverlight provides support to group and ungroup nodes. The Grouping feature comes in handy when you want to apply the same edits to a number of objects and yet retain their individuality. All the operations performed on the group also affect the individual items in the group. However any item in the group can also be edited individually. On ungrouping, the items in the group again act as individual entities.

[] 

[·      ]**Connectors -** Connectors are the objects that are used to create a link between two nodes. Three types of connectors provided are as follows:

[·      ]Orthogonal

[·      ]Bezier

[·      ]Straight**\
\**

[·      ]**Custom Ports -** Essential Diagram Silverlight provides the ability to define custom ports for making connections. The **ConnectionPort** class can be used for defining custom ports on the nodes. Any number of ports can be defined on a node. The user can define a port on any part of the node and make connection to that port. The port\'s visibility can also be controlled. Several customizable properties have been provided for the port.

 

[·      ]**Decorator Shapes -** Decorator shapes can be added to the head and tail of the connectors. Three types of decorator shapes provided are as follows:

[·      ]Arrow

[·      ]Diamond

[·      ]Circle

 

[·      ]**Rulers -** Horizontal and vertical rulers are provided to indicate the coordinates of the mouse position with respect to the view.

 

[·      ]**Symbol Palette -** The Symbol Palette control displays the node shapes and allows a user to drag the symbols onto the diagram. It supports grouping and filtering of symbols, and it is implemented based on the Syncfusion\'s Gallery control. Also, custom shapes can be added to the Symbol Palette.

 

[·      ]**Label Editor -** A label editor is provided for each node and connector. It enables the user to edit labels at run time if **IsLabelEditable** property is set to true for the corresponding object.

 

[·      ]**Customizable -** The control is highly customizable and extensible. Customization is easy, and custom UI tools can be easily created and registered.

 

[·      ]**Automatic Layout Management -** Essential Diagram Silverlight provides the ability to set automatic layout the nodes. Several layout types have been provided. They are:

[] 

[·      ]**DirectedTree Layout** - The DirectedTree layout arranges nodes in a tree-like structure. This layout can be applied to any diagram that is composed of a directed tree graph with unique root and child nodes.

[] 

[·      ]**HierarchicalTree Layout** - The HierarchicalTree layout also arranges nodes in a tree-like structure; however, unlike the directed tree layout, the nodes in hierarchical layout may have multiple parents thereby avoiding the need to specify the root.

 

[·      ]**RadialTree Layout -** The Radial Tree Layout Manager is a specialization of the Directed Tree Layout Manager that employs a circular layout algorithm for locating the diagram nodes. The RadialTreeLayoutManager arranges nodes in a circular layout, positioning the root node at the center of the graph and the child nodes in a circular fashion around the root. Sub-trees formed by the branching of child nodes are located radially around the child nodes. This arrangement results in an ever-expanding concentric arrangement with radial proximity to the root node indicating the node level in the hierarchy.

 

[·      ]**Table Layout** - The Table layout arranges the nodes in a tabular structure based on specified intervals between them. The layout depends upon the number of nodes in each row and column specified. The nodes are assigned rows and columns based on the order in which they are added to the model and based on the maximum nodes allowed in that row and column.

 

**Serialization -** The Diagram Page can be saved in XAML format for future use. The user can then load the saved page into the current view and start editing the page.

**[]** 

User Guide Organization

**[]** 

The product comes with numerous samples as well as an extensive documentation to guide you. This User Guide provides detailed information on the features and functionalities of the Essential Diagram for Silverlight. It is organized into the following sections:

[·      ]**Overview**-This section gives a brief introduction to the product and its key features.

[·      ]**Installation and Deployment**-This section elaborates on the install location of the samples, license and so on.

[·      ]**What\'s New**-This section lists the new features implemented for every release.

[·      ]**Getting Started**-This section guides you on getting started with Silverlight application, controls and so on.

[·      ]**Concepts and Features**-The features of individual controls are illustrated with use case scenarios, code examples and screen shots under this section.

[] 

Document Conventions[ ]

The conventions below will help you to quickly identify the important sections of information, while using the content:

[] 


  ------------------------ ------------------------------------------------------------------------------ --------------------------------------------------------------------------------
  Convention               Icon                                                                           Description of the Icon
  Note                      ***Note:***                                       Represents important information.
  Example                  **Example:**                                                                   Represents an example.
  Tip                                                                         Represents useful hints that will help you in using the controls and features.
  Additional information      Represents additional information on the corresponding topic.
  ------------------------ ------------------------------------------------------------------------------ --------------------------------------------------------------------------------


[] 

[]{#related-topics}


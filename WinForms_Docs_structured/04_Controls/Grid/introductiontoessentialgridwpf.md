---
title: introductiontoessentialgridwpf.md
original_path: WinForms_Docs/04_Controls/Grid/introductiontoessentialgridwpf.md
created_at: 2025-08-05
---








  









## Introduction to Essential Grid WPF {#introduction-to-essential-grid-wpf style="tab-stops: 0pt"}

[] 

The grid at its core functions as a very efficient display engine for tabular data that can be customized down to the cell level. It does not make any assumptions on the structure of the data (many grid controls implemented as straight data bound controls make such explicit assumptions). This leads to a very flexible design that can be easily adapted to a variety of tasks including the display of completely unstructured data and the display of structured data from a database.

 

The display system also hosts powerful and complete styles architecture. Settings can be specified at the cell level or at higher levels using parent styles that are referred to as base styles. Base styles can affect groups of cells. Cell level settings override any higher level settings and enable easy customization right down to that level.

 

With this version, our core focus has been on the underlying architecture for displaying cells with virtualized cell editors in a manner that enables good performance characteristics. The core display system also supports several building block features such as nested grids, virtual mode and support for a virtually unlimited number of rows and columns.

[] 

Real World Scenarios

Essential Grid WPF finds its application in various fields such as finance, banking, software, etc. Some of the important areas are:

Excel-like UI---Rich feature set of Essential Grid allows the users to build feature-rich applications. Below image illustrates an example of an Excel-like UI.

 



Figure 1: Excel-like UI

 

[·      ]Stock Portfolio---Using Essential Grid Control in high performance applications is very much beneficial as it can display large amount of real time data that tends to change periodically, without any performance hits. Below is an illustration of Stock Portfolio using essential grid.

[] 



Figure 2:  Stock portfolio

[] 

[·      ]File Explorer---The GridTree control can be used for file explorer-type applications where the child items should be loaded on demand when the user opens the corresponding parent item.

[] 



Figure 3:  File Explorer

Key Features

The following are the key features of Essential Grid WPF:

[·      ]Easy APIs to add/delete/move row and columns - You can easily add, delete and move rows and columns throughout the grid control using its well-defined APIs.

[·      ]Clipboard Support - Grid provides excellent clipboard support that allows the users to copy/paste grid cells into text or any format.

[·      ]Frozen Row and Column Footers - Grid allows the user to freeze grid columns to the left and also allows to freeze rows to the top of the grid.

[·      ]Resize Rows and Columns - Grid provides option for resizing the rows and columns.

[·      ]Hide Rows and Columns - The grid provides support to hide or unhide a range of rows and columns.

[·      ]Keyboard Interface - Essential Grid provides extensive support for keyboard handling. The following are some of them-

[o  ]Arrow keys-move current cell

[o  ]PageUp/PageDown key-scroll grid by page

[o  ]F2-activate/deactivate cell

[o  ]F4+ALT-Drop-Down/Close-Up cell

[o  ]CTRL + Arrow keys-move to first/last, row/column

[o  ]SHIFT + Arrow keys-select cell

[o  ]DELETE key-delete cell

[o  ]CTRL+X, CTRL+V, CTRL+C, INSERT key and DELETE key support common clipboard operations

**[]** 

All keyboard operations can be customized.

[·      ]Selection Modes - Essential Grid offers different kinds of selection modes such as RowOnly, ColumnOnly and CellOnly for the selection of a particular row, column and a cell respectively.

[·      ]Drag-Drop Support - Essential Grid allows you to drag any column and drop it at any position in the grid. This allows repositioning of columns at the required place.

[·      ]Virtual Mode - Essential Grid for WPF supports a virtual mode, which lets you dynamically provide data to the grid from an external data source through an event. This means that the grid does not store any data in its internal data structure.

[] 

User Guide Organization

The product comes with numerous samples as well as an extensive documentation to guide you. This User Guide provides detailed information on the features and functionalities of the Essential Grid for WPF. It is organized into the following sections:

[·      ]Overview-This section gives a brief introduction to the product and its key features.

[·      ]Installation and Deployment-This section elaborates on the install location of the samples, license etc.

[·      ]What\'s New-This section lists the new features implemented for every release.

[·      ]Getting Started-This section guides you on getting started with WPF application, controls etc.

[·      ]Grid WPF Controls-The features of individual controls are illustrated with use case scenarios, code examples and screen shots under this section.

[] 

Document Conventions

The conventions below will help you to quickly identify the important sections of information, while using the content:

**[]** 

Table 1: Document Convention


  ------------------------ ------------------------------------------ ---------------------------------------------------------------------------------
  Convention               Icon                                       Description of the Icon
  Note                      *****Note:*   Represents important information.
  Example                  Example:                                   Represents an example.
  Tip                      ****           Represents useful hints, that will help you in using the controls and features.
  Additional information   ****           Represents additional information on the corresponding topic.
  ------------------------ ------------------------------------------ ---------------------------------------------------------------------------------


[]{#related-topics}


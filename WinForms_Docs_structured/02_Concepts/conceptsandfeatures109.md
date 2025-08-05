---
title: conceptsandfeatures109.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures109.md
created_at: 2025-08-05
---








  






[ \> ]{.d2h_breadcrumbsLinkSeparator}[Essential HTML UI]{.d2h_breadcrumbsContentsOnly}


# Concepts And Features {#concepts-and-features style="tab-stops: 0pt"}

 

The HTMLUIControl is the main control of the HTMLUI library. The control exposes several properties, methods and events to load, display and interact with rich HTML-based user interfaces.

[] 

Creating the HTMLUI Control

[] 

The HTMLUI control can be created by dragging it from the Visual Studio .NET toolbox, just like any other Windows Forms control.

The following code snippet illustrates how to create a HTMLUIControl programmatically.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [// Initialize a HTMLUIControl.]                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| [this][.htmluiControl1 = [new] Syncfusion.Windows.Forms.HTMLUI.[HTMLUIControl]();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Important Properties

[] 

The following properties help you to get started with the HTMLUIControl.

[] 


  ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property          Description
  StartupDocument   This is the path to the HTML document that will be loaded when the HTMLUIControl is called. Using this property to set a document is the simplest means to load an HTML document.
  Text              The HTMLUIControl does not display the Text property as text. This is the HTML that will be rendered as in the HTMLUIControl. This is the equivalent of the View Source option in a traditional web browser.
  Document          This property provides access to all the display HTML elements programmatically.
  ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

Important Methods

[] 

The following methods help you to get started with the HTMLUIControl.

[] 


  ---------- --------------------------------------------------------------------------------
  Method     Description
  LoadHTML   This method is used to load the HTML document.
  LoadCSS    This method is used to load CSS styles from file and refresh current document.
  ---------- --------------------------------------------------------------------------------


[] 

More:


















































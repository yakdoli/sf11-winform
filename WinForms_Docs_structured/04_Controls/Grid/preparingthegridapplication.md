---
title: preparingthegridapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\preparingthegridapplication.md
created_at: 2025-07-03
---








  









### Preparing the Grid Application {#preparing-the-grid-application style="tab-stops: 0pt"}

[] 

To prepare the Grid Application:

1.   Syncfusion.VisualStudio.TestTools.UITest.GridCommunication.dll contains implementation to easily change an existing application to the test application that the plugin would require.

2.   Let the parent container inherit **GridControlTestApplication** class as shown below:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ][]                                                                                       |
|                                                                                                                                                                                                                     |
| [public][ [class] [Form1] : [GridControlTestApplication]] |
|                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ][]                                   |
|                                                                                                                                                                 |
| [Public][ [Class] [Form1]]    |
|                                                                                                                                                                 |
| [            [Inherits] [GridControlTestApplication]]                          |
|                                                                                                                                                                 |
| [End][ [Class]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application to make it ready for testing.

[]{#related-topics}


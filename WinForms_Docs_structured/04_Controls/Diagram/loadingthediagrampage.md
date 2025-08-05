---
title: loadingthediagrampage.md
original_path: WinForms_Docs/04_Controls/Diagram/loadingthediagrampage.md
created_at: 2025-08-05
---








  









### Loading the Diagram Page {#loading-the-diagram-page style="tab-stops: 0pt"}

[] 

The Load operation can be done in three ways:

[·      ]

[·      ]Using the Load Dialog Box.

[·      ]File name with full path.

[·      ]Using Memory Stream

[] 

Loading using the Load Dialog Box.

**[]** 

To load the page, the following code can be used:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [DiagramControl][ dc = [new] [DiagramControl]();] |
|                                                                                                                                                                                        |
| [dc.Load();]                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [Dim][ dc [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                 |
| [dc.Load()][]                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

1.   The Load Dialog box will appear. Select the \'Files of Type\' as XAML and specify the path of the file to be loaded

2.   Click the Open button in the dialog box.

The selected page gets loaded in the current view and the page is ready to be edited.

 

{border="0"}

Figure 159: Load Dialog Box[]

File name with path[]

[] 

The user can also specify the name of the file directly in the Load method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [DiagramControl][ dc = [new] [DiagramControl]();] |
|                                                                                                                                                                                        |
| [dc.Load([@\"C:\\TestPage.xaml\"]);]                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [Dim][ dc [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                 |
| [dc.Load(\"C:\\TestPage.xaml\")][]                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Essential Diagram Silverlight does not support serializing bindings and bitmap Images.


[] 

Loading from a stream

[] 

The user can also load from a stream.

 

To load from the stream, use the following code snippet.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
| **[]**                                                                 |
|                                                                                                                          |
| [stream.Position = 0;]                                                               |
|                                                                                                                          |
| [dc.Load(stream [as] System.IO.[Stream]);] |
+--------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                         |
|                                                                                                                        |
| **[]**                                                               |
|                                                                                                                        |
| [stream.Position = 0]                                                              |
|                                                                                                                        |
| [dc.Load(TryCast(stream, System.IO.Stream))][] |
+------------------------------------------------------------------------------------------------------------------------+

 


 {border="0"}Note: While loading from memory stream, please make sure the stream's Position property is set to 0.


[]{#related-topics}


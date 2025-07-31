---
title: howtoloadnodesfromanedpfile.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoloadnodesfromanedpfile.md
created_at: 2025-07-03
---








  









## How to load nodes from an EDP file?[] {#how-to-load-nodes-from-an-edp-file style="tab-stops: 0pt"}

[] 

We must deserialize an EDP file for this purpose. Then, the function returns a SymbolPalette from the file (filename -- path to file).

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [// Get the SymbolPalette by deserializing the SymbolPalette file.]                                                                    |
|                                                                                                                                                                                          |
| [public][ [SymbolPalette] LoadPalette([string] filename)] |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [   [SymbolPalette] curSymbolPalette = [null];]                                                            |
|                                                                                                                                                                                          |
| [   FileStream iStream = [new] FileStream(filename, FileMode.Open, FileAccess.Read);]                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [   [if] (iStream != [null])]                                                                              |
|                                                                                                                                                                                          |
| [   {]                                                                                                                                               |
|                                                                                                                                                                                          |
| [      IFormatter formatter = [new] BinaryFormatter();]                                                                         |
|                                                                                                                                                                                          |
| [      [try]]                                                                                                                   |
|                                                                                                                                                                                          |
| [      {]                                                                                                                                            |
|                                                                                                                                                                                          |
| [         curSymbolPalette = ([SymbolPalette])formatter.Deserialize(iStream);]                                                  |
|                                                                                                                                                                                          |
| [      }]                                                                                                                                            |
|                                                                                                                                                                                          |
| [      [catch] (SerializationException)]                                                                                        |
|                                                                                                                                                                                          |
| [      {]                                                                                                                                            |
|                                                                                                                                                                                          |
| [         [try]]                                                                                                                |
|                                                                                                                                                                                          |
| [         {]                                                                                                                                         |
|                                                                                                                                                                                          |
| [            formatter = [new] SoapFormatter();]                                                                                |
|                                                                                                                                                                                          |
| [            iStream.Position = 0;]                                                                                                                  |
|                                                                                                                                                                                          |
| [            curSymbolPalette = ([SymbolPalette])formatter.Deserialize(iStream);]                                               |
|                                                                                                                                                                                          |
| [         }]                                                                                                                                         |
|                                                                                                                                                                                          |
| [         [catch] ([Exception] e)]                                                                         |
|                                                                                                                                                                                          |
| [         {]                                                                                                                                         |
|                                                                                                                                                                                          |
| [            System.Diagnostics.[Trace].WriteLine([\"Error reading SymbolPalette\"], e.Message);]        |
|                                                                                                                                                                                          |
| [         }]                                                                                                                                         |
|                                                                                                                                                                                          |
| [      }]                                                                                                                                            |
|                                                                                                                                                                                          |
| [      [finally]]                                                                                                               |
|                                                                                                                                                                                          |
| [      {]                                                                                                                                            |
|                                                                                                                                                                                          |
| [         iStream.Close();]                                                                                                                          |
|                                                                                                                                                                                          |
| [      }]                                                                                                                                            |
|                                                                                                                                                                                          |
| [   }]                                                                                                                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [   [return] curSymbolPalette;]                                                                                                 |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                  |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Example]                                                                                                                           |
|                                                                                                                                                                                          |
| [string][ palettepath = Server.MapPath([string].Empty);]                       |
|                                                                                                                                                                                          |
| [palettepath = palettepath + [@\"\\App_Data\\SamplePalette.edp\"];]                                                           |
|                                                                                                                                                                                          |
| [SymbolPalette][ palette = LoadPalette(palettepath);]                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| [\' Get the SymbolPalette by deserializing the SymbolPalette file.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [Public][ [Function] LoadPalette([ByVal] filename [As] [String]) [As] Syncfusion.Windows.Forms.Diagram.SymbolPalette] |
|                                                                                                                                                                                                                                                                                                                     |
| [        [Dim] curSymbolPalette [As] Syncfusion.Windows.Forms.Diagram.SymbolPalette = [Nothing]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                     |
| [        [Dim] iStream [As] [New] IO.FileStream(filename, FileMode.Open, FileAccess.Read)]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [        [If] iStream [IsNot] [Nothing] [Then]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [            [Dim] formatter [As] Runtime.Serialization.IFormatter = [New] Runtime.Serialization.Formatters.Binary.BinaryFormatter()]                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [            [Try]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [                curSymbolPalette = [DirectCast](formatter.Deserialize(iStream), Syncfusion.Windows.Forms.Diagram.SymbolPalette)]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| [            [Catch] generatedExceptionName [As] Runtime.Serialization.SerializationException]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [                [Try]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| [                    formatter = [New] Runtime.Serialization.Formatters.Soap.SoapFormatter()]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [                    iStream.Position = 0]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| [                    curSymbolPalette = [DirectCast](formatter.Deserialize(iStream), Syncfusion.Windows.Forms.Diagram.SymbolPalette)]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| [                [Catch] e [As] Exception]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                     |
| [                    System.Diagnostics.Trace.WriteLine([\"Error reading SymbolPalette\"], e.Message)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                     |
| [                [End] [Try]]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                     |
| [            [Finally]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| [                iStream.Close()]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [            [End] [Try]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                     |
| [        [End] [If]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                     |
| [        [Return] curSymbolPalette]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [End][ [Function]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                     |
| [    [\' Example]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                     |
| [Dim][ palettepath [As] [String] = Server.MapPath([String].Empty)]                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [palettepath = palettepath + [\"\\App_Data\\SamplePalette.edp\"] ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [Dim][ palette [As] Syncfusion.Windows.Forms.Diagram.SymbolPalette = LoadPalette(palettepath)]                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

At this moment, we have the palette (SymbolPalette). To get nodes from the palette and insert it into the document, use the below code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [foreach][ ([Node] node [in] palette.Nodes)] |
|                                                                                                                                                                             |
| [{]                                                                                                                                     |
|                                                                                                                                                                             |
| [      [Node] nodeToInsert = ([Node])node.Clone();]                                           |
|                                                                                                                                                                             |
| [      DiagramWebControl1.Model.AppendChild(nodeToInsert);]                                                                             |
|                                                                                                                                                                             |
| [}]                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [For][ [Each] node [As] Node [In] palette.Nodes ]                                      |
|                                                                                                                                                                                                                                            |
| [    [Dim] nodeToInsert [As] Syncfusion.Windows.Forms.Diagram.Node = [DirectCast](node.Clone(), Syncfusion.Windows.Forms.Diagram.Node)] |
|                                                                                                                                                                                                                                            |
| [    DiagramWebControl1.Model.AppendChild(nodeToInsert) ]                                                                                                                                              |
|                                                                                                                                                                                                                                            |
| [Next]                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}


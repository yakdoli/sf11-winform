---
title: howtozipfilesusingthesyncfusioncompressionzipnamespace.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtozipfilesusingthesyncfusioncompressionzipnamespace.md
created_at: 2025-07-03
---








  









### How to zip files using the Syncfusion.Compression.Zip namespace? {#how-to-zip-files-using-the-syncfusion.compression.zip-namespace style="tab-stops: 0pt"}

 

You can use the AddFile method of ZipArchive object to compress files by using XlsIO. Following code example illustrates how to use this method.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [Syncfusion.Compression.Zip.[ZipArchive] zipArchive = [new] Syncfusion.Compression.Zip.[ZipArchive]();] |
|                                                                                                                                                                                                            |
| [zipArchive.DefaultCompressionLevel = Syncfusion.Compression.[CompressionLevel].Best;]                                                            |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [// Add the file you want to zip.]                                                                                                                       |
|                                                                                                                                                                                                            |
| [zipArchive.AddFile([\"..\\..Form1.cs\"]);]                                                                                                     |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [// Zip file name and location.]                                                                                                                         |
|                                                                                                                                                                                                            |
| [zipArchive.Save([\"SyncfusionCompressFileSample.zip\"]);]                                                                                      |
|                                                                                                                                                                                                            |
| [zipArchive.Close();]                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [Dim][ zipArchive [As] [New] Syncfusion.Compression.Zip.ZipArchive()] |
|                                                                                                                                                                                                      |
| [zipArchive.DefaultCompressionLevel = Syncfusion.Compression.CompressionLevel.Best ]                                                                             |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [\' Add the file you want to zip.]                                                                                                                 |
|                                                                                                                                                                                                      |
| [zipArchive.AddFile([\"..\\..Form1.cs\"])]                                                                                                |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [\' Zip file name and location.]                                                                                                                   |
|                                                                                                                                                                                                      |
| [zipArchive.Save([\"SyncfusionCompressFileSample.zip\"])]                                                                                 |
|                                                                                                                                                                                                      |
| [zipArchive.Close()]                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

For compressing directories, you can make use of the **AddDirectory** method. The AddDirectory method adds an empty directory file to a ZipArchive. If you want to add all the files inside the directory, then you should manually add these files by using the **AddItem** method.\
\
For example, you can use the following code to add the file from the local drive.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [string][ fileName = [@\"C:\\Form1.cs\"];]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [Syncfusion.Compression.Zip.[ZipArchive] zipArchive = [new] Syncfusion.Compression.Zip.[ZipArchive]();]                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [zipArchive.DefaultCompressionLevel = Syncfusion.Compression.[CompressionLevel].Best;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [Stream stream = [new] FileStream(fileName, FileMode.Open, FileAccess.Read);]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [FileAttributes attributes = File.GetAttributes(fileName);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [Syncfusion.Compression.Zip.[ZipArchiveItem] item = [new] Syncfusion.Compression.Zip.[ZipArchiveItem]([\"Form1.cs\"], stream, [true], attributes);] |
|                                                                                                                                                                                                                                                                                                    |
| [zipArchive.AddItem(item);]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [zipArchive.Save([@\"c:\\\\SyncfusionCompressFileSample.zip\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                    |
| [zipArchive.Close();]                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Dim][ fileName [As] [String] = [\"C:\\Form1.cs\"]]                                                                                |
|                                                                                                                                                                                                                                                                                          |
| [Dim][ zipArchive [As] [New] Syncfusion.Compression.Zip.ZipArchive()]                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [zipArchive.DefaultCompressionLevel = Syncfusion.Compression.CompressionLevel.Best ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [Dim][ stream [As] IO.Stream = [New] IO.FileStream(fileName, FileMode.Open, FileAccess.Read)]                                                             |
|                                                                                                                                                                                                                                                                                          |
| [Dim][ attributes [As] IO.FileAttributes = File.GetAttributes(fileName)]                                                                                                       |
|                                                                                                                                                                                                                                                                                          |
| [Dim][ item [As] [New] Syncfusion.Compression.Zip.ZipArchiveItem([\"Form1.cs\"], stream, [True], attributes)] |
|                                                                                                                                                                                                                                                                                          |
| [zipArchive.AddItem(item) ]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                          |
| [zipArchive.Save([\"c:\\\\SyncfusionCompressFileSample.zip\"]) ]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| [zipArchive.Close()]                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}


---
title: saveloadthebarinformation.md
original_path: WinForms_Docs/99_Uncategorized/saveloadthebarinformation.md
created_at: 2025-08-05
---






##### Save / Load the Bar Information {#save-load-the-bar-information style="tab-stops: 0pt"}

[] 

ToolBar Persistence can be done by using the below given properties and methods.

**[]** 


  ------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  MainFrameBarManager Property   Description
  AutoLoadToolBarPositions       Indicates whether to automatically load the persisted toolbar positions when the application is restarted.
  AutoPersistCustomization       Indicates whether to persist and load user-customized info from/to isolated storage.
  AutoSaveCustomData             Gets or Sets a value indicating whether to automatically save user\'s customization data (new Bars/BarItems added/removed at runtime), when customization target form is closed.
  AutoLoadCustomData             Gets or Sets a value indicating whether to automatically load user\'s customization data (new Bars/BarItems added/removed at runtime), when customization target form is activating.
  ------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 


  ----------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  MainFrameBarManager Methods   Description
  SaveBarState                  Saves the current toolbars/menus state information to the specified persistence medium.
  LoadBarState                  Reads the previously serialized toolbar/menus states.
  SaveCustomData                Saves the user customized information such as save/load custom baritems, which were created and added during application runtime.
  LoadCustomData                Loads the user customized information that was saved previously.
  ----------------------------- -----------------------------------------------------------------------------------------------------------------------------------


[] 

The Bar State can be saved/loaded using **AppStateSerializer** class and it can be used across multiple applications.

 

The default serialization option is Isolated storage and the System.IO.IsolatedStorage routines normally store application specific encrypted entries under the \'C:\\Documents and Settings\\\[USER name\]\\Local Settings\\Application Data\\IsolatedStorage\\' folder. All of the Essential Tools framework components use the \'Syncfusion.Runtime.Serialization. AppStateSerializer\' class in the Shared library for Read/Write. The AppStateSerializer is fully documented and can be initialized for different persistence mediums such as XML / Binary files, XML / Binary streams, and the Win32 Registry using its API.

 

The Bar States can be serialized in the following formats.

[] 

1.   Binary Format

2.   MemoryStream

3.   XML format

4.   Isolated Storage and

5.   WindowsRegistry

[] 

Persisting Bar state in Binary Format

[] 

To serialize in Binary Format, use the following code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [using][ Syncfusion.Runtime.Serialization;]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| [//Save Bar State in Binary format]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [//You can also use BinaryFmtStream instead of Binaryfile]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.][BinaryFile[,\"Barstate\");]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.mainFrameBarManager1.SaveBarState(app);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                  |
| [app.PersistNow ();]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [//Load Bar State in Binary format]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [//You can also use BinaryFmtStream instead of Binaryfile]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.][BinaryFile[,\"Barstate\");]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.mainFrameBarManager1.LoadBarState(app);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [Imports][ Syncfusion.Runtime.Serialization]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [\'Save Bar State in Binary format]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                     |
| [\'You can also use BinaryFmtStream instead of Binaryfile]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.BinaryFile, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.mainFrameBarManager1.SaveBarState(app)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [app.PersistNow ()]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [\'Load Bar State in Binary format]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                     |
| [\'You can also use BinaryFmtStream instead of Binaryfile]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.BinaryFile, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.mainFrameBarManager1.LoadBarState(app)]                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Persisting Bar State in Memory Stream

[] 

To persist the information in a database, we need to serialize the state into a **memory stream**. After which the stream is written into the database. The field to where the bar state is saved is binary.

**[]** 

Storing State

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| **[]**                                                                                          |
|                                                                                                                                                   |
| [// Saving Bar state to memory stream  ]                                                        |
|                                                                                                                                                   |
| [MemoryStream ms = [new] MemoryStream();]                                                |
|                                                                                                                                                   |
| [AppStateSerializer aser = [new] AppStateSerializer(SerializeMode.BinaryFmtStream, ms);] |
|                                                                                                                                                   |
| [this][.mainFrameBarManager1.SaveBarState(aser);]            |
|                                                                                                                                                   |
| [aser.PersistNow();]                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [\' Saving Bar state to memory stream  ]                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [Dim][ ms [As] MemoryStream = [New] MemoryStream()]                                                |
|                                                                                                                                                                                                                                   |
| [Dim][ aser [As] AppStateSerializer = [New] AppStateSerializer(SerializeMode.BinaryFmtStream, ms)] |
|                                                                                                                                                                                                                                   |
| [Me][.mainFrameBarManager1.SaveBarState(aser) ]                                                                                              |
|                                                                                                                                                                                                                                   |
| [aser.PersistNow() ]                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Persisting Bar state in XML Format

[] 

By default, the bar state will be stored into the default persistence medium, \'IsolatedStorage\'. To store the dock state to some other medium like XML, it could be done as follows:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [using][ Syncfusion.Runtime.Serialization;]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [//Save Bar State in XML format]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [//You can also use XMLFmtStream instead of XMLfile]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.XMLFile,\"Barstate\");] |
|                                                                                                                                                                                                                                                                                 |
| [this][.mainFrameBarManager1.SaveBarState(app);]                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [app.PersistNow ();]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [//Load Bar State in XML format]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [//You can also use XMLFmtStream instead of XMLfile]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.XMLFile,\"Barstate\");] |
|                                                                                                                                                                                                                                                                                 |
| [this][.mainFrameBarManager1.LoadBarState(app);]                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [Imports][ Syncfusion.Runtime.Serialization]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [\'Save Bar State in XML format]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [\'You can also use XMLFmtStream instead of XMLfile]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.XMLFile, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.mainFrameBarManager1.SaveBarState(app)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [app.PersistNow ()]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [\'Load Bar State in XML format]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [\'You can also use XMLFmtStream instead of XMLfile]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.XMLFile, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.mainFrameBarManager1.LoadBarState(app)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Persisting Bar state in Isolated Storage

**[]** 

To serialize in Isolated Storage medium, use the below code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [using][ Syncfusion.Runtime.Serialization;]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [//Save Bar State in Isolated storage]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.][IsolatedStorage[,\"Barstate\");]] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [this][.mainFrameBarManager1.SaveBarState(app);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| [app.PersistNow ();]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [//Load Bar State in Isolated storage]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.][IsolatedStorage[,\"Barstate\");]] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [this][.mainFrameBarManager1.LoadBarState(app);]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Imports][ Syncfusion.Runtime.Serialization]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\'Save Bar State in Isolated storage]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.IsolatedStorage, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.mainFrameBarManager1.SaveBarState(app)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [app.PersistNow ()]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\'Load Bar State in Isolated storage]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.IsolatedStorage, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.mainFrameBarManager1.LoadBarState(app)]                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Persisting Bar state in WindowsRegistry

**[]** 

To serialize in the WindowsRegistry, using the below code snippets.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                       |
| [using][ Syncfusion.Runtime.Serialization;]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [//Save Bar State in Windows Registry]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.][WindowsRegistry[,\"Barstate\");]] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [this][.mainFrameBarManager1.SaveBarState(app);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| [app.PersistNow ();]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [//Load Bar State in Windows Registry]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [AppStateSerializer app=][new][ AppStateSerializer (Syncfusion.Runtime.Serialization.SerializeMode.][WindowsRegistry[,\"Barstate\");]] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [this][.mainFrameBarManager1.LoadBarState(app);]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Imports][ Syncfusion.Runtime.Serialization]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\'Save Bar State in Windows Registry]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.WindowsRegistry, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.mainFrameBarManager1.SaveBarState(app)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [app.PersistNow ()]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\'Load Bar State in Windows Registry]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Private][ app [As] AppStateSerializer = [New] AppStateSerializer(Syncfusion.Runtime.Serialization.SerializeMode.WindowsRegistry, [\"Barstate\"])] |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.mainFrameBarManager1.LoadBarState(app)]                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}


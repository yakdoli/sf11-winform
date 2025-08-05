---
title: dockstatepersistence.md
original_path: WinForms_Docs/99_Uncategorized/dockstatepersistence.md
created_at: 2025-08-05
---






##### Dock State Persistence {#dock-state-persistence style="tab-stops: 0pt"}

[]{#p79}[] 

The docking behavior can be saved in the following formats.

[] 

[·      ]Binary Format

[·      ]XML Format

[·      ]IsolatedStorage medium

[·      ]MemoryStream

[·      ]PersistState property

[] 

The docking windows framework has a fully built-in serialization feature that provides automatic serialization of the form\'s docking state. In addition to this automatic dock state persistence during application termination and start, multiple intermediate docking states can be saved or loaded anytime using the programmatic API. The serialization mechanism is implemented using the standardized Syncfusion.Windows.Forms.AppStateSerializer component that acts as a central coordinator of all the Essential Tools components and provides the option to read / write to different media such as the default Isolated Storage, XML file, XML stream, Binary file, Binary stream and the Windows Registry.

**[]** 

Persisting Dock State in default storage

[] 

The dock state of a control can be persisted by setting the **PersistState** property of Docking manager. This information is stored in the Isolated storage.

[] 


  ----------------------------- ------------------------------------------------------------------------------------------------------
  DockingClientPanel Property   Description
  PersistState                  Gets or sets a value indicating whether the application\'s docking window state should be persisted.
  ----------------------------- ------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| **[]**                                                                                                  |
|                                                                                                                                                           |
| [this][.dockingManager1.PersistState = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| **[]**                                                                                               |
|                                                                                                                                                        |
| [Me][.dockingManager1.PersistState = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The DockingManager has built-in support for dock state serialization that can be enabled or disabled using the PersistState property. When the PersistState property is set to True, closing the form and hosting the docking windows will force the DockingManager to capture the current docking layout and serialize it using the Essential Studio AppStateSerializer serialization.

 

The default serialization option is Isolated storage and the System.IO.IsolatedStorage routines normally store application specific encrypted entries under the \'C:\\Documents and Settings\\\[USER name\]\\Local Settings\\Application Data\\IsolatedStorage\\\' folder. All of the Essential Tools framework components use the \'**Syncfusion.Runtime.Serialization.AppStateSerializer\'** class in the Shared library for Read/Write. The AppStateSerializer is fully documented and can be initialized for different persistence mediums such as XML / Binary files, XML / Binary streams, and the Win32 Registry using its API.

 

The default auto serialization implementation for the DockingManager uses a single instance of the AppStateSerializer that you can access through the **AppStateSerializer.GetSingleton()** method and reinitialize if necessary. But this single reinitialization should be done within the application's Main method before the first instance gets a chance to be created. Another option would be to use a custom instance of the AppStateSerializer and pass this to application-level invocations of the DockingManager\'s LoadDockState / SaveDockState routines.

[] 

LoadDockState and SaveDockState methods

[] 

LoadDockState

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Methods                           | Description                                                                                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| LoadDockState                     | Reads the persisted dockstate from the Isolated Storage.                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| LoadDockState (Overloaded)        | Reads a previously serialized dockstate using the AppStateSerializer object. Parameter is,                                |
|                                   |                                                                                                                           |
|                                   |                                                                                                                           |
|                                   |                                                                                                                           |
|                                   | *Serializer[ - ]*An instance of AppStateSerializer class.                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| LoadDockState (Overloaded)        | Reads a previously serialized dockstate for the specified dockable control and applies the new state. The parameters are, |
|                                   |                                                                                                                           |
|                                   |                                                                                                                           |
|                                   |                                                                                                                           |
|                                   | *Serializer[ - ]*An instance of AppStateSerializer class.                           |
|                                   |                                                                                                                           |
|                                   | *Ctrl[ ]*- Indicates the docked control.                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| **[]**                                                                                                                       |
|                                                                                                                                                                                |
| [this][.dockingManager1.LoadDockState();]                                                 |
|                                                                                                                                                                                |
| [this][.dockingManager1.LoadDockState(serializer);]                                       |
|                                                                                                                                                                                |
| [this][.dockingManager1.LoadDockState(serializer, [this].listBox1);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| **[]**                                                                                                                    |
|                                                                                                                                                                             |
| [Me][.dockingManager1.LoadDockState(serializer)]                                       |
|                                                                                                                                                                             |
| [Me][.dockingManager1.LoadDockState();]                                                |
|                                                                                                                                                                             |
| [Me][.dockingManager1.LoadDockState(serializer, [this].listBox1)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

SaveDockState

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------+
| Methods                           | Description                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------+
| SaveDockState                     | Saves the current dockstate to Isolated Storage.                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------+
| SaveDockState (Overloaded)        | Saves the current dockstate information to the specified AppStateSerializer. Parameter is,      |
|                                   |                                                                                                 |
|                                   |                                                                                                 |
|                                   |                                                                                                 |
|                                   | *Serializer[ - ]*An instance of AppStateSerializer class. |
+-----------------------------------+-------------------------------------------------------------------------------------------------+
| LoadDockState (Overloaded)        | Saves the dockstate information for the specified dockable control. The parameters are,         |
|                                   |                                                                                                 |
|                                   |                                                                                                 |
|                                   |                                                                                                 |
|                                   | *Serializer[ - ]*An instance of AppStateSerializer class. |
|                                   |                                                                                                 |
|                                   | *Ctrl[ ]*- Indicates the docked control.                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| **[]**                                                                                                                       |
|                                                                                                                                                                                |
| [this][.dockingManager1.SaveDockState();]                                                 |
|                                                                                                                                                                                |
| [this][.dockingManager1.SaveDockState(serializer);]                                       |
|                                                                                                                                                                                |
| [this][.dockingManager1.SaveDockState(serializer, [this].listBox1);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| **[]**                                                                                                                    |
|                                                                                                                                                                             |
| [Me][.dockingManager1.SaveDockState()]                                                 |
|                                                                                                                                                                             |
| [Me][.dockingManager1.SaveDockState(serializer)]                                       |
|                                                                                                                                                                             |
| [Me][.dockingManager1.SaveDockState(serializer, [this].listBox1)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Persisting Dock state in XML file

[] 

When the DockingManager\'s PersistState property is set, it will save the dock state into default persistence medium, \'IsolatedStorage\'. To store the dock state to some other medium like XML, it could be done as follows:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| **[]**                                                                                                                                |
|                                                                                                                                                                                         |
| [using][ Syncfusion.Runtime.Serialization;]                                                        |
|                                                                                                                                                                                         |
| [// Persist the dock state into XML File named Dock1.xml. Use this line in the constructor of Control which hosts the dockinglayout ] |
|                                                                                                                                                                                         |
| [public][ form1()]                                                                                 |
|                                                                                                                                                                                         |
| [{ ]                                                                                                                                                |
|                                                                                                                                                                                         |
| [AppStateSerializer.InitializeSingleton(SerializeMode.XMLFile,[\"Dock1\"]); ]                                                |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [Imports ][Syncfusion.Runtime.Serialization]                                                      |
|                                                                                                                                                                                        |
| [\' Persist the dock state into XML File named Dock1.xml.Use this line in the constructor of Control which hosts the dockinglayout ] |
|                                                                                                                                                                                        |
| [Private][ [Sub] [New]()]                               |
|                                                                                                                                                                                        |
| [        AppStateSerializer.InitializeSingleton(SerializeMode.XMLFile, [\"Dock1\"])]                                        |
|                                                                                                                                                                                        |
| [End Sub()]                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Persisting Dock State in Memory Stream

[] 

To persist docking information in a database, we need to serialize the state into a memory stream. After which the stream is written into the database. The field to where the dock state is saved is binary.

[] 

Storing State

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| **[]**                                                                                          |
|                                                                                                                                                   |
| [// Saving dockstate to memory stream  ]                                                        |
|                                                                                                                                                   |
| [MemoryStream ms = [new] MemoryStream();]                                                |
|                                                                                                                                                   |
| [AppStateSerializer aser = [new] AppStateSerializer(SerializeMode.BinaryFmtStream, ms);] |
|                                                                                                                                                   |
| [this][.dockingManager1.SaveDockState(aser);]                |
|                                                                                                                                                   |
| [aser.PersistNow();]                                                                                          |
|                                                                                                                                                   |
| [//Code to store the memory stream into database. Depends upon the database.]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [\' Saving dockstate to memory stream  ]                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [Dim][ ms [As] MemoryStream = [New] MemoryStream()]                                                |
|                                                                                                                                                                                                                                   |
| [Dim][ aser [As] AppStateSerializer = [New] AppStateSerializer(SerializeMode.BinaryFmtStream, ms)] |
|                                                                                                                                                                                                                                   |
| [Me][.dockingManager1.SaveDockState(aser) ]                                                                                                  |
|                                                                                                                                                                                                                                   |
| [aser.PersistNow() ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [\'Code to store the memory stream into database. Depends upon the database.]                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Retrieving State

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| **[]**                                                                                          |
|                                                                                                                                                   |
| [//Code to retrieve data(stream) from database]                                                 |
|                                                                                                                                                   |
| [MemoryStream ms = [new] MemoryStream(val);]                                             |
|                                                                                                                                                   |
| [ms.Position = 0;]                                                                                            |
|                                                                                                                                                   |
| [AppStateSerializer aser = [new] AppStateSerializer(SerializeMode.BinaryFmtStream, ms);] |
|                                                                                                                                                   |
| [this][.dockingManager1.LoadDockState(aser);]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [\'Code to retrieve data(stream) from database]                                                                                                                                 |
|                                                                                                                                                                                                                                   |
| [Dim][ ms [As] MemoryStream = [New] MemoryStream(value)]                                           |
|                                                                                                                                                                                                                                   |
| [ms.Position = 0]                                                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [Dim][ aser [As] AppStateSerializer = [New] AppStateSerializer(SerializeMode.BinaryFmtStream, ms)] |
|                                                                                                                                                                                                                                   |
| [Me][.dockingManager1.LoadDockState(aser)]                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To serialize in **Binary Format**, use the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                        |
| [// To Save]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [AppStateSerializer serializer =][ new][ AppStateSerializer(SerializeMode.][BinaryFile[, \"myfile\");]] |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.][dockingManager1[.]SaveDockState[(serializer);]]                                                                           |
|                                                                                                                                                                                                                                                                                                                        |
| [serializer.PersistNow();]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [// To Load]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| [AppStateSerializer serializer = ][new][ AppStateSerializer(SerializeMode.][BinaryFile[, \"myfile\");]] |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.][dockingManager1[.]LoadDockState[(serializer);]]                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' To Save]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ serializer ][As New][ AppStateSerializer(SerializeMode.][BinaryFile[, \"myfile\")]] |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.][dockingManager1[.]SaveDockState[(serializer)]]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                            |
| [serializer.PersistNow()]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                            |
| [\' To Load]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ serializer ][As New][ AppStateSerializer(SerializeMode.][BinaryFile[, \"myfile\")]] |
|                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.][dockingManager1[.]LoadDockState[(serializer)]]                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To serialize in **Isolated Storage** medium, use the below code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                             |
| [// To Save]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| [AppStateSerializer serializer =][ new][ AppStateSerializer(SerializeMode.][IsolatedStorage[, \"myfile\");]] |
|                                                                                                                                                                                                                                                                                                                             |
| [this][.][dockingManager1[.]SaveDockState[(serializer);]]                                                                                |
|                                                                                                                                                                                                                                                                                                                             |
| [serializer.PersistNow();]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [// To Load]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| [AppStateSerializer serializer = ][new][ AppStateSerializer(SerializeMode.][IsolatedStorage[, \"myfile\");]] |
|                                                                                                                                                                                                                                                                                                                             |
| [this][.][dockingManager1[.]LoadDockState[(serializer);]]                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' To Save]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ serializer ][As New][ AppStateSerializer(SerializeMode.][IsolatedStorage[, \"myfile\")]] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.][dockingManager1[.]SaveDockState[(serializer)]]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [serializer.PersistNow()]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' To Load]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ serializer ][As New][ AppStateSerializer(SerializeMode.][IsolatedStorage[, \"myfile\")]] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.][dockingManager1[.]LoadDockState[(serializer)]]                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**LoadDesignerDockState()** - The dock state that is set through visual designer can be restored by calling LoadDesignerDockState method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                         |
|                                                                                                                                        |
| **[]**                                                                               |
|                                                                                                                                        |
| [this][.dockingManager1.LoadDesignerDockState();] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                  |
|                                                                                                                                     |
| **[]**                                                                            |
|                                                                                                                                     |
| [Me][.dockingManager1.LoadDesignerDockState()] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

**GetSerializedControls -** Calling the GetSerializedControls method will return the serialized control collection enumerator in the specified serializer. This can be done through code as follows.

[] 


  ------------ ------------------------------------------
  Parameter    Description
  Serializer   An instance of AppStateSerializer class.
  ------------ ------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [this][.dockingManager1.GetSerializedControls(serializer);]                                                                                            |
|                                                                                                                                                                                                                                             |
| [Console][.Write([\"Serialized controls :\"] + [this].dockingManager1.GetSerializedControls(serializer));] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [Me][.dockingManager1.GetSerializedControls(serializer)]                                                                                            |
|                                                                                                                                                                                                                                          |
| [Console][.Write([\"Serialized controls :\"] + [Me].dockingManager1.GetSerializedControls(serializer))] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[ProvidePersistenceID Event]{.UGHyperlink}[, ]{.UGHyperlink}[How to avoid flickering while loading dock state?]{.UGHyperlink}[, ]{.UGHyperlink}

[How to serialize or deserialize the docking state for a docked control on loading the application?]{.UGHyperlink}[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[[]]{.UGHyperlink} 


[[Note: ]]{.UGHyperlink}PersistState property mechanism assumes that the DockingManger is hosted on a form and captures the docking layout on the host form's closing event. When DockingManager is hosted on a UserControl, LoadDockState and SaveDockState methods have to be called explicitly, on the Load and Closed events of the form that hosts the UserControl.

 

[[]]{.UGHyperlink} 


[]{#related-topics}


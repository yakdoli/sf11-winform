---
title: methods24.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\methods24.md
created_at: 2025-07-03
---






#### Methods {#methods style="tab-stops: 0pt"}

 


  Methods                                                                Description                                                                    Reference
  ---------------------------------------------------------------------- ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------
  ActivateWindow(string name)                                            Used to make a docking child as an ActiveWindow using the name of the child.   []{.UGHyperlink}
  DeleteDockState()                                                      Used to delete the State Persistence entries in registry.                      []{.UGHyperlink}
  DeleteDockState(string path)                                           Delete the given Persistence file where DockState is saved.                    []{.UGHyperlink}
  DeleteInternalIsolatedStorage()                                        Delete the Persistence file stored in Isolated Storage.                        []{.UGHyperlink}
  LoadDockState()                                                        Loads the DockState from the isolated storage.                                 []{.UGHyperlink}
  LoadDockState(string path)                                             Loads the Dockstate from the specified file.                                   []{.UGHyperlink}
  LoadDockState(BinaryFormatter serializer)                              Loads the Dockstate from the given BinaryFormatter.                            []{.UGHyperlink}
  LoadDockState(IFormatter formatter,StorageFormat format,string path)   Load the DockState from the given filename.                                    []{.UGHyperlink}
  LoadDockState(IsolatedStorageFile isofile,string Filename)             Loads the Dockstate from given isolated storage filename.                      []{.UGHyperlink}
  LoadDockState(TextReader reader)                                       Loads the DockState from TextReader.                                           []{.UGHyperlink}
  LoadDockState(XMLTextReader reader)                                    Loads the Dockstate from XMLTextReader.                                        []{.UGHyperlink}
  SetMDILayout(MDILayout layout)                                         Sets the MDILayout for Document child (Cascade, Horizontal, Vertical)          []{.UGHyperlink}
  SaveDockState()                                                        Saves the DockState of in IsolatedStorage location.                            []{.UGHyperlink}
  SaveDockState(BinaryFormatter serializer)                              Saves the DockState in the given BinaryFormatter object.                       []{.UGHyperlink}
  SaveDockState(IFormatter formatter,StorageFormat format,string path)   Saves the Dockstate in the given formatter with storage format.                []{.UGHyperlink}
  SaveDockState(IsolatedStorageFile isofile,string Filename)             Saves the DockState in the given Isolated storage file name.                   []{.UGHyperlink}
  SaveDockState(TextReader reader)                                       Saves the Dockstate in given TextReader object.                                []{.UGHyperlink}
  SaveDockState(XMLTextReader reader)                                    Saves the Dockstate in given XMLTextReader object.                             []{.UGHyperlink}
  SaveDockState(string path)                                             Saves the DockState in given file path.                                        []{.UGHyperlink}


 

 

 

 

[]{#related-topics}


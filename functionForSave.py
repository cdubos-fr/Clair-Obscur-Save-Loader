import os
import shutil
import stat
folderLocation = os.getenv('LOCALAPPDATA') + "/Sandfall/Saved/SaveGames"
AllSavePath = folderLocation + "/Save"
os.makedirs(AllSavePath,exist_ok=True)
for i in os.listdir(folderLocation) :
    if i.isdigit():
        CurrentSavePath = folderLocation+"/"+i
        break

def GetSavePath(Profile):
    return AllSavePath +"/"+Profile

def ImportSave(Name,Profile):
    if Profile == "":
        return False
    NewSavePath = AllSavePath +"/"+Profile+"/"+Name
    if os.path.exists(NewSavePath) :        
        os.chmod(NewSavePath,stat.S_IWUSR)
        shutil.rmtree(NewSavePath)
    shutil.copytree(CurrentSavePath,NewSavePath,dirs_exist_ok=True)
    return True

def DuplicateSave(Name,NameOfCopy,Profile):
    if Profile == "":
        return False
    OldSavePath = AllSavePath +"/"+Profile+"/"+Name
    NewSavePath = AllSavePath +"/"+Profile+"/"+NameOfCopy
    if os.path.exists(NewSavePath) :        
        os.chmod(NewSavePath,stat.S_IWUSR)
        shutil.rmtree(NewSavePath)
    shutil.copytree(OldSavePath,NewSavePath,dirs_exist_ok=True)
    return True

def RemoveSave(Name,Profile):
    if Profile == "":
        return False
    RemovedSavePath = AllSavePath +"/"+Profile+"/"+Name
    os.chmod(RemovedSavePath,stat.S_IWUSR)
    shutil.rmtree(RemovedSavePath)
    return True

def RenameSave(OldName,NewName,Profile):
    if Profile == "":
        return False
    OldNamePath = AllSavePath +"/"+Profile+"/"+OldName
    NewNamePath = AllSavePath +"/"+Profile+"/"+NewName
    os.rename(OldNamePath,NewNamePath)
    return True

def LoadSave(Name,Profile):
    if Profile == "":
        return False

    LoadedSavePath = os.path.join(AllSavePath, Profile, Name)

    if os.path.exists(CurrentSavePath):
        for i in os.listdir(CurrentSavePath):
            item_path = os.path.join(CurrentSavePath, i)
            if i == "Backup":
                for j in os.listdir(item_path):
                    os.remove(os.path.join(item_path, j))
            else:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)

    try:
        shutil.copytree(LoadedSavePath,CurrentSavePath,dirs_exist_ok=True)
    except Exception:
        return False

    return True

def GetListOfSave(Profile):
    return os.listdir(AllSavePath+"/"+Profile)

def GetListOfProfile():
    return os.listdir(AllSavePath)

def CreateProfile(Profile):
    if Profile == "":
        return False
    NewProfilePath = AllSavePath +"/"+Profile
    if os.path.exists(NewProfilePath) :
        return "Profile already exist"
    os.makedirs(NewProfilePath,exist_ok=True)
    return True

def DeleteProfile(Profile):
    if Profile == "":
        return False
    RemovedprofilePath = AllSavePath +"/"+Profile
    for root,dirs,files in os.walk(RemovedprofilePath):
        os.chmod(root,stat.S_IWUSR)
        for d in dirs:
            if d== "Backup":
                pass
            else:
                dirsPath = RemovedprofilePath + "/" + d
                for i in os.listdir(dirsPath):
                    if i=="Backup":
                        os.chmod(dirsPath+"/"+i,stat.S_IWUSR)
                os.chmod(dirsPath,stat.S_IWUSR)
    shutil.rmtree(RemovedprofilePath)
    return True

def DuplicateProfile(Profile, NameOfCopy):
    profilePath = AllSavePath +"/"+Profile
    CopyPath = AllSavePath +"/"+NameOfCopy
    shutil.copytree(profilePath,CopyPath,dirs_exist_ok=True)

def RenameProfile(Profile, NewName):
    OldProfilePath = AllSavePath +"/"+Profile
    NewProfilePath = AllSavePath +"/"+NewName
    os.rename(OldProfilePath,NewProfilePath)

    



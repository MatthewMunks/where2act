#!/usr/bin/env python3

from distutils.dir_util import copy_tree

WHERE_2_ACT_ROOT = "/home/matthewmunks/Documents/where2act/"

print();

def getStorageFurnitureFolderNames() -> list:
    # So we want to parse through ./stats/all_15cats.txt to get the file names of
    # the pieces of storage furniture.

    file_name = "stats/all_15cats.txt";

    file = open(WHERE_2_ACT_ROOT + file_name, 'r');

    lines = file.readlines();
    print(lines);

    output = [];

    for line in lines:
        line:str;
        split_line = line.split(' ')
        if split_line[1] == "StorageFurniture\n":
            output.append(split_line[0]);
    
    print(output);

    file.close();

    return output;

def copyFolders(copying_from:str, copy_items:list, copy_to:str):
    progress_bar = "";
    counter = 0;
    for item in copy_items:
        try:
            copy_tree(copying_from+item, copy_to+item);
            progress_bar += "|";
        except:
            progress_bar += ":";
        print(progress_bar + (len(copy_items)-counter) * " " + "EE");

        counter += 1;

if __name__=='__main__':

    storage_furniture = getStorageFurnitureFolderNames();

    test_data = [];
    training_data = [];

    for i in range(len(storage_furniture)):
        if i % 3 == 0:
            test_data.append(storage_furniture[i]);
        else:
            training_data.append(storage_furniture[i]);

    print("Copying training data");

    copyFolders(WHERE_2_ACT_ROOT + "data/where2act_original_sapien_dataset/", training_data,  WHERE_2_ACT_ROOT + "data/training/");

    print("Copying testing data");
    
    copyFolders(WHERE_2_ACT_ROOT + "data/where2act_original_sapien_dataset/", test_data,  WHERE_2_ACT_ROOT + "data/testing/");

    print("Finished");

    pass;

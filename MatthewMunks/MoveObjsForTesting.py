#!/usr/bin/env python3
"""
Moving stuff over from training to testing.
"""
import os;
import shutil;

ROOT_DIR = "/home/matthewmunks/Documents/where2act/data/"
TRAINING_DIR = "gt_data-train_1cat_train_data-pushing/"
TESTING_DIR = "gt_data-train_1cat_test_data-pushing/"
FILE_NAME = "data_tuple_list.txt";
FILE_NAME_2 = "data_tuple_list_2.txt";

OBJS_FOR_TESTING = ["35059", "38516", "40147", "40417", "40453", "41003", "41004", "41083", "41085", "41510", "41529", "44781", "44817", "44826"]

print("Moving...")

files_folders = os.scandir(ROOT_DIR + TRAINING_DIR);
for entity in files_folders:
    if entity.is_file():
        pass;
    elif entity.is_dir():
        for obj in OBJS_FOR_TESTING:
            if obj in entity.name:
                print("\tmoving", entity.path, "to", ROOT_DIR + TESTING_DIR + entity.name)
                shutil.move(entity.path, ROOT_DIR + TESTING_DIR + entity.name);
                break;
        pass;

print("Finished Moving");
print("Getting names...");

input();

training_output = "";
testing_output = "";

print(ROOT_DIR + TRAINING_DIR + FILE_NAME);
with open(ROOT_DIR + TRAINING_DIR + FILE_NAME, "r") as file:
    lines = file.read();
    print(lines);
    for line in lines.split("\n"):
        found = False;
        for obj in OBJS_FOR_TESTING:
            if obj in line:
                found = True;
                testing_output += line + "\n";
                break;
        if found is False:
            training_output += line + "\n";

print("Finished getting names")

print("-----TESTING OUTPUT-----");
with open(ROOT_DIR + TESTING_DIR + FILE_NAME_2, "w") as file:
    file.write(testing_output);

print("-----TRAINING OUTPUT-----");
with open(ROOT_DIR + TRAINING_DIR + FILE_NAME_2, "w") as file:
    file.write(training_output);
    
print("Finished");
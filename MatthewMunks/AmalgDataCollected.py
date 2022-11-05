#!/usr/bin/env python3
"""
This collects all the different data_tuple_list_e... files and amalgamates them into a single
file. Note that this will also remove the empty entries that only have a log.txt within them.
"""

import os;

ROOT_DIR = "/home/matthewmunks/Documents/where2act/data/gt_data-train_1cat_train_data-pushing/"

output = "";

files_folders = os.scandir(ROOT_DIR);
for entity in files_folders:
    if entity.is_file():
        print(entity.path);

        with open(entity.path) as file_reading:
            lines = file_reading.read();
            files_rejected = 0
            files_accepted = 0;
            for line in lines.split("\n"):
                scan_dir_out = list(os.scandir(ROOT_DIR + line));
                # print(scan_dir_out);
                if len(scan_dir_out) != 1:
                    output += line + "\n";
                    files_accepted += 1;
                else:
                    files_rejected += 1;
            print("files_accepted=", files_accepted, "files_rejected=", files_rejected);

# print(output);

with open(ROOT_DIR + "data_tuple_list.txt", "w") as output_file:
    output_file.write(output);

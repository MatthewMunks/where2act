echo $(date)

python gen_offline_data.py \
  --data_dir ../data/gt_data-train_1cat_train_data-pushing \
  --data_fn ../stats/train_1cat_train_data_list.txt \
  --category_types StorageFurniture \
  --primact_types pushing \
  --num_processes 7 \
  --num_epochs 60 \
  --ins_cnt_fn ../stats/ins_cnt_15cats.txt \
  --starting_epoch 411 \
  --out_fn data_tuple_list_e_411_470.txt

# --data_dir ../data/gt_data-train_10cats_train_data-pushing \
# --num_epochs 150 \

echo $(date)

# python gen_offline_data.py \
#   --data_dir ../data/gt_data-train_1cat_test_data-pushing \
#   --data_fn ../stats/train_1cat_test_data_list.txt \
#   --category_types StorageFurniture \
#   --primact_types pushing \
#   --num_processes 7 \
#   --num_epochs 50 \
#   --ins_cnt_fn ../stats/ins_cnt_15cats.txt \
#   --starting_epoch 1 \
#   --out_fn data_tuple_list_e_1_50.txt

echo $(date)

# --num_epochs 10 \

# python gen_offline_data.py \
#   --data_dir ../data/gt_data-test_5cats-pushing \
#   --data_fn ../stats/test_5cats_data_list.txt \
#   --primact_types pushing \
#   --num_processes 6 \
#   --num_epochs 10 \
#   --ins_cnt_fn ../stats/ins_cnt_5cats.txt


python train_3d_critic.py \
    --exp_suffix train_3d_critic \
    --model_version model_3d_critic \
    --primact_type pushing \
    --data_dir_prefix ../data/gt_data \
    --offline_data_dir ../data/gt_data-train_1cat_train_data-pushing \
    --val_data_dir ../data/gt_data-train_1cat_test_data-pushing \
    --val_data_fn data_tuple_list.txt \
    --train_shape_fn ../stats/train_1cat_train_data_list.txt \
    --ins_cnt_fn ../stats/ins_cnt_15cats.txt \
    --buffer_max_num 10000 \
    --num_processes_for_datagen 6 \
    --num_interaction_data_offline 50 \
    --num_interaction_data 1 \
    --sample_succ \
    --overwrite

# --offline_data_dir ../data/gt_data-train_10cats_train_data-pushing \
# --val_data_dir ../data/gt_data-train_10cats_test_data-pushing \
# --train_shape_fn ../stats/train_1cat_train_data_list.txt \

# train a character-level model on bitstrings
# similar to shakespeare_char.

out_dir = 'out-bitstrings'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'bitstrings'
wandb_run_name = 'bitstrings-run'

dataset = 'bitstrings'
gradient_accumulation_steps = 1
batch_size = 128
block_size = 16 # number of previous characters to consider

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384

# Dropout seems to make it worse. Maybe because the dataset is small?
# dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher

max_iters = 100000
lr_decay_iters = max_iters # make equal to max_iters usually

min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially
out_dir = 'out-finance_data'
eval_interval = 250
eval_iters = 200
log_interval = 10

dataset = 'finance_data'
gradient_accumulation_steps = 4  # reduce a bit
batch_size = 32                  # halve it to fit GPU
block_size = 256                 # smaller context length

# model
n_layer = 16                     # smaller but still capable
n_head = 16
n_embd = 384
dropout = 0.2

# training
learning_rate = 1e-4
max_iters = 20000
lr_decay_iters = 20000
min_lr = 1e-4
warmup_iters = 2000

# system
device = 'cuda'
compile = False  # disable compile to save ~2–3GB memory

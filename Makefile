LANGUAGE := marathi
TASK := pos_tag
REPRESENTATION := onehot
MODEL := linear
SHUFFLE := False
DATA_DIR := ./data
CHECKPOINT_DIR := ./checkpoints

REPRESENTATIONS_CONTEXTUAL := bert albert roberta
REPRESENTATIONS_UD := onehot random

DATA_PROCESS := $(if $(filter-out $(REPRESENTATION), random),$(REPRESENTATION),ud)
DATA_PROCESS := $(if $(filter-out $(REPRESENTATION), onehot),$(DATA_PROCESS),ud)

SHUFFLE_ARG := $(if $(filter-out $(SHUFFLE), True),,--shuffle-labels)
SHUFFLE_ARG := $(if $(filter-out $(SHUFFLE), true),$(SHUFFLE_ARG),--shuffle-labels)

UD_DIR_BASE := $(DATA_DIR)/ud

UDURL := https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3105/ud-treebanks-v2.5.tgz

UD_DIR := $(UD_DIR_BASE)/ud-treebanks-v2.5
UD_FILE := $(UD_DIR_BASE)/ud-treebanks-v2.5.tgz

PROCESSED_DIR_BASE := $(DATA_DIR)/processed/
PROCESSED_DIR := $(PROCESSED_DIR_BASE)/$(LANGUAGE)
PROCESSED_FILE_UD := $(PROCESSED_DIR)/train--ud.pickle.bz2
PROCESSED_FILE := $(PROCESSED_DIR)/test--$(DATA_PROCESS).pickle.bz2
PROCESSED_FILE_SHUFFLED := $(PROCESSED_DIR)/test--$(DATA_PROCESS)shuffled.pickle.bz2

TRAIN_DIR := $(CHECKPOINT_DIR)/$(TASK)/$(LANGUAGE)
TRAIN_MODEL := $(TRAIN_DIR)/$(MODEL)/$(REPRESENTATION)/finished.txt

COMPILED_RESULTS := results/compiled_$(TASK).tsv

# ifeq ($(REPRESENTATION), bert)
ifneq ($(filter $(REPRESENTATION),$(REPRESENTATIONS_UD)),)
all: get_ud process train
	echo "Finished everything"
else ifneq ($(filter $(REPRESENTATION),$(REPRESENTATIONS_CONTEXTUAL)),)
all: get_ud process_ud process process_shuffled train
	echo "Finished everything"
else
all: get_ud process_ud process train
	echo "Finished everything"
endif

get_results: $(COMPILED_RESULTS)

train: $(TRAIN_MODEL)

process: $(PROCESSED_FILE)

process_shuffled: $(PROCESSED_FILE_SHUFFLED)

process_ud: $(PROCESSED_FILE_UD)

get_ud: $(UD_DIR)

$(COMPILED_RESULTS):
	python -u src/h03_analysis/compile_results.py --checkpoint-path $(CHECKPOINT_DIR) --task $(TASK)

$(TRAIN_MODEL):
	echo "Train " $(REPRESENTATION) " representation"
	python -u src/h02_learn/random_search.py --language $(LANGUAGE) --data-path $(PROCESSED_DIR_BASE) --representation $(REPRESENTATION) --checkpoint-path $(CHECKPOINT_DIR) --task $(TASK) --model $(MODEL) $(SHUFFLE_ARG)
# 	python src/h02_learn/train.py --language $(LANGUAGE) --data-path $(PROCESSED_DIR_BASE) --representation $(REPRESENTATION) --checkpoint-path $(CHECKPOINT_DIR) --task $(TASK) --model $(MODEL) $(SHUFFLE_ARG)

# Preprocess data
$(PROCESSED_FILE):
	echo "Process language in ud " $(LANGUAGE)
	python src/h01_data/process.py --language $(LANGUAGE) --ud-path $(UD_DIR) --output-path $(PROCESSED_DIR_BASE) --representation $(DATA_PROCESS)

# Preprocess shuffled data
$(PROCESSED_FILE_SHUFFLED):
	echo "Process language in ud " $(LANGUAGE)
	python src/h01_data/process.py --language $(LANGUAGE) --ud-path $(UD_DIR) --output-path $(PROCESSED_DIR_BASE) --representation $(DATA_PROCESS)shuffled

# Preprocess ud base data
$(PROCESSED_FILE_UD):
	echo "Process language in ud " $(LANGUAGE)
	python src/h01_data/process.py --language $(LANGUAGE) --ud-path $(UD_DIR) --output-path $(PROCESSED_DIR_BASE) --representation ud

# Get Universal Dependencies data
$(UD_DIR):
	echo "Get ud data"
	mkdir -p $(UD_DIR_BASE)
	wget -P $(UD_DIR_BASE) $(UDURL)
	tar -xvzf $(UD_FILE) -C $(UD_DIR_BASE)

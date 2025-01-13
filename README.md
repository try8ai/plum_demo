# Plum AI

Plum AI is a developer API that evaluates and improves the quality of your LLM applications.

## Prerequisites

To get started all you need is a Plum API key. If you don't have one you can get one [here](https://auth.getplum.ai).

Use the following button to open the `api_key.py` file and then insert your API key where indicated.

<button data-command="open:api_key.py">Open `api_key.py`</button>

## Data

We've provided sample data for the demo.

<button data-command="open:data/input_output_pairs.json">Open `input_output_pairs.json`</button>

Optionally you can use your own data.  Just provide the following in a `json` file:
1. The system prompt you’ve been using
2. User prompts (inputs) you’ve sent to the LLM
3. Outputs that the LLM has returned

Then update the config to point at your data
<button data-command="open:config.py">Open `config.py`</button>

## Step 1

We will start by uploading our data. 
<button data-command="open:step1.py">Examine `Step 1`</button>

Lets upload the data now:
<button data-command="run:python3.12 step1.py; read">Run `Step 1: Upload Data`</button>

This will return a dataset ID which will be used later on.  Our script will store this ID in a file called `ids.json`.

## Step 2

The ability to evaluate your model comes from well-defined metrics. Plum creates criteria based on your business use case, which it then uses to score the model.
<button data-command="open:step2.py">Examine `Step 2`</button>

Lets generate metric definitions based updon the system prompt:
<button data-command="run:python3.12 step2.py; read">Run `Step 2: Generate Metric Definitions`</button>

This will return a metrics ID which will be stored in the `ids.json` file.

## Step 3

Plum returns a score for each of the criteria defined in the previous step. These scores are out of a maximum of **5**.
<button data-command="open:step3.py">Examine `Step 3`</button>

Let's run the evaluation:
<button data-command="run:python3.12 step3.py; read">Run `Step 3: Evaluation`</button>

These evaluation results will be used in the next step. Plum’s goal is to boost the lowest of these scores.

## Step 4

We now need to generate synthetic inputs and outputs, each pair being a variation of one of the seed pairs you uploaded in Step 1.
<button data-command="open:step4.py">Examine `Step 4`</button>

Adjust the `multiple` to adjust the size of the dataset you would like to generate. For each example in your seed dataset, Plum will generate `multiple` synthetic examples similar to it.

You will need at least 50-100 examples, so set the `multiple` accordingly.

Let's generate the synthetic data:
<button data-command="run:python3.12 step4.py; read">Run `Step 4: Generate Synthetic Data`</button>

## Step 5

We can now download the synthetic data in a format that OpenAI’s fine-tuning UI accepts. OpenAI provides the ability to fine-tune and customize their latest models. In order to do this, you will use the synthetic data that Plum generated in the previous step.
<button data-command="open:step5.py">Examine `Step 5`</button>

Lets download the data:
<button data-command="run:python3.12 step5.py; read">Run `Step 5`</button>

This will create a file `train.jsol`

## Step 6

1. Go to the OpenAI [fine-tuning page](https://platform.openai.com/finetune)
2. Click “Create”.
3. Upload new training data.
4. Optional: Select “Upload new” validation data. Drag your validation `.jsonl` file to upload.

After around 15 minutes, the fine-tuning run completes, and OpenAI will provide a customized model ID that you can start using.

**Congratulations!** You’ve completed one round of fine-tuning using Plum AI.

A complete python script can be found here:
<button data-command="open:plum.py">Examine `plum.py`</button>


Unlock your data flywheel: generate a new set of data using your fine-tuned model, create synthetic data using Plum AI, and start another round of fine-tuning.

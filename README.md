# SelectCode LLM-App

This repository contains the code for the practical component of the SelectCode AI Workshop.
Your task is to build the coolest application within the given time.

## Links
- [Slides](https://www.canva.com/design/DAFrFSYhC6c/_w-0KrluvJb7tIdJ04OrSw/view?utm_content=DAFrFSYhC6c&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)
- [API Key]() - Want to continue building after the workshop? You can easily create your own key in the [OpenAI portal](platform.openai.com/).


## Option 1: Langchain
<details>
  <summary>Details</summary>
  
If you just want to work directly with [LangChain](https://github.com/langchain-ai/langchain), simply install it using


```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
# For Windows
env\Scripts\activate
# For Unix or MacOS
source env/bin/activate

# Install langchain
pip install langchain
```
</details>

## Option 2: Chainlit
<details>
  <summary>Details</summary>

If you want to work with a pre-provided framework for a chat app, this repository contains some code to help you get started.

> ℹ️ The easiest way to get started is to use [this Colab](https://colab.research.google.com/drive/1lTHXzEa7o7hPqyUXvYVkyADaV1AR4zg8?usp=sharing). Note that this will your progress will not be saved unless you export the files manually.

Alternatively, to install locally:

```bash
# Clone the repo
git clone https://github.com/SelectCode/llm-example.git
```

Next, input the OpenAI API Key in the `.env` file (just copy and paste it)

```bash
# Navigate into the repo
cd ./llm-example

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
# For Windows
env\Scripts\activate

# For Unix or MacOS
source env/bin/activate

# Install the dependencies from the `requirements.txt` file
pip install -r requirements.txt

# Launch chainlit
chainlit run app.py -w
```

### Get started!
Now you can get started by integrating different langchain components into your application - have a look at `app.py`!
In `utils.py` we have provided some useful methods.

Looking for inspiration? Check out the [Chainlit documentation](https://docs.chainlit.io/integrations/langchain) or the [LangChain overview of popular chains](https://python.langchain.com/docs/modules/chains/popular/).
Also useful: the [Chainlit Cookbook](https://github.com/Chainlit/cookbook/).
You can find exciting examples with open APIs in the [Overview of Langchain API Chains](https://python.langchain.com/docs/modules/chains/popular/api), for example.
</details>


## Option 3: Langflow
<details>
  <summary>Details</summary>
  
If you prefer to work with a no-code tool instead, you could use Langflow. You can find more info in the [documentation](https://docs.langflow.org/).
  
> ℹ️ As long as you are fine with other people seeing your progress, you can use [our hosted platform](https://langflow.deploy.selectcode.dev/).
  
Otherwise you can either use the provided Colab (note that this will mean that your progress will not be saved unless you export the files manually) or install the tool locally by

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
# For Windows
env\Scripts\activate
# For Unix or MacOS
source env/bin/activate

# Install langflow
pip install langflow

# Launch langflow
langflow
```
</details>

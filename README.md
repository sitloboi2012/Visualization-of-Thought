# Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models
![pipeline](vot_banner.png)

This is the repository implements code for the paper [Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models](https://arxiv.org/pdf/2404.03622.pdf) and the model used in the paper are GPT-4-0125-Preview and GPT-4-Vision.

The paper propose a new prompting method which is called Visualization-of-Thought or VoT where LLM could visualize an imaginary visualization in their memory (Mind's Eye or Mental Images) and use that to help them solve problem that required visualize out each of the step in order to keep track and seeing the update of the changes.

## Setup

### 1. Local

```bash
git clone https://github.com/sitloboi2012/Visualization-Of-Thought.git
conda create --name vot python=3.11 -y
conda activate vot
set OPENAI_API_KEY=sk-123
pip install -r requirements.txt
```

### 2. Docker

```bash
TBA
```

## References
```bibtex
@misc{shao2024visual,
      title={Visualization-of-Thought Elicits Spatial Reasoning in Large Language Models}, 
      author={Wenshan Wu, Shaoguang Mao, Yadong Zhang, Yan Xia, Li Dong, Lei Cui, Furu Wei},
      year={2024},
      eprint={2404.03622},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
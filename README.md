# Hands-On Large Language Models

## What's this?

This repository contains my implementations of the projects from [Hands-On Large Language Models: Language Understanding and Generation](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961) written by [Jay Alammar](https://www.linkedin.com/in/jalammar/) and [Maarten Grootendorst](https://www.linkedin.com/in/mgrootendorst/) . For the official examples, please refer to the [official repository](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models).

## Table of contents

```
In progress!
```

## Requirements

- An NVIDIA GPU with a minimum of 16 GB of VRAM, or
- [Google Colab](https://colab.google) where an NVIDIA T4 GPU with 16 GB of VRAM can be accessed for free

The book mentions that not all chapters require a minimum of 16 GB of VRAM. However, some tasks, like training and fine-tuning, are more compute-intensive. Since the book is intended for those with limited GPU resources (like myself), all the code and models are designed to run on Google Colab.

## Local environment setup

### Prerequisites

1. Install Xcode from App Store

2. Verify Xcode command line tools (it should show: `/Applications/Xcode.app/Contents/Developer`)

```bash
xcode-select -p
```

3. Agree to Xcode license

```bash
sudo xcodebuild -license
```

### Installation

1. Create a [Conda](https://docs.conda.io/) environment

```bash
conda create -n handsonllm python=3.12
```

2. Activate the environment

```bash
conda activate handsonllm
```

3. Install necessary dependencies

```bash
pip install -r requirements.txt
```
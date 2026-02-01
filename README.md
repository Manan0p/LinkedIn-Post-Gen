---
title: LinkedIn Post Gen
emoji: 🚀
colorFrom: red
colorTo: red
sdk: streamlit
sdk_version: 1.31.0
app_file: main.py
pinned: false
---

# LinkedIn Post Generator

This tool will analyze posts of a LinkedIn influencer and help them create new posts based on the writing style in their old posts.

## Technical Architecture

1. **Stage 1**: Collect LinkedIn posts and extract Topic, Language, Length etc. from it.
2. **Stage 2**: Now use topic, language and length to generate a new post. Some of the past posts related to that specific topic, language and length will be used for few shot learning to guide the LLM about the writing style etc.

## Setup

1. Get an API_KEY from https://console.groq.com/keys
2. Add `GROQ_API_KEY` to Hugging Face Space secrets
3. The app will run automatically!

Copyright (C) Codebasics Inc. All rights reserved.

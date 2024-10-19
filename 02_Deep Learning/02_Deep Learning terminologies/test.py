from llama_cpp import Llama
# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path="/home/arjun/Desktop/tinyllama-1.1b-chat-v1.0.Q5_K_S.gguf",  # Download the model file first
  n_ctx=1024,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35,         # The number of layers to offload to GPU, if you have GPU acceleration available
  verbose=False,
)

system_message = '''You will be given text extracted from a resume. 
You should take the contents and then classify the skills present in the resume into the following categories:
1. Technical skills
2. Social skills
3. Other skills
4. Exprience
5. Overall score for the resume (on a scale from 0 to 100)
'''

prompt = '''
The following are the details extracted from the resume:
```
Name: Isabel Schumacher
Job: Graphics Designer
Education
Wardiere University
Senior Graphic Designer
Bachelor of Design

Contact:

+123-456-7890
hello@reallygreatsite.com
123 Anywhere Street., Any City

Experience:
Fauget studio (2011 -2015)
create more than 100 graphic designs for big companies

YMI Studio(2014 -2019)
complete a lot of complicated work
create more than 100 graphic designs for big companies

larana, inc3.65(2020 -2023)
complete a lot of complicated work

Skills
Branding
SEO
Web Design
Marketing
Graphic Design

Language
English
French
```
Ensure that you will respond with only the information that is provided. 
Now extrat the relevant skills from the 
# 1. Skill 1
- <put skills here>
- <put skills here>

You should take the contents and then classify the skills present in the resume into the following categories:
1. Technical skills
2. Social skills
3. Other skills
4. Exprience

After that give an overall score for the resume (on a scale from 0 to 100)

'''

output = llm(
  f"<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>", # Prompt
  max_tokens=500,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=False,        # Whether to echo the prompt
  temperature=0,
  top_k=20,
  top_p=0.1,
  stream=True
)
for chunk in output:
    print(chunk['choices'][0]['text'], end='', flush=True)
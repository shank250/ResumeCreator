# from langchain.chains import LLMChain,  RunnableSequence
# from langchain.chains import SimpleSequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import AnthropicLLM, ChatAnthropic
from langchain_core.runnables.utils import ConfigurableField

model = ChatAnthropic(temperature=0, model='claude-3-opus-20240229',       anthropic_api_key="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"
    )

# Define the chains to be chained together
# chain1 = ...
# chain2 = ...


# JOB_DESCRIPTION = 
# import sys
# JOB_DESCRIPTION = ""
# while True:
#     line = input()
#     if line == "":  # Check for empty line to indicate user finished input
#         break
#     JOB_DESCRIPTION += line + "\n"
# import threading
# import sys

# def timeout_handler():
#     print("Time limit reached!")
#     sys.stdin.close()  # Close standard input to stop waiting for input

# # Set your desired time limit in seconds
# time_limit = 10

# # Start the timer thread
# timer = threading.Timer(time_limit, timeout_handler)
# timer.start()

# # Capture job description
# JOB_DESCRIPTION = "".join(sys.stdin.readlines())

# # Wait for the timer thread to finish (optional)
# timer.join()
# # JOB_DESCRIPTION = "".join(sys.stdin.readlines())  # Read all lines from standard input
# print(JOB_DESCRIPTION)
def aboutReturn(JOB_DESCRIPTION):
    # template = f"""Here is a job description for a role:

    # <job_description>
    # {JOB_DESCRIPTION}
    # </job_description>

    # Please read through this job description carefully. Identify the key skills, qualifications, and experience that a candidate should have in order to be a good fit for this role. 

    # Extract these skills and create a concise bulleted list summarizing the most important qualifications based solely on the job description. Focus only on skills and qualifications that are explicitly stated in the description or very strongly implied by the responsibilities and requirements.

    # Organize and output the final list of key skills inside <skills> tags. For example:

    # <skills>
    # - Skill 1
    # - Skill 2
    # - Skill 3
    # </skills>

    # Carefully review the job description and create the skills list for an ideal candidate resume now.

    # RESPONSE:
    # On the basis of the given, skills create a resume's about section.(keep the word limit 50 - 60 words)
    # I need only resume about section and no other information and tags.
    # REMEMBER:
    # Remove such lines from response:'Based on the job description, here is a concise summary of the key skills and qualifications for the Software Engineer intern role in a resume about section:'

    # """
    template = f"""
    JOB DESCRIPTION:
    {JOB_DESCRIPTION}
    RESPONSE: 
    ON the basis of the given above job description craete a resume's about section, project section, skills section as accordign to the jab description.
    It should be in proper format which can be directly pasted into resume.Use html tags to write in like resume like format
    NOTE: Do not write a single extra character except  about, project and skilld section
"""
#     template = """
# **JOB DESCRIPTION:**
# {JOB_DESCRIPTION}

# **RESPONSE:**

# Based on the provided job description, I can craft your resume's About, Projects, and Skills sections. Here's the formatted content you can directly paste into your resume:

# **About**

# <html>
#   <p>{Write a compelling summary about yourself highlighting relevant skills and experience based on the job description.}</p>
# </html>

# **Projects**

# <html>
#   <h2>Projects</h2>
#   <ul>
#     <li>
#       **{Project Title 1}** ({Year}) - {Brief description of the project and your contributions, emphasizing skills relevant to the job description.}
#     </li>
#     <li>
#       **{Project Title 2}** ({Year}) - {Brief description of the project and your contributions, emphasizing skills relevant to the job description.}
#     </li>
#     </ul>
# </html>

# **Skills**

# <html>
#   <h2>Skills</h2>
#   <ul>
#     <li>{Skill 1} (proficient/intermediate/basic)</li>
#     <li>{Skill 2} (proficient/intermediate/basic)</li>
#     <li>{Skill 3} (proficient/intermediate/basic)</li>
#     </ul>
# </html>

# **Please note:**

# * Replace `{JOB_DESCRIPTION}` with the actual job description.
# * Fill in the bracketed sections with your specific information.
# * You can adjust the formatting (e.g., font size, spacing) to match your resume's style.
# """
    skillsets_list =  model.invoke(template).content
    print(skillsets_list)
    # print("*"*40)

    # templateAboutSection = f"""
    # Skills: {skillsets_list}
    # ---
    # On the basis of the given, skills create a resume's about section.(keep the word limit 50 - 60 words)

    # """
    # result = skillsets_list.split("<skills")[1][2:-9]


    # skillsets_list = model.invoke(templateAboutSection).content
    # print(skillsets_list)
    return skillsets_list
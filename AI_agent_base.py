import autogen
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("API_KEY"))
config_list =[
    {
        'model': os.getenv("MODEL"),
        'api_key': os.getenv("API_KEY")
    }
]

llm_config = {
    # 'request_timeout': 600,
    'seed': 42,
    'config_list': config_list,
    'temperature': 0
}

assistent = autogen.AssistantAgent(
    name = 'assistent',
    llm_config= llm_config
)

user_proxy = autogen.UserProxyAgent(
    name = 'user_proxy',
    human_input_mode= "TERMINATE",
    max_consecutive_auto_reply= 10,
    is_termination_msg= lambda x:x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config= {"work_dir":"web", "use_docker":False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task1 = """write a python code for the following problem and below is the deatils,
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

once the code is validated save the code with the name 'testcase1.py'
"""
task3 = "python code to find vocabulary letters are present in the string or not, if presented provide the total count of identified letters and save the code with the name 'testcase1.py'"
task = "summarize the article in following link: 'https://medium.com/towards-data-science/building-a-chat-app-with-langchain-llms-and-streamlit-for-complex-sql-database-interaction-7433245079f3' and save the summary in text file "
user_proxy.initiate_chat(
    assistent,
    message=task
)
import os
from python_on_whales import docker

output = docker.run(
    "iqvia:repoA" , ["/results/aaa.xlsx", "para1", "para2"],
    volumes=[(os.path.abspath("./OUTPUTS"), "/results")] 
)
print(output)
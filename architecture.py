# diagram.py
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.security import IAMPermissions
from diagrams.aws.devtools import Codepipeline, Codebuild
from diagrams.aws.management import CloudformationStack
from diagrams.aws.general import Users
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram("ServiceControlPolicyAutomation", show=True):
    with Cluster("Security Tooling Account"):
        with Cluster("Pipeline"):
            pipeline = Codepipeline("CDK Pipeline")
            cdksynth = Codebuild("CDK Synth")
            
    pipeline >> cdksynth
    with Cluster("Delegated Organizations Account"):
        with Cluster("Stage Deploy"):
            cfstack = CloudformationStack("CloudFormation-Stack")
            sso = IAMPermissions("Service Control Policy")


    # download the icon image file
    github_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    github_icon = "github.png"
    urlretrieve(github_url, github_icon)

    github = Custom("Github PR Review, Test validation of Policy & Merge", github_icon)
    
    folks = Users("Contributers")
    cdksynth >> cfstack
    cfstack >> sso
    folks >>  Edge(label="Pull Request") >> github
    github >> Edge(label="Trigger Pipeline") >> pipeline
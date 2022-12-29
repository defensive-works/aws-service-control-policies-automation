from aws_cdk import (
	App, Stack,
	pipelines as pipelines
)

from deploy import PipelineStage
from constructs import Construct


class PipelineStack(Stack):

	def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
		super().__init__(scope, construct_id, **kwargs)


		# This creates the CodePipeline to deploy the CDK Stack across accounts using the Github connection which was created using the console manually.
		pipeline = pipelines.CodePipeline(
			self, 'AutomatedServiceControlPolicies-Pipeline',
			pipeline_name='AutomatedServiceControlPolicies-Pipeline',
			cross_account_keys=True,
			synth=pipelines.ShellStep("Synth",
				input=pipelines.CodePipelineSource.connection("defensive-works/aws-service-control-policies-automation", 'main',
					connection_arn="arn:aws:codestar-connections:us-east-1:920024193878:connection/12eccab1-8799-430d-a936-07ab5a7ee1ef",
				),
				commands=[
					"npm install -g aws-cdk",	
					"pip install -r requirements.txt",
					"npx cdk synth"
					]
				)
			)


		deploy_stage = pipeline.add_stage(PipelineStage(
			self, 'DeployServiceControlPoliciesAutomation'
		))
		

# Initialize and Call Class Stack
app = App()
PipelineStack(app, 'AutomatedServiceControlPolicies-Pipeline-Stack', env = {'account': '920024193878', 'region': 'us-east-1'})
app.synth()

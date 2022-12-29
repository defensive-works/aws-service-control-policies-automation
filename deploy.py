from aws_cdk import (
	Stage
)
from constructs import Construct

from stacks.service_control_policies_stack import AutomatedSCPStack

enforcement_account_env = {'account': '920024193878', 'region': 'us-east-1'}
#org_account_env = {'account': '466200656080', 'region': 'us-east-1'} 


class PipelineStage(Stage):
	def __init__(self, scope: Construct, id: str, **kwargs):
		super().__init__(scope, id, **kwargs)

		servicecontrolpoliciesautomation_stack = AutomatedSCPStack(self, 'ServiceControlPoliciesAutomation-Stack', env = enforcement_account_env)

